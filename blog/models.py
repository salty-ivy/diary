
"""
App model for Blog realted pages and logic
"""

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from home.models import StandardPage


class BlogIndexPage(StandardPage):
    """
    For indexing/listing blog pages
    """
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]
