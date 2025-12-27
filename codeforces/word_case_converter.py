word = input()
count_upper = 0
count_lower = 0

for i in word :
    if i.isupper() :
        count_upper += 1
    else:
        count_lower += 1

if count_upper > count_lower :
    print(word.upper())
elif count_upper <= count_lower :
    print(word.lower())
