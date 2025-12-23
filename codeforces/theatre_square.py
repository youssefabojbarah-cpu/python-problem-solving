import math
n, m, a = map(int, input().split())

titels_n = math.ceil(n / a)
titels_m = math.ceil(m / a)

result = titels_n * titels_m

print(result)
