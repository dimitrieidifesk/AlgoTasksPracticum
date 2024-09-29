def factorization(num):
    result = []
    while num % 2 == 0:
        result.append(2)
        num //= 2
    for i in range(3, int(num**0.5) + 1, 2):
        while num % i == 0:
            result.append(i)
            num //= i
    if num > 2:
        result.append(num)

    return sorted(result)


num = int(input().strip())
print(' '.join(map(str, factorization(num))))