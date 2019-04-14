white_rabit = "I'm late! I'm late! For a very important date!"
s = "    I'm feeling spaced out.     "
white_queen = "Jam tommorrow and jam yesterday - but never jam today."

def count_vowels(s):
    ''' (str) -> int

    Return the number of vowels in string s.
    
    >>> count_vowels("Happy Anniversary!")
    5
    >>> count_vowels("xyz")
    0
    '''

    num_vowels = 0

    for char in s:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1

    return num_vowels


def collect_vowels(s):
    ''' (str) -> str

    Return the vowels from s.

    >>> collect_vowels("Happy Anniversary!")
    'aAiea'
    >>> collect_vowels("xyz")
    ''
    '''

    vowels = ''
    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char

    return vowels
