def reverse_word_order(string):
    return join(reverse(split(string)))

def split(string):
    result = []
    index = 0
    while index < len(string):
        while index < len(string):
            while index < len(string) and string[index].isspace():
                index +=1
            if index == len(string):
                return result
            result.append('')
            while index < len(string) and not string[index].isspace():
                result[-1] += string[index]
                index += 1
        return result

def reverse(elements):
    for left in range(len(elements) // 2):
        right = len(elements) - left - 1
        elements[left], elements[right] = elements[right], elements[left]
    return elements

def join(words):
    if not words:
        return ''
    result = words[0]
    for index in range(1, len(words)):
        result += ' ' + words[index]
    return result
