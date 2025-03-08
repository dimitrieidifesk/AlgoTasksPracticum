class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root: Node) -> int:
    if root is None:
        return 0

    left_height = solution(root.left)
    right_height = solution(root.right)

    return max(left_height, right_height) + 1



def test():
    n = int(input())
    nodes_str = []
    for _ in range(n):
        nodes_str.append(input())
    nodes = [None] * n
    for node_str in nodes_str[::-1]:
        n_str = node_str.split()
        left = nodes[int(n_str[2])] if n_str[2] != 'None' else None
        right = nodes[int(n_str[3])] if n_str[3] != 'None' else None
        nodes[int(n_str[0])] = Node(int(n_str[1]), left, right)
    print(solution(nodes[0]))


if __name__ == '__main__':
    test()
