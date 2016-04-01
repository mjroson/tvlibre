import itertools
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.html import format_html
from django.utils.text import slugify


from embed_video.admin import AdminVideoMixin

from sorl.thumbnail import get_thumbnail

from .models import Program, Episode, Category
from .forms import EpisodeForm, ProgramForm


class EpisodeAdminInline(AdminVideoMixin, admin.StackedInline):
    form = EpisodeForm
    model = Episode
    extra = 0


class RelatedFieldCheckLimitByUser(admin.RelatedFieldListFilter):
    def field_choices(self, field, request, model_admin):
        try:
            limit_choices_to = {'pk__in': set(request.user.programs.all().values_list('id', flat=True))}
        except:
            limit_choices_to = {}

        return field.get_choices(include_blank=False, limit_choices_to=limit_choices_to)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('show_image', 'title', 'q_episodes', 'add_episode')
    search_fields = ('title',)
    list_display_links = ('title', 'show_image')
    form = ProgramForm
    readonly_fields = ('q_episodes', 'add_episode')
    #inlines = [EpisodeAdminInline,]

    def show_image(self, instance):
        if instance.image:
            return format_html('<img class="item-program-img" src="{url}" />',
                               url=get_thumbnail(instance.image, '300x300', crop='center', quality=99).url)
        else:
            return format_html('<img class="item-program-img" src="/static/img/default_episode.png" />')

    show_image.short_description = 'Imagen'

    def q_episodes(self, instance):
        return instance.episodes.all().count()

    q_episodes.short_description = 'Cantidad de episodios'

    def add_episode(self, instance):
        url = reverse('admin:program_episode_add') + '?program=%s' %(instance.id)
        return format_html('<a title="Añadir nuevo episodio" class="addlink" href="{url}">Episodio</a>', url=url)

    add_episode.short_description = 'Acciones'

    def get_queryset(self, request):
        qs = super(ProgramAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user.id)

        return qs



    class Media:
        js = [
            '/static/bower_components/tinymce/tinymce.min.js',
            '/static/js/tiny_setup.js'
            ]
        css = {
            "all": ('/static/css/admin/program_list.css',)
        }

    def save_model(self, request, obj, form, change):
        obj.user = request.user

        if not obj.slug:
            max_length = Program._meta.get_field('slug').max_length
            obj.slug = orig = slugify(obj.title)[:max_length]

            for x in itertools.count(1):
                if not Program.objects.filter(slug=obj.slug).exists():
                    break
                obj.slug = '%s-%d' % (orig, x)

        return super(ProgramAdmin, self).save_model(request, obj, form, change)


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('show_image', 'title', 'program', 'pub_date')
    search_fields = ('title', 'program__name')
    list_display_links = ('title', 'show_image')
    form = EpisodeForm
    list_filter = (
        ('program', RelatedFieldCheckLimitByUser),
    )

    def show_image(self, instance):
        if instance.image:
            return format_html('<img class="item-program-img" src="{url}" />',
                               url=get_thumbnail(instance.image, '300x300', crop='center', quality=99).url)
        else:
            return format_html('<img class="item-program-img" src="/static/img/default_episode.png" />')

    show_image.short_description = 'Imagen'

    def get_queryset(self, request):
        qs = super(EpisodeAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(program__in=request.user.programs.all().values_list('id', flat=True))

        return qs

    def get_form(self, request, obj=None, **kwargs):
        form = super(EpisodeAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['program'].queryset = Program.objects.filter(user=request.user.id)
        return form

    class Media:
        js = [
            '/static/bower_components/tinymce/tinymce.min.js',
            '/static/js/tiny_setup.js'
            ]
        css = {
            "all": ('/static/css/admin/program_list.css',)
        }

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')




admin.site.register(Program, ProgramAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Category)