def average(marks, name):
    if name in marks:
        average = "{:.2f}".format(sum(marks[name])/len(marks[name]))
        print(average)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average(student_marks, query_name)
