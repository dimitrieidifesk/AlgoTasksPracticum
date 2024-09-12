from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    if len(temperatures) == 1:
        return 1
    result = 0
    for day in range(len(temperatures)):
        if day == len(temperatures) - 1:
            if temperatures[day] > temperatures[day - 1]:
                result += 1
        elif day == 0:
            if temperatures[day] > temperatures[day + 1]:
                result += 1
        elif temperatures[day] > temperatures[day - 1] and temperatures[day] > temperatures[day + 1]:
            result += 1
    return result


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
