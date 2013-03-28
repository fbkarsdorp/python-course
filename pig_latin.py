#! /usr/bin/env python3
# -*- coding: utf8 -*-


VOWELS = 'aeiouAEIOU'

def starts_with_vowel(word):
    "Does the word start with a vowel?"
    return word[0] in VOWELS

def add_ay(word):
    "Add 'ay' at the end of the word."
    return word + 'ay'

def convert_word(word):
    "Convert a word to latin (recursive style)."
    if not starts_with_vowel(word):
        return convert_word(word[1:] + word[0])
    return add_ay(word)

def convert_word_imperative(word):
    "Convert a word to latin (imperative style)."
    start = 0
    end = ''
    for i, char in enumerate(word):
        if char not in VOWELS:
            end += char
        else:
            start = i
            break # break out of the loop
    return add_ay(word[start:] + end)

def convert_text(text):
    "Convert all words in a sentence to latin."
    return ' '.join(convert_word(word) for word in text.split())
