from django.urls import reverse
from django.utils import timezone

from .initial_setup import BaseTestSetup
from ..models import Post, Comment, Tag


class TestPostModel(BaseTestSetup):

    
    def test_get_absolute_url(self):
        """For a given post titled 'Post title', the reversed url
        should be '/<year>/<month>/<day>/post-title/' ."""
        year = timezone.now().year
        month = timezone.now().strftime('%b').lower()
        day = timezone.now().day
        url = reverse('posts:post_detail', kwargs={
            'year':year, 'month':month, 'day':day, 'slug':self.post.slug})
        expected_url = '/{}/{}/{}/post-title/'.format(year, month, day)
        self.assertEqual(expected_url, url)



class TestTagModel(BaseTestSetup):
    
    def test_get_absolute_url(self):
        """For a given tag with the name 'testtag', the reversed url
        should be '/tag/testtag/'. """
        url = reverse("posts:tag_detail", kwargs={'slug':self.tag.slug})
        expected_url = '/tag/testtag/'
        self.assertEqual(expected_url, url)

    