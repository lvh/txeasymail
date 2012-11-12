"""
Support e-mail templates in Markdown.
"""
import markdown


class MarkdownTemplate(object):
    """
    An e-mail template formatted in Markdown.
    """
    def __init__(self, subject, body):
        """
        Initializes a Markdown template.
        """
        self._subject = subject
        self._body = body


    def evaluate(self, context):
        """
        Evaluates the markdown source in the given context, producing HTML
        and (Markdown) plain text. Also interpolates the subject line with
        the given context.
        """
        headers = {"Subject": self._subject.format(**context)}

        md = self._source.format(**context)
        html = markdown.markdown(md)
        parts = {"text/html": html, "text/plain": md}
        return headers, parts
