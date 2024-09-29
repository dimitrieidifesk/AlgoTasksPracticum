"""
https://contest.yandex.ru/contest/22781/run-report/119218153/

-- ПРИНЦИП РАБОТЫ --
В процессе итерации по символам выражения я добавляю числа в стек в том порядке, в котором они стоят в выражении. 
Когда встречается знак операции, я достаю из стека два последних операнда и выполняю нужную операцию. 
Результат кладу обратно в стек и буду использовать его в одной из следующих операций.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Последний оставшийся элемент в стеке будет результатом выполнения всех операций. 
Порядок выполнения операций и использования операндов сохраняется благодаря структуре стека, который использует принцип LIFO.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Проход по выражению осуществляется один раз и требует времени O(n). Все операции стека выполяются за O(1).  
Значит временная сложность зависит только от длины выражения и состовляет O(n).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Стек хранит операнды выражения и в худшем случае нам придется сохранить N операндов, где N - длина выражения. 
Поэтому для хранения стека нам понадобится O(n) памяти.

"""
from typing import List

class Stack:
    def __init__(self):
        self.items = list()

    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        return self.items.pop()
    

def get_result(expression: List[str]) -> int:
    boofer = Stack()
    operations = ['+', '-', '*', '/']
    for char in expression:
        if char in operations:
            num_1 = boofer.pop()
            num_2 = boofer.pop()
            if char == '+':
                boofer.push(num_1 + num_2)
            elif char == '-':
                boofer.push(num_2 - num_1)
            elif char == '*':
                boofer.push(num_2 * num_1)
            elif char == '/':
                boofer.push(num_2 // num_1)
        else:
            boofer.push(int(char))
    return boofer.pop()

expression = input().split()
print(get_result(expression))

