import textwrap

def wrap(string, max_width):
    c = 1
    final_str = ""
    for i in range(len(string)):
        if i == (max_width*c):
            final_str += "\n"
            final_str += string[i]
            c += 1
        else:
            final_str += string[i]
    return final_str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)