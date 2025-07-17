import mimetypes

def attachment(file):
    mime_type, _ = mimetypes.guess_type(file)
    mime_type, mime_subtype = mime_type.split('/', 1)
    return mime_type, mime_subtype
