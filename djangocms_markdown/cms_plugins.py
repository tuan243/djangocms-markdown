"""Implementation of CMSPluginBase class for ``cmsplugin-markdown``."""
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_markdown.models import MarkdownPlugin


class MarkdownCMSPlugin(CMSPluginBase):
    model = MarkdownPlugin
    name = _('Markdown')
    render_template = 'djangocms_markdown/markdown.html'
    change_form_template = 'djangocms_markdown/change_form.html'


plugin_pool.register_plugin(MarkdownCMSPlugin)
