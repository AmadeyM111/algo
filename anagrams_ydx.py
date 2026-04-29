def areAnagrams(a, b):
    ca = Counter(a)
    cb = Counter(b)
    diff = ca - cb
    return len(diff) == 0 and len(a) == len(b)
