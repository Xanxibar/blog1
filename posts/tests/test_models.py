import time
from django.urls import reverse
from django.utils import timezone

from .initial_setup import BaseTestSetup



class TestPostModel(BaseTestSetup):

     
    def test_get_absolute_url(self):
        """For a given post titled 'Post title', the reversed url
        should be '/<year>/<month>/<day>/post-title/' ."""
        url = reverse('posts:post_detail', kwargs={
            'year':self.year, 'month':self.month, 'day':self.day, 'slug':self.post.slug})
        expected_url = '/{}/{}/{}/post-title/'.format(self.year, self.month, self.day)
        self.assertEqual(expected_url, url)
        print("TESTPOSTMODEL: test_get_absolute_url")
    


class TestTagModel(BaseTestSetup):
    
    
    def test_get_absolute_url(self):
        """For a given tag with the name 'testtag', the reversed url
        should be '/tag/testtag/'. """
        url = reverse("posts:tag_detail", kwargs={'slug':self.tag.slug})
        expected_url = '/tag/testtag/'
        self.assertEqual(expected_url, url)
        print("TESTTAGMODEL: test_get_absolute_url")

    

    