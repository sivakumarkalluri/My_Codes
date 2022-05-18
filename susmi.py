size=int(input())
array=[]
flag=True
for i in range(size):
    array.append(input())
for i in array:
    total=array.count(i)
    if total%2!=0:
        print(i)
        flag=False
        break
if flag:
    print("All are even")
        