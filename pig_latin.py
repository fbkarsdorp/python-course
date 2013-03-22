
VOWELS = 'aeiouAEIOU'

def starts_with_vowel(word):
    return word[0] in VOWELS

def add_ay(word):
    return word + 'ay'

def convert_word(word):
    if not starts_with_vowel(word):
        return convert_word(word[1:] + word[0])
    return add_ay(word)

def convert_text(text):
    return ' '.join(convert_word(word) for word in text)
