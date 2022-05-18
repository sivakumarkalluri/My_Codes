array=list(map(int,input().split()))
<<<<<<< HEAD
l=[0]
for i in range(len(array)-1):
    result=True
    repeat=1
    for j in range(i+1,len(array)):
        if array[j-1]<array[j] and result==True:
            result=True
            repeat+=1
            if j+1==len(array):
                l.append(repeat)
        else:
            if max(l)<repeat:
                l.append(repeat)
                result=False
                break
            else:
                result=False
                break
print(max(l))

=======
shift=int(input())
l=[]
if shift>size:
    shift=shift-size
for i in array[shift:]:
    l.append(i)
for i in array[:shift]:
    l.append(i)
for i in l:
    print(i,end=" ")
>>>>>>> bfe60d88b340e65d9eef7789eedc86c3e462b38f
