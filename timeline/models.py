from django.db import models as models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.search import index

MED_LENGTH = 255
MAX_LENGTH = 1023


class IndexPage(Page):
    description = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='index_description'),
    ]

    def get_context(self, request, *args, **kwargs):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blog_posts = Post.objects.live().specific().order_by('-date')
        context['blog_posts'] = blog_posts
        return context


class Post(Page):
    intro = models.CharField(max_length=MAX_LENGTH)
    date = models.DateField("Post Date")
    body = RichTextField()

    search_fields = [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='post_intro'),
        FieldPanel('date', classname='post_date'),
        FieldPanel('body', classname='post_body'),
    ]
