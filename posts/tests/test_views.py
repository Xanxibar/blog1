from django.urls import reverse
from django.utils import timezone

from .initial_setup import BaseTestSetup
from ..models import Post, Comment, Tag
from ..views import PostListView


class TestPostListView(BaseTestSetup):

    def test_posts_available_at_url(self):
        """Test that a list of posts is available at the 
        url given in the urlconf."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['posts']) >= 1)
        
    def test_correct_view_is_being_used(self):
        """Tests that the correct view is being used to 
        put out a response."""
        response = self.client.get('/')
        self.assertEqual(
            response.resolver_match.func.__name__, 
            PostListView.as_view().__name__)

    def test_correct_template_is_used(self):
        """Tests that the template used for rendering a posts list
        is 'post_list.html'. """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'posts/post_list.html')
    