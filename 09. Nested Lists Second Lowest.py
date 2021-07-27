def second_lowest(data, scores):
    scores.sort()
    second_lowest_score = scores[1]
    result = data[second_lowest_score]
    result.sort()
    print(*result, sep="\n")
    
    

if __name__ == '__main__':
    python_students = {}
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in python_students:
            python_students[score].append(name)
        else:
            python_students[score] = [name]
        if score not in scores:
            scores.append(score)
    second_lowest(python_students, scores)
