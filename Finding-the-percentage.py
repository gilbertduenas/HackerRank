if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    score = student_marks[query_name]
    avg_score = sum(score)/len(score)

    print(f'{avg_score:.2f}')
