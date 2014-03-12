import string

def strip_punctuation(s):
    """Return the text without (hopefully...) any punctuation.
    >>> strip_punctuation('this.is?as!funny@word') == 'thisisasfunnyword'
    """
    return ''.join(ch for ch in s if ch not in string.punctuation)

def clean_text(text):
	return strip_punctuation(text.lower())