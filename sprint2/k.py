# 4
# 1 2 0 0
# 34
# 1 2 3 4

def get_sum(x_str, k):
    result = []
    carry = 0
    x = int(''.join(x_str))
    for _ in range(1, max(len(x_str), len(str(k))) + 1):
        carry_ = 0
        cur_x = x % 10
        cur_k = k % 10
        if cur_x + cur_k >= 10:
            carry_ = 1
            cur_suma = (cur_x + cur_k) % 10
        else:
            cur_suma = cur_x + cur_k
        if cur_suma + carry >= 10:
            carry_ = 1
        result.append((cur_suma + carry) % 10)
        x //= 10
        k //= 10
        carry = carry_
    if carry:
        result.append(carry)
    return result[::-1]


count_x = int(input().strip())
x = list(map(str, input().strip().split()))
k = int(input().strip())

print(' '.join(map(str, get_sum(x, k))))
