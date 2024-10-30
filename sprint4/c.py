def is_strings_equal(s: str, t: str):
    if len(s) != len(t):
        return 'NO'
    letters = {}
    for i in range(min(len(s), len(t))):
        if letters.get(s[i]):
            if letters[s[i]] != t[i]:
                return 'NO'
        else:
            if t[i] in list(letters.values()):
                return 'NO'
            letters[s[i]] = t[i]
    return 'YES'


s = input()
t = input()
print(is_strings_equal(s, t))
