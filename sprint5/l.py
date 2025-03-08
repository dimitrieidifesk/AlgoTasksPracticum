class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def build_tree(node_value):
    print(node_value)
    if node_value <= 0:
        return
    if node_value >= n:
        return
    node = Node(node_value, left=build_tree(node_value-1), right=build_tree(node_value+1))
    return node



def main(n):
    cnt = 0
    for i in range(1, n):
        tree = build_tree(i)
        if tree:
            cnt += 1
    return cnt


n = int(input())
print(main(n))
