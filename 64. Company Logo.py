from collections import Counter


def display(s):
    counted_alphabets = dict(Counter(s))
    counted_alphabets = dict(sorted(counted_alphabets.items(), key=lambda x: x[0]))
    counted_alphabets = dict(sorted(counted_alphabets.items(), key=lambda x: x[1], reverse=True))
    count = 0
    for k, v in counted_alphabets.items():
        count += 1
        print(k, v)
        if count == 3:
            break


if __name__ == '__main__':
    input_string = input()
    display(input_string)
