class MaxItemsStack:
    def __init__(self):
        self.items = []
    
    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        return self.items.pop()
    
    def pick(self):
        return self.items[-1]

class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_items_stack = MaxItemsStack()

    def pop(self):
        if len(self.items) > 0:
            if self.max_items_stack.pick() == len(self.items) - 1:
                self.max_items_stack.pop()
            return self.items.pop()
        print('error')

    def get_max(self):
        return self.items[self.max_items_stack.pick()] if len(self.items) > 0 else None

    def push(self, x):
        if len(self.items) > 0:
            self.items.append(x)
            if x > self.items[self.max_items_stack.pick()]:
                self.max_items_stack.push(len(self.items) - 1)
        else:
            self.items.append(x)
            self.max_items_stack.push(0)

    def top(self):
        if len(self.items) > 0:
            print(self.items[-1])
            return
        print('error')
        

stack = StackMaxEffective()


def proccess_command(command: str):
    if 'push' in command:
        x = int(command.strip().split('push')[1])
        stack.push(x)
    elif command == 'pop':
        stack.pop()
    elif command == 'get_max':
        print(stack.get_max())
    elif command == 'top':
        stack.top()

n = int(input())
for _ in range(n):
    proccess_command(input())


