def get_len_substring(s: str):
    max_len = 0
    for i in range(len(s)):
        cache = []
        for j in range(i, len(s)):
            if s[j] not in cache:
                cache.append(s[j])
            else:
                break
        max_len = max(max_len, len(cache))
    return max_len


s = input()
print(get_len_substring(s))
