from collections import Counter

num_of_shoes = int(input())
shoes = list(map(int, input().split()))
k = int(input())

total_money = 0

shoe_count = dict(Counter(shoes))

for _ in range(k):
    order = list(map(int, input().split()))
    required_num = order[0]
    money = order[1]
    if required_num in shoe_count and shoe_count[required_num] > 0:
        total_money += money
        shoe_count[required_num] -= 1

print(total_money)
        


