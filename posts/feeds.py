from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.utils.feedgenerator import Atom1Feed

from .models import Post

class RssPostsFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'Latest entries from my blog'

    def items(self):
        return Post.published.all()[:5]


    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.text, 30)


class AtomPostsFeed(RssPostsFeed):
    feed_type = Atom1Feed
    subtitle = RssPostsFeed.description