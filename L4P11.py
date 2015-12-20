def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    vowelrange=['a','A','e','E','i','I','o','O','u','U']
    booltest=(char in vowelrange)
    return booltest
