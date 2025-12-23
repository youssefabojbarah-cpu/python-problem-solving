n = int(input())
solved_count = 0
for i in range(n):
    p, v, t = map(int, input().split())
    if p + v + t >= 2:
        solved_count += 1
print(solved_count)
