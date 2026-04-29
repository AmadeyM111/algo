def areAnagrams_counter(a, b):
    ca = Counter(a)
    cb = Counter(b)
    diff = ca - cb
    return len(diff) == 0 and len(a) == len(b)

def dictFromString(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    return d

def areAnagrams_dict(a, b):
    return dictFromString(a) == dictFromString(b)
