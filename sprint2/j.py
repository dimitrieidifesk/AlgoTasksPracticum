
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class Queue:
    def __init__(self, head: Node = None):
        self.queue_size = 0
        self.head = head

    def put(self, x):
        self.queue_size += 1
        if not self.head:
            self.head = Node(value=x)
            return
        self.head = Node(value=x, next_item=self.head)

    def get(self):
        if self.queue_size == 0:
            return 'error'
        self.queue_size -= 1
        last_node = self.head
        if last_node.next_item:
            while last_node.next_item.next_item:
                last_node = last_node.next_item
            value = last_node.next_item.value
            last_node.next_item = None
        else:
            value = self.head.value
            self.head = None
        return value

    def size(self):
        return self.queue_size


def proccess_command(cmd):
    if 'put' in cmd:
        x = int(cmd.strip().split('put')[1])
        queue.put(x)
    elif cmd == 'get':
        print(queue.get())
    elif cmd == 'size':
        print(queue.size())


n = int(input())
queue = Queue()
for _ in range(n):
    proccess_command(input().strip())

