# Enter your code here. Read input from STDIN. Print output to STDOUT
before = []
odd = []
even = []
after = []
def ginortS(S):
    final = ""
    for char in S:
        if char.islower():
            before.append(char)
        elif char.isupper():
            after.append(char)
        elif char.isnumeric():
            if int(char) % 2 == 0:
                even.append(int(char))
            else:
                odd.append(int(char))
                
    before.sort()
    after.sort()
    odd.sort()
    even.sort()
                
    for i in before:
        final += i
        
    for i in after:
        final += i
        
    for i in odd:
        final += str(i)
        
    for i in even:
        final += str(i)
        
    print(final)

S = input("")
ginortS(S)
    
    
    
                
            
