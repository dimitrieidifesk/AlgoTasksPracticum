
class StackMax:
    def __init__(self):
        self.items = []

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        print('error')

    def get_max(self):
        return max(self.items) if len(self.items) > 0 else None

    def push(self, x):
        self.items.append(x)

stack = StackMax()


def proccess_command(command: str):
    if 'push' in command:
        x = int(command.strip().split('push')[1])
        stack.push(x)
    elif command == 'pop':
        stack.pop()
    elif command == 'get_max':
        print(stack.get_max())

n = int(input())
for _ in range(n):
    proccess_command(input())


