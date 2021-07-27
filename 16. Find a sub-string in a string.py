def count_substring(string, sub_string):
    count = 0
    len_str = len(string)
    len_sub_str = len(sub_string)
    for i in range(len_str-(len_sub_str-1)):
        if sub_string == string[i:i+(len_sub_str)]:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)