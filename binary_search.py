def binary_search(arr, target):
    left_idx, right_idx = 0, len(arr)
    while left_idx < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if arr[mid_idx] == target:
            return True
        elif arr[mid_idx] < target:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx
    return False


# complexity: O(logN)   

def solve_equation(value):
    left, right = 1, value
    for _ in range(100):
        mid = (left + right) / 2
        expr_result = mid * log2(mid)
        if expr_result < value:
            left = mid
        else:
            right = mid
    return mid

# non-standart application of the binary search

def find_01(s):
    for i in range(len(s) - 1):
        if s[i] == '0' and s[i + 1] == '1':
            return i

s = "000101"
print(find_01(s))

# Time O(Log n) Memory O(1)

# ========= EXAMPLE WITH ERROR ==========

def max_lower_or_equal(sorted_arr, value):
    # Сначала проверим, существует ли искомый элемент
    if not sorted_arr or sorted_arr[0] > value:
        return -1

    left_idx, righr_idx = 0, len(sorted_arr)
    while left_idx + 1 < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if sorted_arr[mid_idx] <= value:
            left_idx = mid_idx
        else:
            right_idx = mid_idx
        return left_idx


def _max_lower_or_equal(sorted_arr, value):
    # Сначала проверим, существует ли искомый элемент
    if not sorted_arr or sorted_arr[0] > value:
        return -1

    left_idx, right_idx = 0, len(sorted_arr)
    while left_idx < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if sorted_arr[mid_idx] <= value:
            left_idx = mid_idx
        else:
            right_idx = mid_idx
    return left_idx

# Error - may enter into an infinite loop