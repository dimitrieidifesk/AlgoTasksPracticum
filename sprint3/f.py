def get_triangle(n, arr):
    max_per = 0
    arr.sort()
    arr = arr[::-1]
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                if a == b or b == c or a == c:
                    continue
                if arr[a] + arr[b] <= arr[c]:
                    continue
                if arr[c] + arr[b] <= arr[a]:
                    continue
                if arr[c] + arr[a] <= arr[b]:
                    continue
                max_per = max(arr[a] + arr[b] + arr[c], max_per)
                return max_per
    return max_per


n = int(input())
arr = list(map(int, input().split()))
print(get_triangle(n, arr))
