"""
https://contest.yandex.ru/contest/24810/run-report/131059377/

-- ПРИНЦИП РАБОТЫ --
    Реализован алгоритм пирамидальной сортировки.
    Описание работы алгоритма:
    1. Создание кучи. Добавляем массив по одному элементу, выполняя просеивание вверх для каждого нового элемента, что бы он занял нужную позицию в куче.
    2. До тех пор, пока куча не пуста, забираем корневой элемент из кучи, выполняя каждый раз просеивание вниз.
    Просеивание вверх и вниз выполняется рекурсивной заменой родительского с дочерним элементов, начиная с просеиваемого, до тех пор,
    пока все элементы не займут свои правильные позиции в куче, определяемые на основе сравнения параметров участников: кол-во решенных задач, штраф, логин.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
    Просеивание после каждой итерации извлечения корневого элемента гарантирует, что на следующей итерации в корне кучи окажется лидирующий участник из оставшихся.
    После извлечения всех элементов функцией pop_max мы получим отсортированный массив участников.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    Создание массива с объектами участников - O(N)
    Создание массива heap - O(1)
    Вставка в кучу 1 элемента - O(logN)
    Удаление из кучи 1 элемента - O(logN)
    Вывод отсортированного массива по одному - O(N)
    Общая временная сложность: O(N) + O(1) + N*O(logN) + N*O(logN) + O(N) = O(N*logN)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Массив members - O(N)
    Массив heap - O(2N+1)
    Отсортированный массив - O(N)
    Общая пространственная сложность: O(N) + O(2N+1) + O(N) = O(N)
"""

class Member:
    def __init__(self, login: str, tasks: int, fine: int):
        self.login = login
        self.tasks = int(tasks)
        self.fine = int(fine)

    def __str__(self):
        return f"{self.login}"


def members_compare(member_1: Member, member_2: Member):
    if member_1.tasks == member_2.tasks:
        if member_1.fine == member_2.fine:
            return member_1 if member_1.login < member_2.login else member_2
        else:
            return member_1 if member_1.fine < member_2.fine else member_2
    else:
        return member_1 if member_1.tasks > member_2.tasks else member_2


def sift_up(heap, index):
    if index == 1:
        return

    parent_index = index // 2
    if members_compare(heap[index], heap[parent_index]) == heap[index]:
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        sift_up(heap, parent_index)


def heap_add(heap, key):
    heap.append(key)
    index = len(heap) - 1
    sift_up(heap, index)


def sift_down(heap, index):
    heap_max_index = len(heap) - 1
    left = index * 2
    right = index * 2 + 1

    if left > heap_max_index:
        return

    if right <= heap_max_index and members_compare(heap[right], heap[left]) == heap[right]:
        index_largest = right
    else:
        index_largest = left

    if members_compare(heap[index_largest], heap[index]) == heap[index_largest]:
        heap[index_largest], heap[index] = heap[index], heap[index_largest]
        sift_down(heap, index_largest)


def pop_max(heap):
    result = heap[1]
    heap[1] = heap[len(heap) - 1]
    heap.pop()
    sift_down(heap, 1)
    return result


def heapsort(array):
    heap = [None]

    for item in array:
        heap_add(heap, item)

    sorted_array = []
    while len(heap) > 1:
        max_val = pop_max(heap)
        sorted_array.append(max_val)

    return sorted_array


members = list()

n = int(input())
for _ in range(n):
    members.append(Member(*input().split()))

for m in heapsort(members):
    print(m)
