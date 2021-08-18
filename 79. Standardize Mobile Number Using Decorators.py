def wrapper(f):
    def fun(l):
        new_lst = []
        for number in map(int, l):
            if len(str(number)) == 10:
                new_lst.append("+91 " + str(number)[:5] + " " + str(number)[5:])
            else:
                new_lst.append("+" + str(number)[:2] + " " +str(number)[2:7] + " " + str(number)[7:])
        return f(new_lst)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


