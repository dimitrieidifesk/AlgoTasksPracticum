class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root: Node) -> int:
    branch_lengths = []

    def get_branch_length(node, cur_len):
        cur_len += 1
        if node.left:
            get_branch_length(node.left, cur_len)
        else:
            branch_lengths.append(cur_len)
        if node.right:
            get_branch_length(node.right, cur_len)
        else:
            branch_lengths.append(cur_len)

    get_branch_length(root, 1)
    for i in branch_lengths:
        for j in branch_lengths:
            if abs(i - j) > 1:
                return False
    return True


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
