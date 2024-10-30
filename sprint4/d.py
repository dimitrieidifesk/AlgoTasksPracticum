def get_hash(a: int, m: int, s: str):
    suma = 0
    for i in range(len(s)):
        suma += (ord(s[i]) * (a ** i))

    return suma % m


a = int(input())
m = int(input())
s = input()

print(get_hash(a, m, s))
