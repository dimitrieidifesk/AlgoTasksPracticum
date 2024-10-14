"""
https://contest.yandex.ru/contest/23815/run-report/120720615/

-- ПРИНЦИП РАБОТЫ --
Реализован эффективный алгоритм быстрой сортировки.
Принцип работы заключается в рекурсивной обработке интервалов массива, разделенных рандомного выбранным опорным элементом.
В алгоритме используется метод двух указателей для определения границ интервала, внутри которого выбирается опорный элемент
и происходит сортировка. С каждым шагом рекурсии массив разбивается на две части и частично сортируется. Так происходит до тех пор,
пока указатель left не столкнется с указателем right.
Функция in_place обеспечивает эффективное использование памяти. Сортировка от left до right в функции in_place происходит
перестановками.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Когда указатель left оказывается не меньше right, рекурсия останавливается.
При этом массив считается отсортированным, так как он состоит из одного или нуля элементов.
Таким образом весь массив будет отсортирован, когда каждый рекурсивный вызов дойдет до этого элемента.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
В худшем случае время работы алгоритма составит O(n^2), но такой результат возможен только в том случае, когда опорный
элемент всегда будет первым элементов интервала. В среднем алгоритма составит O(n*log(n)).
P.S. Не учитываем циклы, которые используются для форматирования вывода и ввода исходных данных.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Все операции происходят только с исходным массивом, благодаря функции in_place.
Пространственная сложность O(n).
"""

import random
from typing import List


def compare_results(party_1, party_2) -> int:
    if party_1[1] == party_2[1]:
        if party_1[2] == party_2[2]:
            return 1 if party_1[0] < party_2[0] else 2
        return 1 if party_1[2] < party_2[2] else 2
    return 1 if party_1[1] > party_2[1] else 2


def in_place(array, left, right) -> int:
    pivot = random.randint(left, right)
    pivot_val = array[pivot]
    array[pivot], array[right] = array[right], array[pivot]
    left_store = left

    for i in range(left, right):
        if compare_results(array[i], pivot_val) == 1:
            array[i], array[left_store] = array[left_store], array[i]
            left_store += 1

    array[left_store], array[right] = array[right], array[left_store]
    return left_store


def quicksort(array, left=0, right=None) -> List:
    if not right:
        right = len(array) - 1
    if left < right:
        pivot = in_place(array, left, right)
        quicksort(array, left, pivot - 1)
        quicksort(array, pivot + 1, right)
    return array


n = int(input())
participants = []
for _ in range(n):
    login, tasks, fines = input().split()
    participants.append((login, int(tasks), int(fines)))

print('\n'.join([x[0] for x in quicksort(participants)]))
