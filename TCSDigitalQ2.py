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

# PROBLEM STATEMENT
# ROTATE THE VALUES VALUES IN ARRAY BY ONE STEP IN CLOCK WISE BY K TIMES
# Example if array={10,20,30,40,50} k=2 then output is {40,50,10,20,30}