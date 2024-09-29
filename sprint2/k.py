def get_commits_count(n: int):
    if n == 0 or n == 1:
        return 1
    return get_commits_count(n-1) + get_commits_count(n-2)
    

n = int(input())
print(get_commits_count(n))
