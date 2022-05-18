a=int(input())
x=int(input())
y=int(input())
output1=[]
output2=[]
x1=a//x
y1=0
if (a-x1*x)>=y:
    y1=(a-x1*x)//y
    remain1=a-(x1*x)-(y1*y)
else:
    remain1=a-(x1*x)
x2=0
y2=a//y
if (a-y2*y)>=x:
    x2=(a-y2*y)//x
    remain2=a-(y2*y)-(x2*x)
else:
    remain2=a-(y2*y)
if remain1<remain2:
    print(x1,end=" ")
    print(y1,end=" ")
    print(remain1)
elif remain1>=remain2:
    print(x2,end=" ")
    print(y2,end=" ")
    print(remain2)




