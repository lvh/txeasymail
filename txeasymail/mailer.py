"""
Tools for sending e-mail.
"""
from OpenSSL import SSL

from twisted.internet import defer, ssl
from twisted.mail import smtp


_CONTEXT_FACTORY = ssl.ClientContextFactory()
_CONTEXT_FACTORY.method = SSL.TLSv1_METHOD



class Mailer(object):
    """
    Sends e-mail.
    """
    def __init__(self, endpoint, credentials):
        self._endpoint = endpoint
        self._authentication = [credentials.username, credentials.password]
        self._factoryKwargs = {"contextFactory": _CONTEXT_FACTORY}


    def send(self, sender, recipient, content):
        d = defer.Deferred()

        args = self._authentication + [sender, recipient, content, d]
        factory = smtp.ESMTPSenderFactory(*args, **self._factoryKwargs)

        return self.endpoint.connect(factory).addCallback(lambda _ign: d)



def _nop(headers, parts):
    """
    A no-op.
    """


def sendTemplate(mailer, sender, recipient, template, context, hook=_nop):
    """
    Simple case for sending some e-mail using a template.
    """
    headers, parts = template.evaluate(context)
    headers["From"] = sender
    headers["To"] = recipient
    hook(headers, parts)

    content = mime.buildMessage(headers, parts)
    return mailer.send(sender, recipient, content)
