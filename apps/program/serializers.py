from rest_framework import serializers

from .models import Program, Episode, Category
from embed_video.backends import detect_backend
from sorl.thumbnail import get_thumbnail
from apps.favorite.models import Favorite


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')
        readonly_fields = ('id', 'name', 'slug')


class ProgramSerializer(serializers.ModelSerializer):
    thumbnail_300x300 = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()
    category = CategorySerializer()

    class Meta:
        model = Program
        fields = ('id', 'title', 'description', 'episodes', 'slug', 'category', 'thumbnail_300x300', 'is_favorite')
        readonly_fields = ('id', 'episodes', 'category', 'slug')

    def get_thumbnail_300x300(self, obj):
        try:
            return get_thumbnail(obj.image, '300x300', crop='center', quality=99).url
        except:
            return ""

    def get_is_favorite(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated():
            try:
                return True if Favorite.objects.get_favorite(request.user, obj) else False
            except Favorite.DoesNotExist:
                pass # Hasnt favorite

        return False


class EpisodeSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()
    thumbnail_300x300 = serializers.SerializerMethodField()
    parent_slug = serializers.SerializerMethodField(read_only=True)
    category = serializers.SerializerMethodField()
    video_backend = serializers.SerializerMethodField()
    video_code = serializers.SerializerMethodField()

    class Meta:
        model = Episode
        fields = ('title', 'description', 'slug', 'program', 'pub_date', 'id', 'thumbnail_300x300', 'short_description',
                  'parent_slug', 'category', 'video_url', 'video_backend', 'video_code')

    def get_video_url(self, obj):
        return detect_backend(obj.video).url

    def get_video_backend(self, obj):
        return detect_backend(obj.video).backend

    def get_video_code(self, obj):
        return detect_backend(obj.video).get_code()

    def get_thumbnail_300x300(self, obj):
        try:
            return get_thumbnail(obj.image, '300x300', crop='center', quality=99).url
        except:
            return ""

    def get_parent_slug(self, obj):
        return obj.program.slug

    def get_category(self, obj):
        return CategorySerializer(instance=obj.program.category).data
