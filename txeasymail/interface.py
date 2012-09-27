"""
Interface definition.
"""
from zope import interface


class IMailer(interface.Interface):
    def send(sender, recipient, content):
        """
        Sends the content over e-mail to the recipient as the sender.
        """
