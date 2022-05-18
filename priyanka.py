from sys import flags


word="1234"
y=30
size=4
array=[]
l=[]
count=0
for i in range(len(word)-1):
    flag=False
    for j in range(i+1,len(word)):
        data=word[int(i):int(j)]
        for i in data:
            if i not in l:
                flag=True
                l.append(i)
            else:
                flag=False
                break
        if flag and int(data)<=30 and data not in array:
            count+=1
            array.append(data)

print(len(array))
print(array)
            