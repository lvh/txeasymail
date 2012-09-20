import lxml.html
import lxml.html.clean


def textFromHTML(html):
    """
    Cleans and parses text from the given HTML.
    """
    cleaner = lxml.html.clean.Cleaner(scripts=True)
    cleaned = cleaner.clean_html(html)
    return lxml.html.fromstring(cleaned).text_content()
