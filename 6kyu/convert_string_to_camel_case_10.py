def to_camel_case(text):
    text = text.replace('_', '-')
    text = text.split('-')

    result = list(text[0])
    res = [x.capitalize() for x in text[1:]]
    result += res
    return ''.join(result)


print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))


# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was
# capitalized (known as Upper Camel Case, also often referred to as Pascal case).
#
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
