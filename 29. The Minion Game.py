def minion_game(string):
    len_s = len(string)
    vow = cons = 0
    for i in range(len_s):
        if string[i] in "AEIOU":
            vow = vow + (len_s - i)
        else:
            cons = cons + (len_s - i)
    if cons > vow:
        print(f"Stuart {cons}")
    elif vow == cons:
        print("Draw")
    else:
        print(f"Kevin {vow}")

if __name__ == '__main__':
    s = input()
    minion_game(s)