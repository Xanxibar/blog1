from django.urls import path
from django.views.generic.dates import ArchiveIndexView

from .feeds import LatestPostsFeed
from .models import Post
from .views import (post_detail, post_share, tag_cloud, PostListView, TagDetailView,
PostYearArchiveView)


app_name="posts"
urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:slug>/', 
        post_detail, name="post_detail"),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('archive/', ArchiveIndexView.as_view(
        model=Post, date_field='publish'), name='post_archive'),
    path('archive/<int:year>/', PostYearArchiveView.as_view(), name="post_year_archive"),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('tags/', tag_cloud, name='tag_cloud'),
    path('tag/<slug:slug>/', TagDetailView.as_view(), name="tag_detail"),
    
]