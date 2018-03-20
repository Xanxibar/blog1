from django.urls import path
from django.views.generic.dates import ArchiveIndexView

from .feeds import AtomPostsFeed, RssPostsFeed
from .models import Post
from .views import (post_detail, post_share, tag_cloud, PostListView, TagDetailView,
PostDayArchiveView, PostMonthArchiveView, PostTodayArchiveView, 
PostWeekArchiveView, PostYearArchiveView)


app_name="posts"
urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:slug>/', 
        post_detail, name="post_detail"),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('archive/', ArchiveIndexView.as_view(
        model=Post, date_field='publish'), name='post_archive'),
    path('archive/<int:year>/', PostYearArchiveView.as_view(), name="year_archive"),
    path('archive/<int:year>/<str:month>/', PostMonthArchiveView.as_view(),
         name="month_archive"),
    path('archive/<int:year>/week/<int:week>/',
         PostWeekArchiveView.as_view(),
         name="week_archive"),
    path('archive/<int:year>/<str:month>/<int:day>/',
         PostDayArchiveView.as_view(),
         name="day_archive"),
    path('today/',
         PostTodayArchiveView.as_view(),
         name="today_archive"),
    path('feed/atom', AtomPostsFeed(), name='atom_feed'),
    path('feed/rss', RssPostsFeed(), name='rss_feed'),
    path('tags/', tag_cloud, name='tag_cloud'),
    path('tag/<slug:slug>/', TagDetailView.as_view(), name="tag_detail"),
    
]