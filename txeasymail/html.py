"""
Stuff related to HTML e-mail.
"""
import lxml.html
import lxml.html.clean


class UnsafeHTMLTemplate(object):
    """
    An unsafe HTML e-mail template.
    """
    def __init__(self, source):
        self._source = source


    def evaluate(self, context):
        """
        Interpolates the HTML source with the context, then returns that HTML
        and the text extracted from that html.
        """
        html = self._source.format(**context)
        parts = {"text/html": html, "text/plain": textFromHTML(html)}
        return {}, parts



def textFromHTML(html):
    """
    Cleans and parses text from the given HTML.
    """
    cleaner = lxml.html.clean.Cleaner(scripts=True)
    cleaned = cleaner.clean_html(html)
    return lxml.html.fromstring(cleaned).text_content()
