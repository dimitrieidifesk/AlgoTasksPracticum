class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()

    def push(self, x):
        self.items.append(x)


results = []
result = ''


def get_all_bracket_sequences(n: int, prefix: str):
    global result
    if n == 0:
        result += prefix
    else:
        get_all_bracket_sequences(n - 1, prefix + '(')
        if result:
            results.append(result)
        result = ''
        get_all_bracket_sequences(n - 1, prefix + ')')
        if result:
            results.append(result)
        result = ''
    return results


def check_correct_sequence(seq: str):
    stack = Stack()
    for c in seq:
        if c == '(':
            stack.push(c)
        else:
            i = stack.pop()
            if not i:
                return False
    if not stack.pop():
        return True


def get_correct_bracket_sequences(n):
    arr = get_all_bracket_sequences(2 * n, '')
    corrects = []
    for seq in arr:
        if check_correct_sequence(seq):
            corrects.append(seq)
    return '\n'.join(corrects)


n = int(input())
print(get_correct_bracket_sequences(n))
