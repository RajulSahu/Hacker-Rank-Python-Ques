def merge_the_tools(string, k):
    n = len(string)
    sub = ""
    sub_lst = []
    i = 0
    for char in string:
        i += 1
        if char not in sub:
            sub += char
        if i % k == 0:
            print(sub)
            sub = ""
            
            
        
        
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)