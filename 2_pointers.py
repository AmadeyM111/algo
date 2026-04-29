def max_consecutive_elements(input_str):
    result, cur_letter_idx = 0, 0
    while cur_letter_idx < len(input_str):
        next_letter_idx = cur_letter_idx
        while next_letter_idx < len(input_str) \
        and input_str[next_letter_idx] == input_str[cur_letter_idx]:
            next_letter_idx += 1
        result = max(result, next_letter_idx - cur_letter_idx)
        cur_letter_idx = next_letter_idx
    return result

def subarray_sum (non_negative_arr, target):
    right, current_sum = 0,0
    for left in range(len(non_negative_arr)):
        # пересчитываем сумму
        if left > 0:
            current_sum -= non_negative_arr[left - 1]

        # при необходимости двигаем правую границу
        while right < len(non_negative_arr) and current_sum < target:
            current_sum += non_negative_arr[right]
            right += 1

        if current_sum == target:
            return True
    
    return False

def subarray_sum_other(arr, target: int):
    prefix_sums = {0}
    cur_sum = 0

    for x in arr:
        cur_sum += x

        if cur_sum in prefix_sums:
            return True

        prefix_sums.add(cur_sum)

    return False


def get_next_dif_letter_idx(input_str, cur_letter_idx):
    next_letter_idx = cur_letter_idx
    while next_letter_idx < len(input_str) \
    and input_str[next_letter_idx] == input_str[cur_letter_idx]: #??
        next_letter_idx += 1
    return next_letter_idx

def max_consecutive_elemets_alt(input_str):
    result, cur_letter_idx = 0, 0
    while cur_letter_idx < len(input_str):
        next_letter_idx = get_next_dif_letter_idx(input_str, cur_letter_idx)
        result = max(result, next_letter_idx - cur_letter_idx)
        cur_letter_idx += next_letter_idx
    return result

# двигаемся по блокам одинаковых символов