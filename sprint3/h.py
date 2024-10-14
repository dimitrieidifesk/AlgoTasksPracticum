def largest_number(arr):
    arr.sort(key=lambda x: x * 3, reverse=True)

    largest_num = ''.join(arr)

    return largest_num if largest_num[0] != '0' else '0'


n = int(input())
numbers = list(map(str, input().split()))

print(largest_number(numbers))
