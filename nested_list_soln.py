# Score: 10
arr = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    item = [name, score]
    scores.append(score)  # Track score values in separate array
    arr.extend([item])

# lowest score in original scores array
lowest_score = min(scores)

# scores_v2 is the scores array without the original minimum value
scores_v2 = [float(num) for num in scores if num != lowest_score]

# second_lowest_score is the second lowest value of original array
second_lowest_score = min(scores_v2)

# new_arr consists of arr items where score is second lowest only.
new_arr = [item for item in arr if item[1] == second_lowest_score]
new_arr.sort()
for item in new_arr:
    print(item[0])
