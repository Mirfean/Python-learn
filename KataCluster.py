from typing import Iterable
from typing import Union
import copy


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
        result_list.append(a[x] + a[x + 1])
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
    return text[(text.find(begin).__index__() + 1):text.find(end).__index__()]


def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    if not text.endswith("."):
        text += "."
    return text


def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


def sum_numbers(text: str) -> int:
    temp_list = text.split()
    result = 0
    for x in temp_list:
        if x.isdigit():
            result += int(x)
    return result


def checkio(array: list) -> int:
    result = 0
    if not len(array) == 0:
        for x in array[::2]:
            result += x
            print(str(result))
        result *= array.pop()
    return result


def checkio2(words: str) -> bool:
    my_list = words.split()
    counter = 0
    for x in my_list:
        if x.isalpha():
            counter += 1
            if counter == 3:
                return True
        else:
            counter = 0
    return False


def first_word(text: str) -> str:
    text.replace(".", " ")
    text.replace(",", " ")
    result = str()
    for x in text:
        if x.isalpha() or x == "'":
            result += x
        elif len(result) > 0:
            break
    return result


def days_diff(a, b):
    from datetime import datetime
    date_a = datetime(year=a[0], month=a[1], day=a[2])
    date_b = datetime(year=b[0], month=b[1], day=b[2])
    result = date_a - date_b
    return int.__abs__(result.days)


def count_digits(text: str) -> int:
    result = 0
    for i in text:
        if i.isdigit():
            result += 1
    return result


def backward_string_by_word(text: str) -> str:
    '''
    not done :(
    :param text:
    :return:
    '''
    return text


def second_index(text: str, symbol: str) -> [int, None]:
    result = text.find(symbol, text.find(symbol) + 1)
    if result < 0:
        return None
    return result


def popular_words(text: str, words: list) -> dict:
    text_list = text.lower().split()
    words_dict = {}
    for x in words:
        words_dict[x] = 0
    for single_word in text_list:
        if single_word in words_dict or single_word.title() in words_dict:
            words_dict[single_word] += 1

    print(words_dict)
    return words_dict


# safe pawns V1
def safe_pawnsV1(pawns: set) -> int:
    result = 0
    copy_pawns = copy.copy(pawns)
    for pawn in copy_pawns:
        safe_square, safe_square2 = 0, 0
        if pawn[0] != "a" and pawn[0] != "h":
            safe_square = chr(ord(pawn[0])-1) + str(int(pawn[1])+1)
            safe_square2 = chr(ord(pawn[0])+1) + str(int(pawn[1])+1)
            if safe_square in pawns:
                print("ss1")
                result += 1
                pawns.discard(safe_square)
            if safe_square2 in pawns:
                print("ss2")
                result += 1
                pawns.discard(safe_square2)
        else:
            if pawn[0] == "a":
                safe_square = chr(ord(pawn[0]) + 1) + str(int(pawn[1]) + 1)
                if safe_square in pawns:
                    print("a")
                    result += 1
                    pawns.discard(safe_square)
            else:
                safe_square = chr(ord(pawn[0]) - 1) + str(int(pawn[1]) + 1)
                if safe_square in pawns:
                    print("h")
                    result += 1
                    pawns.discard(safe_square)

        print("result " + str(result) + " pawns remain:" + str(len(pawns)))
    return result

# /safe pawns V1


def getdiags(pawn):
    c, r = map(ord, pawn)
    return chr(c - 1) + chr(r - 1), chr(c + 1) + chr(r - 1)


def safe_pawns(pawns):
    return len([p for p in pawns if any(d in pawns for d in getdiags(p))])


def sun_angle(time: str) -> Union[int, str]:
    if not int(time.replace(":", "")) in range(600, 1801):
        return "I don't see the sun!"
    return (int(time[0:2]) - 6)*15 + int(time[3:])*0.25


'''
Failed but educational

def frequency_sort(items):

    def second_value(x):
        return x[1]

    result_list = list((i, items.count(i)) for i in items)
    result_list.sort(key=second_value, reverse=True)
    print(result_list)
    result = [x[0] for x in result_list]
    print(result)
    return result
'''

def sort_by_ext(files: list[str]) -> list[str]:

    files.sort(key=lambda x: (x[x.rfind("."):], x))
    for x in files[::-1]:
        if x[0] == "." and x.count(".") == 1:
            files.pop(files.index(x))
            files.insert(0, x)
    print(files)
    return files


def digits_multiplication(number: int) -> int:
    int_list = [int(x) for x in str(number) if x != "0"]
    result = int_list[0]
    if len(int_list) > 1:
        for x in int_list[1:]:
            result *= x
    print(result)
    return result

def is_acceptable_password2(password: str) -> bool:
    try:
        password[6]
        digit = any(x.isdigit() for x in password)
        letters = any(x.isalpha() for x in password)
        if digit and letters:
            return True
        return False
    except:
        return False

def is_acceptable_password4(password: str) -> bool:
    try:
        password[6]
        digit = any(x.isdigit() for x in password)
        letters = any(x.isalpha() for x in password)
        if (digit and letters) or len(password) > 9:
            return True
        return False
    except:
        return False


def is_acceptable_password5(password: str) -> bool:
    forbidden_word = "password"
    if len(password) > 6:
        if not forbidden_word in password \
                and not forbidden_word.capitalize() in password \
                and not forbidden_word.upper() in password:
            if len(password) > 9:
                return True
            else:
                if any(x.isalpha() for x in password) and any(x.isdigit() for x in password):
                    return True
    return False


def is_acceptable_password6(password: str) -> bool:
    forbidden_word = "password"
    if len(password) > 6:
        if not forbidden_word in password \
                and not forbidden_word.capitalize() in password \
                and not forbidden_word.upper() in password:
            letters = {i for i in password}
            print(letters)
            if len(password) > 9 and len(letters) >= 3:
                return True
            else:
                if any(x.isalpha() for x in password) and any(x.isdigit() for x in password) and len(letters) >= 3:
                    return True
    return False


def is_all_upper2(text: str) -> bool:
    text_list = text.split()
    if len(text_list) == 0:
        return False
    for x in text_list:
        if not x.isupper():
            return False
    return True


def is_ascending(items: Iterable[int]) -> bool:
    items_list = list(items)
    for index, x in enumerate(items_list, start=0):
        if index == len(items_list)-1:
            continue
        if x >= items_list[items_list.index(x) + 1]:
            return False
    return True

'''
MAIN
'''

assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False