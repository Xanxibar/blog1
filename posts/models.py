from django.conf import settings 
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='P')

class Post(models.Model):
    STATUS_CHOICES = (
        ('D', 'draft'),
        ('P', 'published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='D')
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-publish"]

    def __str__(self):
        return self.title

    @property
    def c_count(self):
        return self.comments.count()

    def get_absolute_url(self):
        return reverse('posts:post_detail', 
        args=[
            self.publish.year,
            self.publish.strftime('%b').lower(),
            self.publish.strftime('%d'),
            self.slug
        ])

    def get_archive_year(self):
        return reverse('year_archive', kwargs={'year':self.publish.year})

    def get_archive_month(self):
        return reverse(
            'month_archive', args=[self.publish.year, self.publish.strftime('%b').lower()])

    def get_archive_day(self):
        return reverse(
            'day_archive', args=[
                self.publish.year, self.publish.strftime('%b').lower(), 
                self.publish.strftime('%d')])
    
    def get_archive_today(self):
        return reverse('today_archive')


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, related_name="replies")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return  "{} on {}".format(self.name, self.post)


class Tag(models.Model):
    posts = models.ManyToManyField(Post, related_name="tags")
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique=True)
    weight = models.PositiveIntegerField(default=1)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("posts:tag_detail", args=[self.slug])

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Tag, self).save(*args, **kwargs)