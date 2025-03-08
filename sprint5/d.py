class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root: Node, root_1: Node) -> bool:
    def nodes_comparison(node1, node2):
        if node1.value != node2.value:
            return False
        left_flag = False
        if node1.left and node2.left:
            left_flag = nodes_comparison(node1.left, node2.left)
        elif not node1.left and not node2.left:
            left_flag = True
        else:
            return False

        right_flag = False
        if node1.right and node2.right:
            right_flag = nodes_comparison(node1.right, node2.right)
        elif not node1.right and not node2.right:
            right_flag = True
        else:
            return False

        return right_flag and left_flag

    return nodes_comparison(root, root_1)


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

    n = int(input())
    nodes_str = []
    for _ in range(n):
        nodes_str.append(input())
    nodes_1 = [None] * n
    for node_str in nodes_str[::-1]:
        n_str = node_str.split()
        left = nodes_1[int(n_str[2])] if n_str[2] != 'None' else None
        right = nodes_1[int(n_str[3])] if n_str[3] != 'None' else None
        nodes_1[int(n_str[0])] = Node(int(n_str[1]), left, right)

    print(solution(nodes[0], nodes_1[0]))


if __name__ == '__main__':
    test()
