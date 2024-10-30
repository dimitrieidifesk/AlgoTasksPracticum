"""
https://contest.yandex.ru/contest/24414/run-report/122736374/

-- ПРИНЦИП РАБОТЫ --
Реализована хеш-таблица с использованием метода открытой адресации с квадратичным пробированием при обработке коллизий.
Каждый ключ хешируется в методе _get_hash как отстаток от деления на длину массива.
Поиск значения происходит либо по полученному хешу, который и является индексом, либо по правилу обработки коллизий.
Обработка коллизий: Используется self.size // 100 попыток найти нужную ячейку. Следующая ячейка для проверки выбирается по
правилу открытой адресации, используя квадратичное пробирование.Все коллизии записываются в последующие баскеты,
индексы которых расчитываются в методе _conflict_resolution.
Удаление происходит поиском баскета и заменой параметра is_deleted на True (А вообще можно было и на None баскет поменять).

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Хеш-таблица эффективно работает, т.к. правильно выбрана длина массива = 300007, т.к. это простое число и
оно в 3 раза больше, чем максимальное кол-во элементов в хеш-таблице.
Это позволяет уменьшить время на разрешение коллизий и снизить вероятность их появления.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
В среднем все операции выполняются за O(1), благодаря правильному выбору длины массива, правильной хеш-функции и правилу
обработки коллизий.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Для уменьшения вероятности появления коллизий и ускорения работы программы длина массива была выбрана как
наименьшее простое число, большее 3 * 10 ** 5   (300007)
Следовательно пространственная сложность = O(3*N) = O(N)
"""

from typing import List


class Basket:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.is_deleted = False


class HashTable:
    def __init__(self):
        self.size = 300007
        self.table: List[Basket] = [None] * self.size
        self.deleted_count = 0

    def _get_hash(self, key: int):
        return key % self.size

    def _get_index(self, key: int):
        index = self._get_hash(key)

        if self.table[index] is not None and not self.table[index].is_deleted:
            if self.table[index].key == key:
                return index
        for i in range(self.size // 100):
            new_index = self._conflict_resolution(key, i)
            if self.table[new_index] is None:
                return None
            if not self.table[new_index].is_deleted and self.table[new_index].key == key:
                return new_index

    def _conflict_resolution(self, key: int, i: int = 0):
        c1 = 1
        c2 = 3
        new_index = (self._get_hash(key) + c1 * i + c2 * i * i) % self.size
        return new_index

    def get(self, key: int) -> int:
        index = self._get_index(key)
        if index is None:
            return None
        return self.table[index].value

    def put(self, key: int, value: int):
        index = self._get_hash(key)
        if self.table[index] is not None and not self.table[index].is_deleted:
            if self.table[index].key == key:
                self.table[index].value = value
            else:
                for i in range(self.size // 100):
                    new_index = self._conflict_resolution(key, i)
                    if self.table[new_index] is None or self.table[new_index].is_deleted:
                        self.table[new_index] = Basket(key, value)
                        return
                    if self.table[new_index].key == key:
                        self.table[new_index].value = value
                        return
        else:
            self.table[index] = Basket(key, value)

    def delete(self, key: int) -> int:
        index = self._get_index(key)
        if index is None:
            return None
        self.table[index].is_deleted = True
        return self.table[index].value


storage = HashTable()


def process_command(cmd: str):
    cmd_parts = cmd.strip().split()
    operation = cmd_parts[0]

    if operation == 'get':
        key = int(cmd_parts[1])
        print(storage.get(key))
    elif operation == 'put':
        key = int(cmd_parts[1])
        value = int(cmd_parts[2])
        storage.put(key, value)
    elif operation == 'delete':
        key = int(cmd_parts[1])
        print(storage.delete(key))


n = int(input())
for _ in range(n):
    process_command(input().strip())
