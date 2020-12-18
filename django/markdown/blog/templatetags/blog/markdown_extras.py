# blog/templatetags/markdown_extras.py
from django import template
from django.template.defaultfilters import stringfilter
from pygments import highlight

import markdown as md

register = template.Library()


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)


@register.filter()
@stringfilter
def markdown(value):
    renderer =
    """
    'markdown.extensions.fenced_code', 'markdown.extensions.extra', 'markdown.extensions.abbr', 'markdown.  extensions.attr_list', 'markdown.extensions.def_list', 'markdown.extensions.fenced_code', 'markdown.extensions.   footnotes', 'markdown.extensions.md_in_html', 'markdown.extensions.tables', 'markdown.extensions.admonition',  'markdown.extensions.codehilite', 'markdown.extensions.legacy_attrs', 'markdown.extensions.legacy_em',   'markdown.extensions.meta', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'markdown. extensions.smarty', 'markdown.extensions.toc', 'markdown.extensions.wikilinks'
    """
    renderer = HighlightRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(value, extensions=['markdown.extensions.fenced_code', ])
    # return md.markdown(value, extensions=['markdown.extensions.fenced_code', ])
