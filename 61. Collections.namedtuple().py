from collections import namedtuple

N = int(input())

variables = " ".join(input().split())
student_data = namedtuple('student_data', variables)
total_marks = 0

for _ in range(N):
    total_marks += int(student_data(*input().split()).MARKS)

print("{0:.2f}".format(total_marks / N))