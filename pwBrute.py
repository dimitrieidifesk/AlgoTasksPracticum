import multiprocessing
import string
from hashlib import md5

symbols = list(string.ascii_lowercase) + list(string.digits)

targets = ['3bd0a32f99a0185c8a8f4af9ccff90ae', '8bad66e16b191a1f779f4c9f9f0955ea', '6467b3d4f0176029b582280342c83d33']


def worker(start, end):
    count = len(symbols)
    for index in range(start, end):
        combin = []
        temp_index = index
        for _ in range(6):
            combin.append(symbols[temp_index % count])
            temp_index //= count
        passwd = ''.join(combin)
        password_hash = md5(passwd.encode()).hexdigest()
        if password_hash in targets:
            print(f"Found {passwd} for {password_hash}")
        # print(passwd, password_hash)


if __name__ == '__main__':
    workers_count = 20
    processes = []
    n = len(symbols)
    N = n ** 6
    step = N // workers_count
    for i in range(workers_count):
        start = i * step
        end = (i + 1) * step
        print(start, end)
        p = multiprocessing.Process(target=worker, args=(start, end))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
