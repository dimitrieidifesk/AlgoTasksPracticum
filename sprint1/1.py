# https://contest.yandex.ru/contest/22449/problems/?nc=AEHrPb2i
def solution(a: int, b: int, c: int) -> str:
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        return 'WIN'
    elif a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
        return 'WIN'
    return 'FAIL'


a, b, c = map(int, input().strip().split())
print(solution(a, b, c))
