# --------------
# User Instructions
#
# Write a function is_anagram(string1, string2) that takes two
# strings as input and returns True if the strings are anagrams of each
# other and False otherwise.
#
# Your program is correct if it passes all tests

def is_anagram(string1, string2):
    # put your code here
    return True

def is_anagram(string1, string2):
    string1 = sorted(string1.lower().replace(' ', '')) 
    string2 = sorted(string2.lower().replace(' ', ''))
    return string1 == string2

def test():
    assert is_anagram('Mary', 'army') is True
    assert is_anagram('education', 'knowledge') is False
    assert is_anagram('dormitory', 'dirty room') is True
    assert is_anagram('Tom Marvolo Riddle', 'I am Lord Voldemort') is True
    assert is_anagram('humanities', 'ah minuets') is False
    assert is_anagram('digital', 'computer') is False
    assert is_anagram('A Wheat Sissy', 'This was easy') is True
    return 'all tests passed'


print test()