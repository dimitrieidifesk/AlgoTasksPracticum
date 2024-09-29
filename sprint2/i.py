
def is_4degree(num):
    for i in range(num):
        if i * i > num:
            return False
        if 4 ** i == num:
            return True
    return False

num = input().strip()

print(is_4degree(int(num)))