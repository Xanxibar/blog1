from django import template
from django.db.models import Count

from ..models import Comment, Post, Tag


register = template.Library()


@register.simple_tag(name='posts_count')
def total_posts():
    return Post.published.count()


@register.inclusion_tag('posts/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}


@register.inclusion_tag('posts/tag_cloud_trunc.html')
def tag_cloud(count=100):
    tags = Tag.objects.order_by('name')[:count]
    return {'tags':tags}


@register.simple_tag(name='comments_count')
def total_comments():
    return Comment.objects.filter(active=True).count()


@register.simple_tag(name='tags_count')
def total_comments():
    return Tag.objects.count()


@register.simple_tag(name='commented_posts')
def commented_posts():
    comments = Post.published.filter(comments__gte=1).distinct().count()
    return comments
