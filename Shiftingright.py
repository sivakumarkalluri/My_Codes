size=int(input())
array=list(map(int,input().split()))
shift=int(input())
l=[]
if shift>size:
    shift=shift-size
for i in range(shift,0,-1):
    l.append(array[-i])
for i in array[:len(array)-shift]:
    l.append(i)
for i in l:
    print(i,end=" ")

