from typing import Tuple

from django.db import models as models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField
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

    api_fields = [
        APIField("description"),
    ]

    def get_context(self, request, *args, **kwargs):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blog_posts = Post.objects.live().specific().order_by('-date')
        context['blog_posts'] = blog_posts
        return context


class Post(Page):
    intro = models.CharField(max_length=MAX_LENGTH)
    body = RichTextField()

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='post_intro'),
        FieldPanel('body', classname='post_body'),
    ]

    api_fields = [
        APIField('intro'),
        APIField('body'),
        APIField('last_published_at'),
    ]

    def get_siblings_by_published_date(self) -> Tuple:
        try:
            prev_sibling = Post.objects.filter(
                **{f"{Post.last_published_at.field.name}__lt": self.last_published_at}
            ).latest(Post.last_published_at.field.name)
        except Post.DoesNotExist:
            prev_sibling = None

        try:
            next_sibling = Post.objects.filter(
                **{f"{Post.last_published_at.field.name}__gt": self.last_published_at}
            ).earliest(Post.last_published_at.field.name)
        except Post.DoesNotExist:
            next_sibling = None

        return prev_sibling, next_sibling
