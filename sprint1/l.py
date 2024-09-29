def get_extra_letter(str_1, str_2):
    letters_counts = {}
    for letter in str_1:
        if letters_counts.get(letter):
            letters_counts[letter] += 1
        else:
            letters_counts[letter] = 1
    for letter in str_2:
        if not letters_counts.get(letter):
            return letter
        letters_counts[letter] -= 1


str_1 = input().strip()
str_2 = input().strip()

print(get_extra_letter(str_1, str_2))
