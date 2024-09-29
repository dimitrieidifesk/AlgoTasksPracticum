def is_palindrome(line: str) -> bool:
    string = line.upper().replace(',', '').replace(' ', '').replace(':', '').replace('.', '').replace('-', '').replace(
        '!', '').replace('*', '').replace('@', '').replace('`', '').replace('(', '').replace(')', '').replace('>',
                                                                                                              '').replace(
        '_', '').replace("'", '')
    if string == string[::-1]:
        return True
    return False


print(is_palindrome(input().strip()))
