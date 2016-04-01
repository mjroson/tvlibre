from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from rest_framework import routers

from apps.comments.views import ThreadedCommentViewSet
from apps.favorite.views import FavoriteModelViewSet
from apps.notification.views import NotificationModelViewSet
from apps.program.views import EpisodeViewSet, ProgramViewSet, CategoryListAPIView
from apps.user.views import CustomRegisterView

from .views import IndexView

#admin.site.index_template = 'index.html'
admin.site.site_title = 'Tv Libre - Panel de administracion'
admin.site.site_header = 'Tv Libre - Panel de administracion'

router = routers.DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'episodes', EpisodeViewSet)
router.register(r'comments', ThreadedCommentViewSet)
router.register(r'favorites', FavoriteModelViewSet)
router.register(r'notifications', NotificationModelViewSet)
#router.register(r'categories', CategoryListAPIView)

urlpatterns = [
    url(r'^api/v1/categories/$', CategoryListAPIView.as_view()),
    url(r'^api/v1/', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^cuenta/signup/$', CustomRegisterView.as_view(), name='custom_register'),
    url(r'^cuenta/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', IndexView.as_view()),
]


if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                           ) + staticfiles_urlpatterns() + urlpatterns