word="xyyxabcdefx"
l=[]
for i in word:
    l.append(i)
for i in range(len(l)-1):
    if l[i]==l[i+1]:
        l.pop(i)
        l.pop(i+1)
print(l)
