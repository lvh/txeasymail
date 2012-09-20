from email import Charset, generator, header
from email.mime import multipart, text

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


# Yay global state!
Charset.add_charset('utf-8', Charset.QP, Charset.QP, 'utf-8')


def buildMessage(headers, parts):
    message = multipart.MIMEMultipart('alternative')

    for name, value in headers.iteritems():
        multipart[name] = _encodeHeader(value)

    for partType, part in parts.iteritems():
        mt = text.MIMEText(part.encode("utf-8"), partType, "UTF-8").encode()
        message.attach(mt)

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


def messageToFile(message):
    """
    Flattens a message into a file-like object.
    """
    outFile = StringIO()
    messageGenerator = generator.Generator(outFile, False)
    messageGenerator.flatten(message)
    outFile.seek(0, 0)
    return outFile
