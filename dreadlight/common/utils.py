import unicodedata


def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())


def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def jsonify_boolean(boolean):
    if boolean:
        return 'true'
    else:
        return 'false'
