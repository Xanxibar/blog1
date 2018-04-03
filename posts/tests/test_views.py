import time
from django.urls import reverse


from .initial_setup import BaseTestSetup
from ..views import PostListView



class TestPostListView(BaseTestSetup):
    
    
    def test_posts_available_at_url(self):
        """Test that a list of posts is available at the 
        url given in the urlconf."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['posts']) >= 1)
        print("TESTPOSTLISTVIEW: test_posts_available_at_url")
    
        
    def test_correct_view_is_being_used(self):
        """Tests that the correct view is being used to 
        put out a response."""
        response = self.client.get('/')
        self.assertEqual(
            response.resolver_match.func.__name__, 
            PostListView.as_view().__name__)
        print("TESTPOSTLISTVIEW: test_correct_view_is_being_used")

    def test_correct_template_is_used(self):
        """Tests that the template used for rendering a posts list
        is 'post_list.html'. """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'posts/post_list.html')
        print("TESTPOSTLISTVIEW: test_correct_temlate_is_being_used")


class TestPostDetailView(BaseTestSetup):
    
    
    def test_post_available_at_url(self):
        """Test that a given post can be found at the 
        url declared in the urlconf."""
        response = self.client.get(
            '/{}/{}/{}/post-title/'.format(self.year, self.month, self.day))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post title')
        print("TESTPOSTDETAILVIEW: test_post_is_available_at_url")
    