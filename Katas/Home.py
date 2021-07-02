from typing import Union

import copy


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
            safe_square = chr(ord(pawn[0]) - 1) + str(int(pawn[1]) + 1)
            safe_square2 = chr(ord(pawn[0]) + 1) + str(int(pawn[1]) + 1)
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
    return (int(time[0:2]) - 6) * 15 + int(time[3:]) * 0.25