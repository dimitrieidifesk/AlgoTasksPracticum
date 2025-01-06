"""
https://contest.yandex.ru/contest/24810/run-report/131066265/

-- ПРИНЦИП РАБОТЫ --
    Реализовано удаление узла из бинарного дерева поиска по ключу.
    Получив на вход ключ для удаления узла, мы ищем его в бинарном дереве, проходя по левой или правой ветке в зависимости от значения текущего узла.
    Когда узел для удаления найден, проверяем можем ли мы удалить его просто, заменив его на левый или правый дочерний узел. (Это возможно только если
    у узла есть только правый или только левый узел).
    Если нет, мы находим узел с наименьшим значением в правой дочерней ветке и заменяем им удаляемый узел.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
    Замена удаляемого узла узлом с наименьшим значением из дочерней правой ветки гарантирует, что принцип построения бинарного дерева не будет нарушен.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    h = высота дерева
    Поиск узла для удаления - O(h)
    Удаление узла в худшем случае - O(h)
    Общая временная сложность: O(h) + O(h) = O(2*h), то есть O(h)
    В не сбалансированном дереве сложность может доходить до O(N), N - кол-во узлов

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Пространственная сложность алгоритма зависит только от стека рекурсивных вызовов. В худшем случае это O(h), где h - высота дерева.
"""

from typing import Optional


class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def remove(root, key) -> Optional[Node]:
    if root is None:
        return root

    if key < root.value:
        root.left = remove(root.left, key)
    elif key > root.value:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        current = root.right
        while current.left is not None:
            current = current.left
        root.value = current.value
        root.right = remove(root.right, current.value)

    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8


if __name__ == '__main__':
    test()
