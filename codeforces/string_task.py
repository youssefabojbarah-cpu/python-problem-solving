word = input()
vowels = ['a','o','y','e','u','i','A','O','Y','E','U','I']
result = ""

for i in word :
    if i not in vowels :
        result += "." + i.lower()

print(result)
