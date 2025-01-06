
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root) -> int:
    def forward(node: Node, cur_sum):
        if not node:
            return 0
        cur_sum = cur_sum * 10 + node.value
        if not node.left and not node.right:
            return cur_sum
        return forward(node.left, cur_sum) + forward(node.right, cur_sum)
    return forward(root, 0)


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)
    print(solution(node5))
    # assert solution(node5) == 275


if __name__ == '__main__':
    test()