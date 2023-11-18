import math

given_str = "101"

str_len_index = len(given_str) - 1


def fun_left(start, end):
    edit_count = 0

    while start <= end:

        if not (given_str[start] == given_str[str_len_index - start]):
            edit_count = edit_count + 1
        start += 1
    return edit_count


def fun_right(start, end):
    edit_count = 0

    while end >= start:

        if not (given_str[end] == given_str[str_len_index - end]):
            edit_count = edit_count + 1
        end -= 1

    return edit_count


if len(given_str) % 2 == 0:
    mid = len(given_str) / 2
    left_val = fun_left(0, mid - 1)
    right_val = fun_right(mid, str_len_index)
    print(min(left_val, right_val))


else:
    mid = math.floor(len(given_str) / 2)
    left_val = fun_left(0, mid - 1)
    right_val = fun_right(mid + 1, str_len_index)
    print(min(left_val, right_val))
