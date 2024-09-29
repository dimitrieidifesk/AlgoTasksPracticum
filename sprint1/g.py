from typing import Tuple


def get_sum(bin1, bin2):
    if len(bin1) < len(bin2):
        bin1, bin2 = bin2, bin1

    result = []
    carry = 0

    i = len(bin1) - 1
    j = len(bin2) - 1

    while i >= 0 or j >= 0 or carry:
        bit1 = int(bin1[i]) if i >= 0 else 0
        bit2 = int(bin2[j]) if j >= 0 else 0

        total = bit1 + bit2 + carry

        result.append(str(total % 2))
        carry = total // 2

        i -= 1
        j -= 1

    return ''.join(reversed(result))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
