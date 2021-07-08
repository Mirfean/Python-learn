from typing import Iterable


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
        if forbidden_word not in password \
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
        if index == len(items_list) - 1:
            continue
        if x >= items_list[items_list.index(x) + 1]:
            return False
    return True

def Brackets(expression):
    open_brackets = ("(", "{", "[")
    close_brackets = (")", "}", "]")
    brackets_str = ""

    for x in expression:
        if x in open_brackets:
            brackets_str += x
        elif x in close_brackets:
            if brackets_str != "":
                if brackets_str[-1] == open_brackets[close_brackets.index(x)]:
                    brackets_str = brackets_str[:-1]
                    continue
            return False
    if brackets_str == "":
        return True
    return False