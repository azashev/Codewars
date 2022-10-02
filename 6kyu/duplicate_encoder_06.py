def duplicate_encode(word):
    word = word.lower()
    result = ''
    for ch in word:
        if word.count(ch) > 1:
            result += ')'
        else:
            result += '('

    return result



# Solution #2
#
#
# def duplicate_encode(word):
#     word = word.lower()
#     result = ''.join([')' if word.count(x) > 1 else '(' for x in word])
#
#     return result


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
# The goal of this exercise is to convert a string to a new string where each character in the new string
# is "(" if that character appears only once in the original string, or ")" if that character appears more than once in
# the original string. Ignore capitalization when determining if a character is a duplicate.
#
#
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("
