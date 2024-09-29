"""
https://contest.yandex.ru/contest/22781/run-report/119203984/

-- ПРИНЦИП РАБОТЫ --
Реализована очередь на деке с возможностью добавления и извлечения элементов из начала и конца очереди.
При вставке элемента в конец очереди я записываю новый элемент в ячейку с индексом self.tail, поскольку это индекс крайней не занятой ячейки с конца очереди.
При вставке элемента в начало очереди я записываю новый элемент в ячейку self.head - 1, что бы не сдвигать все элементы массива. При этом, если массив пуст,
мы можем записать новый элемент в ячейку self.head и сместить self.tail на 1 ячейку вперед.
При извлечении элемента из начала очереди я возвращаю элемент под индексом self.head и смещаю этот индекс головного элемента 
на новое начало очереди, обнуляя извлеченный элемент.
При извлечении элемента из конца очереди я возвращаю самый последний элемент под индексом self.tail - 1, обнуляя его ячейку и 
сдвигая индекс крайней пустой ячейки на освободившееся место.

Что бы не выскакивать за пределы массива, при обновлении индексов self.tail и self.head, я беру остаток от деления нового индекса на self.max_size.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Дек хранит индексы "головного" и "хвостового" элементов в кольцевом буфере, что позволяет вставлять и извлекать элементы из начала и конца очереди за короткое время. 

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Благодаря использованию кольцевого буфера все операции выполняются за время O(1).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Дек хранит массив фиксированной длины - m, значит очередь будет потреблять O(n) памяти.
"""


class Queue:
    def __init__(self, max_size: int):
        self.size = 0
        self.max_size = max_size
        self.items = [None] * max_size
        self.head = 0
        self.tail = 0
    
    def push_back(self, value: int):
        if self.size == self.max_size:
            raise ValueError('error')
        self.size += 1
        self.items[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size

    def push_front(self, value: int):
        if self.size == self.max_size:
            raise ValueError('error')
        if self.size == 0:
            index = self.head
            self.tail = (self.tail + 1) % self.max_size
        else:
            index = self.head - 1 if self.head - 1 >= 0 else self.max_size - 1
            self.head = index
        self.items[index] = value
        self.size += 1

    def pop_front(self) -> int:
        if self.size == 0:
            raise ValueError('error')
        self.size -= 1
        value = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_size
        return value

    def pop_back(self) -> int:
        if self.size == 0:
            raise ValueError('error')
        self.size -= 1
        index = self.tail - 1 if self.tail - 1 >= 0 else self.max_size - 1
        value = self.items[index]
        self.items[index] = None
        self.tail = index
        return value

def proccess_command(cmd: str):
    if 'push_back' in cmd:
        x = int(cmd.strip().split('push_back')[1])
        queue.push_back(x)
    if 'push_front' in cmd:
        x = int(cmd.strip().split('push_front')[1])
        queue.push_front(x)
    elif cmd == 'pop_front':
        item = queue.pop_front()
        print(item)
    elif cmd == 'pop_back':
        item = queue.pop_back()
        print(item)

n = int(input())
m = int(input())
queue = Queue(max_size=m)

for _ in range(n):
    try:
        proccess_command(input().strip())
    except ValueError as ex:
        print(str(ex))
    