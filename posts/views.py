import datetime
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.dates import (DayArchiveView, MonthArchiveView, 
TodayArchiveView, WeekArchiveView, YearArchiveView)
from django.views.generic.detail import SingleObjectMixin


from .forms import CommentForm, EmailPostForm
from .mixins import PageLinksMixin
from .models import Post, Tag


class PostListView(PageLinksMixin, ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = settings.PAGINATE_BY
    



def post_detail(request, year, month, day, slug):
    month = datetime.datetime.strptime(month.title(), '%b').strftime('%m')
    post = get_object_or_404(
        Post, slug=slug, status='P', publish__year=year, 
        publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = False
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    post_tags_ids =  post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(
        same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(
        request, 'posts/post_detail.html', 
        {
            'post':post, 'comments':comments,
             'comment_form':comment_form, 'new_comment':new_comment,
             'similar_posts':similar_posts,
             }
             )


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status="P")
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = '{} ({}) recommends you reading "{}"'.format(
                cd['name'], cd['email'], post.title
                )
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(
                post.title, post_url, cd['name'], cd['comments']
                )
            if cd['email'] and cd['to'] and cd['name']:
                try:
                    send_mail(subject, message, 'django-sparkpost@sparkpostbox.com', 
                    [cd['to']], fail_silently=False)
                    sent = True
                except BadHeaderError:
                    return HttpResponse("Invalid Header Found")
    else:
        form = EmailPostForm()
    return render(request, 'posts/share.html', {'post':post, 'form':form, 'sent':sent})



def tag_cloud(request):
    MAX_WEIGHT = 5
    tags = Tag.objects.order_by('name')
    tags = tags.annotate(
        num_posts=Count('posts')).order_by('num_posts')
    count = tags.count()
    max_count, min_count = tags[count-1].posts.count(), tags[0].posts.count()
    range = float(max_count - min_count)
    if range == 0:
        range = 1
    for tag in tags:
        tag.count = tag.posts.count()
        tag.weight = int(((tag.count - min_count)/range) * MAX_WEIGHT)
        tag.save()
    return render(request, 'posts/tag_cloud.html', {'tags':tags.order_by('name')})
    

class TagDetailView( SingleObjectMixin, PageLinksMixin, ListView):
    paginate_by = settings.PAGINATE_BY
    template_name = "posts/tag_detail.html"
    context_object_name = "tag"


    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Tag.objects.all())
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.posts.all()


class PostYearArchiveView(YearArchiveView):
    queryset = Post.published.all()
    date_field = 'publish'
    make_object_list = True
    allow_future = False
    allow_empty = True


class PostMonthArchiveView(MonthArchiveView):
    queryset = Post.published.all()
    date_field = 'publish'
    allow_future = False
    allow_empty = True


class PostWeekArchiveView(WeekArchiveView):
    queryset = Post.published.all()
    date_field = "publish"
    week_format = "%U"
    allow_future = False
    allow_empty = True


class PostDayArchiveView(DayArchiveView):
    queryset = Post.published.all()
    date_field = "publish"
    allow_future = False
    allow_empty = True


class PostTodayArchiveView(TodayArchiveView):
    queryset = Post.published.all()
    date_field = "publish"
    allow_future = False
    allow_empty = True