from typing import Iterable


def reverse_string(string):
    return string[::-1]


def split_strings(s):
    result = []
    x = 0
    try:
        while x < len(s):
            result.append(s[x] + s[x + 1])
            x += 2
    except IndexError:
        result.append(s[len(s) - 1] + "_")
    return result


def first_word(text: str) -> str:
    result = text.split()
    return result[0]


def is_acceptable_password(password: str) -> bool:
    try:
        password[6]
        return True

    except IndexError:
        return False


def number_length(a: int) -> int:
    result = 1
    while a >= 10:
        a = a / 10
        print("a " + str(a))
        result += 1
    return result


def end_zeros(num: int) -> int:
    result = 0
    temp = str(num)
    for x in str(num)[::-1]:
        if x == "0":
            result += 1
        else:
            return result
    return result


def backward_string(val: str) -> str:
    return val[::-1]


def remove_all_before(items: list, border: int) -> Iterable:
    try:
        return items[items.index(border):]
    except ValueError:
        return items


def is_all_upper(text: str) -> bool:
    temp = text.replace(' ', '')
    if temp.isupper() or temp == "" or not temp.isalpha():
        return True
    return False


def replace_first(items: list) -> Iterable:
    if len(items) > 1:
        items.append(items.pop(0))
    return items


def max_digit(number: int) -> int:
    result = [int(x) for x in str(number)]
    return max(result)


def split_pairs(a: str):
    if len(a) == "":
        return a
    if len(a) % 2 != 0:
        a += "_"
    result_list = []
    x = 0
    while x < len(a):
        result_list.append(a[x]+a[x+1])
        x += 2
    return result_list


def beginning_zeros(number: str) -> int:
    result = 0
    for x in number:
        if x == "0":
            result += 1
        else:
            break
    return result


def nearest_value(values: set, one: int) -> int:
    closest = int()
    for x in values:
        print(x)
        print(closest)
        if closest == 0:
            closest = x
            continue
        if x == one:
            return x
        if int.__abs__(one - x) < int.__abs__(one - closest):
            closest = x
    return closest


def between_markers(text: str, begin: str, end: str) -> str:
    return text[(text.find(begin).__index__()+1):text.find(end).__index__()]


def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    if not text.endswith("."):
        text += "."
    return text

'''
MAIN
'''

print(correct_sentence("twoja stara"))
print(correct_sentence("welcome to New York"))