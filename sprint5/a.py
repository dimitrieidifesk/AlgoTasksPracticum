class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


max_val = 0


def solution(root: Node) -> int:
    global max_val
    max_val = max(max_val, root.value)
    if root.left:
        max_val = max(max_val, root.left.value)
        max_val = max(max_val, solution(root.left))
    if root.right:
        max_val = max(max_val, root.right.value)
        max_val = max(max_val, solution(root.right))
    return max_val


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
