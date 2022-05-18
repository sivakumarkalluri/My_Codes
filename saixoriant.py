array=[]
while True:
    a=int(input())
    array.append(a)
    if a<0:
        break
flag=True
array=array[::-1]
for i in array:
    if i>=100:
        flag=False
        print(i)
        break
if flag:
    print(0)