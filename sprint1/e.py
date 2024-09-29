def get_longest_word(line: str) -> str:
    arr = line.strip().replace('\n', '').split()
    max_index = 0
    for i, word in enumerate(arr):
        if len(word) > len(arr[max_index]):
            max_index = i

    return arr[max_index]

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))