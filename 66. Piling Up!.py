def checker(side_lengths):
    left = 0
    right = len(side_lengths) - 1
    base_length = sum(side_lengths)
    while left <= right:
        if side_lengths[right] <= side_lengths[left] <= base_length:
            base_length = side_lengths[left]
            left += 1
        elif side_lengths[left] <= side_lengths[right] <= base_length:
            base_length = side_lengths[right]
            right -= 1
        else:
            return "No"
    return "Yes"


N = int(input())
for _ in range(N):
    n = int(input())
    side_lengths = list(map(int, input().split()))
    print(checker(side_lengths))
