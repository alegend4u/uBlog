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


class Post(Page):
    intro = models.CharField(max_length=MAX_LENGTH)
    timestamp = models.DateField("Post Date")
    body = RichTextField()

    search_fields = [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='post_intro'),
        FieldPanel('timestamp', classname='post_timestamp'),
        FieldPanel('body', classname='post_body'),
    ]
