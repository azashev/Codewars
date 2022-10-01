def get_count(sentence):
    result = 0
    for x in sentence:
        if x in "aeiou":
            result += 1
    return result



# # Solution #2:
#
# def get_count(sentence):
#     return len([x for x in sentence if x in 'aeiou'])


# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.
