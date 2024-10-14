def get_substring(s, t):
    last_index = 0
    len_string = len(s)

    for char in t:
        if len_string == last_index:
            return True
        if char == s[last_index]:
            last_index += 1
    return len_string == last_index


s = input()
t = input()
print(get_substring(s, t))
