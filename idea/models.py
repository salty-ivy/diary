
"""
App model for Idea realted pages and logic
"""

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from home.models import StandardPage, StandardIndexPage


class IdeaIndexPage(StandardIndexPage):
    """
    For indexing/listing idea pages
    """
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]


class IdeaPage(StandardPage):
    pass
