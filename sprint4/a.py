n = int(input())
hash = {}
for _ in range(n):
    v = input()
    if hash.get(v):
        hash[v] += 1
    else:
        hash[v] = 1
print('\n'.join(list(hash.keys())))


