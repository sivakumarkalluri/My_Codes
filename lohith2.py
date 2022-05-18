size=int(input())
array=[]
for i in range(size):
    array.append(int(input()))
step=0
total=array[step]
while step<=size-1:

    if step+2<=size-1:
        step=step+2
        total+=array[step+2]
    else:
        break
    if step-1<=size-1:
        step=step-1
        total+=array[step-1]
    else:
        break

print(total)
    
