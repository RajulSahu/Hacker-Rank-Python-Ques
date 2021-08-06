from collections import Counter

N = int(input())
word_list = []

for _ in range(N):
    word_list.append(input())


count = Counter(word_list)
print(len(count))
print(*count.values())
    
