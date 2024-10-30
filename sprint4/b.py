def get_longest_segment(rounds):
    rounds = [-1 if x == 0 else 1 for x in rounds]

    prefix_sum = {0: -1}
    current_sum = 0
    longest = 0

    for i, value in enumerate(rounds):
        current_sum += value

        if current_sum in prefix_sum:
            length = i - prefix_sum[current_sum]
            longest = max(longest, length)
        else:
            prefix_sum[current_sum] = i

    return longest

n = int(input())
rounds = list(map(int, input().split()))

print(get_longest_segment(rounds))
