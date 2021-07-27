def swap_case(s):
    result_str = ""
    for char in s:
        if char.islower():
            result_str += char.upper()
        elif char.isupper():
            result_str += char.lower()
        else:
            result_str += char
    return result_str
            
   

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)