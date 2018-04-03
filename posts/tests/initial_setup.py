from django.test import Client, TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

from ..models import Comment, Post, Tag
User = get_user_model()

class BaseTestSetup(TestCase):

          
    def setUp(self):
        self.client = Client()
        self.mylo = User.objects.create(
            username="mylo",
            email="mylomann@gmail.com",
            password="simplepass1"
        )
        
        self.post = Post.objects.create(
            title="Post title",
            slug="post-title",
            author=self.mylo,
            text="This is just  a sample post.",
            status='P'
        )

        Comment.objects.create(
            name=self.mylo,
            email='mylomann@gmail.com',
            text="this is a comment.",
            post=self.post,
        )
        self.tag = Tag(name="testtag", slug="testtag")
        self.tag.save()
        self.tag.posts.add(self.post)
        self.tag.save()
        self.year = timezone.now().year
        self.month = timezone.now().strftime('%b').lower()
        self.day = timezone.now().day
    
