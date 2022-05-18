a=input()
b=input()
vowels=['a','e','i','u','o']
if len(a)==len(b):
    print("true",end=" ")
else:
    print("false",end=" ")
print(ord(b[-1]),end=" ")
count=0
for i in a:
    if i in vowels:
        count+=1
for i in b:
    if i in vowels:
        count+=1
print(count)

