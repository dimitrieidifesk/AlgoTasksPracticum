def get_commits_count(n: int):
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


n, k = map(int, input().split())
print(get_commits_count(n) % 10**k)