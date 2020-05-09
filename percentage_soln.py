# Score: 10
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

# calculate average
avg = (sum(student_marks[query_name])) / len(student_marks[query_name])

# format avg to display up to 2 decimals
print("{:.2f}".format(avg))
