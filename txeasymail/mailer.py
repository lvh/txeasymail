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
