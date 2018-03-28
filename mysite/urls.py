from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from posts.sitemaps import PostSitemap

sitemaps = {'posts':PostSitemap,}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("posts.urls", namespace="posts")),
    path(
        'sitemap.xml', sitemap, {'sitemaps':sitemaps},  
        name='django.contrib.sitemaps.views.sitemaps'),
]


from django.conf import settings

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns