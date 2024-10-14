def sort_clothes(n, arr):
    pink = []
    yellow = []
    red = []

    for i in arr:
        if i == 0:
            pink.append(str(i))
        elif i == 1:
            yellow.append(str(i))
        elif i == 2:
            red.append(str(i))
    res = []
    res.extend(pink)
    res.extend(yellow)
    res.extend(red)

    return ' '.join(res)


n = int(input())
arr = list(map(int, input().split()))
print(sort_clothes(n, arr))
