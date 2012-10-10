from email import Charset, generator, header
from email.mime import multipart, text
from email.utils import formataddr, parseaddr

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


# Yay global state!
Charset.add_charset('utf-8', Charset.QP, Charset.QP, 'utf-8')


def buildMessage(headers, parts):
    """
    Builds a message from some headers and MIME parts.
    """
    message = multipart.MIMEMultipart('alternative')

    for name, value in headers.iteritems():
        name = name.title()
        if name == "From":
            multipart[name] = _encodeAddress(value)
        elif name in ["To", "Cc", "Bcc"]:
            multipart[name] = _encodeAddresses(value)
        else:
            multipart[name] = _encodeHeader(value)

    for partType, part in parts.iteritems():
        mimeText = text.MIMEText(part.encode("utf-8"), partType, "UTF-8")
        message.attach(mimeText.encode())

    return message


def _encodeHeader(headerValue):
    """
    Encodes a header value.

    Returns ASCII if possible, else returns an UTF-8 encoded e-mail header.
    """
    try:
        return headerValue.encode('ascii', 'strict')
    except UnicodeError:
        encoded = headerValue.encode("utf-8")
        return header.Header(encoded, "UTF-8").encode()


def _encodeAddress(address):
    """
    Encodes an address.

    This parses the address into the real name and the actual address. Each
    part is then encoded as per ``_encodeHeader``.
    """
    return formataddr(map(_encodeHeader, parseaddr(address)))


COMMASPACE = ", "


def _encodeAddresses(addresses):
    """
    Encodes multiple e-mail addresses.

    Splits on a comma followed by a space to produce individual addresses.
    Each such address is then encoded as per ``_encodeAddress``.
    """
    return COMMASPACE.join(map(_encodeAddress, addresses.split(COMMASPACE)))


def messageToFile(message):
    """
    Flattens a message into a file-like object.
    """
    outFile = StringIO()
    messageGenerator = generator.Generator(outFile, False)
    messageGenerator.flatten(message)
    outFile.seek(0, 0)
    return outFile
