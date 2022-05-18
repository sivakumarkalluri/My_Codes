sentence=input().split()
value=input()
length=0
count=0
for i in sentence:
    if i.lower()==value.lower():
        count+=1
    length+=1
print(length)
print(count)
