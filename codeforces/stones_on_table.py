n = int(input())
color = input()

removes = 0

for i in range(n - 1) :
    if color[i] == color[i+1] :
        removes += 1
        
print(removes)
