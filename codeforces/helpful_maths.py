s = input()

nums = []

for i in s:
    if i != "+":
        nums.append(int(i))

nums.sort()

for i in range(len(nums)):
    print(nums[i], end="")
    if i != len(nums) - 1:
        print("+", end="")
