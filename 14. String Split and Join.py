def split_and_join(line):
    # write your code here
    str_list = line.split(' ')
    return "-".join(str_list)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)