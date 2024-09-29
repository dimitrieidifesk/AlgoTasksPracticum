def add_binary(bin1, bin2):
    result = []
    carry = 0

    max_len = max(len(bin1), len(bin2))

    for i in range(max_len):
        bit1 = int(bin1[-1 - i]) if i < len(bin1) else 0
        bit2 = int(bin2[-1 - i]) if i < len(bin2) else 0

        total = bit1 + bit2 + carry
        result.append(str(total % 2))
        carry = total // 2

    if carry:
        result.append('1')

    return ''.join(result[::-1])


bin1 = input().strip()
bin2 = input().strip()

print(add_binary(bin1, bin2))
