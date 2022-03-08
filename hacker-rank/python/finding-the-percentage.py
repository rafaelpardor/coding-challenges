#!/usr/bin/python3

def calc_avg(listt):
    return sum(listt)/len(listt)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    for i in student_marks:
        student_marks.update({i:calc_avg(student_marks[i])})
    query_name = input()

    print("{:.2f}".format(student_marks[query_name]))
