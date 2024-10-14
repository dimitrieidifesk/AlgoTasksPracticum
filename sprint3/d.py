def get_satisfied_childrens(children_cnt, greed_factors, cookies_cnt, cookies_sizes):
    satisfied_childrens_cnt = 0
    greed_factors.sort()
    cookies_sizes.sort()
    last_cookie = 0
    for greed in greed_factors:
        for i in range(last_cookie, len(cookies_sizes)):
            last_cookie += 1
            if cookies_sizes[i] >= greed:
                satisfied_childrens_cnt += 1
                break
    return satisfied_childrens_cnt


children_cnt = int(input())
greed_factors = list(map(int, input().split()))
cookies_cnt = int(input())
cookies_sizes = list(map(int, input().split()))

print(get_satisfied_childrens(children_cnt, greed_factors, cookies_cnt, cookies_sizes))
