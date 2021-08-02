k = int(input())
rooms_arr = list(map(int, input().split()))

rooms_set = set(rooms_arr)

sum_rooms_arr = sum(rooms_arr)
sum_rooms_set = sum(rooms_set)

captain_room = ((sum_rooms_set * k) - sum_rooms_arr) // (k - 1)

print(captain_room)