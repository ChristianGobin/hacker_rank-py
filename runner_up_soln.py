# Score: 10
n = int(input())
arr = list(map(int, input().split(" ")))
max_val = max(arr)
new_arr = [int(x) for x in arr if x != max_val]
runner_up = max(new_arr)
print(runner_up)
