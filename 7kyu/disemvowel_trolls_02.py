def disemvowel(string_):
    result = ''
    for char in string_:
        if char not in 'aeiouAEIOU':
            result += char
    return result


# Solution #2
# def disemvowel(string_):
#     return ''.join(x for x in string_ if x.lower() not in 'aeiou')


# Your task is to write a function that takes a string and return a new string with all vowels removed.
#
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
#
# Note: for this kata y isn't considered a vowel.
