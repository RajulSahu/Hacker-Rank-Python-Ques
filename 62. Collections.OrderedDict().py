from collections import OrderedDict

order_dict = OrderedDict()

N = int(input())

for _ in range(N):
    inp = input().split()
    price = int(inp[-1])
    name = " ".join(inp[0:-1])
    if name in order_dict:
        order_dict[name] += price
    else:
        order_dict[name] = price

for k, v in order_dict.items():
    print(k,v)