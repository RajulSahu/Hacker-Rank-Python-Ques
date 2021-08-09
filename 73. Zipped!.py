N = int(input().split()[1])

all_marks = []
for _ in range(N):
    marks = [list(map(float, input().split()))]
    all_marks += marks

zipped = list(zip(*all_marks))
for student in zipped:
    print("{0:.1f}".format(sum(student)/len(student)))
