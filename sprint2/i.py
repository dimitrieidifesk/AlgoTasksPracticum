
class Queue:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.items = [None] * max_size
        self.queue_size = 0
        self.head = 0
        self.tail = 0

    def push(self, x):
        if self.queue_size == self.max_size:
            raise ValueError('Переполнение')
        self.items[self.tail] = x
        self.tail = (self.tail + 1) % self.max_size
        self.queue_size += 1

    def pop(self):
        if self.queue_size == 0:
            return
        head = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.queue_size -= 1
        return head
    
    def peek(self):
        if self.queue_size == 0:
            return
        return self.items[self.head]
    
    def size(self):
        return self.queue_size

def proccess_command(cmd):
    if 'push' in cmd:
        x = int(cmd.strip().split('push')[1])
        try:
            queue.push(x)
        except ValueError:
            print('error')
    elif cmd == 'peek':
        print(queue.peek())
    elif cmd == 'pop':
        print(queue.pop())
    elif cmd == 'size':
        print(queue.size())


n = int(input())
max_size = int(input())
queue = Queue(max_size)
for _ in range(n):
    proccess_command(input().strip())

