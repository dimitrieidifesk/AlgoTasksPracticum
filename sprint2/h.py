class Brackets:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        self.items.pop()
    
    def pick(self):
        return self.items[-1] if len(self.items) > 0 else None


def is_correct_bracket_seq(string: str):
    brackets = Brackets()
    if string == '':
        return True
    bracket_types = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for s in string:
        if s in ['(', '[', '{']:
            brackets.push(s)
        else:
            last = brackets.pick()
            if not last:
                return False
            if bracket_types[last] != s:
                return False
            brackets.pop()
    if brackets.pick():
        return False
    return True

string = input().strip()
print(is_correct_bracket_seq(string))
