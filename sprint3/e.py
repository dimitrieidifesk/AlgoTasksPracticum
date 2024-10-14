def get_homes_count(k, costs):
    costs.sort()
    count = 0
    for home in costs:
        if k >= home:
            count += 1
            k -= home
        if k <= 0:
            break
    return count


n, k = list(map(int, input().split()))
costs = list(map(int, input().split()))
print(get_homes_count(k, costs))
