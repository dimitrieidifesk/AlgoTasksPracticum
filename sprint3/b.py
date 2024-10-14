def letter_combinations(digits):
    if not digits:
        return []

    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = []

    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            result.append(combination)
        else:
            digit = next_digits[0]
            for letter in phone_map[digit]:
                backtrack(combination + letter, next_digits[1:])

    backtrack("", digits)

    return sorted(result)


input_digits = input().strip()
combinations = letter_combinations(input_digits)

print(" ".join(combinations))
