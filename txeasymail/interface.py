"""
Interface definition.
"""
from zope import interface


class IMailer(interface.Interface):
    """
    An object that sends e-mail.
    """
    def send(sender, recipient, content):
        """
        Sends the content to the recipient as the sender.
        """



class ITemplate(interface.Interface):
    """
    An e-mail template.
    """
    def evaluate(context):
        """
        Evaluates a template given a context.

        Returns a pair of headers and parts that can be used to build a MIME
        message.
        """
