test=int(input())
output=[]
for i in range(test):
    size=int(input())
    array=list(map(int,input().split()))
    total_1=sum(array[::2])
    total_2=sum(array[1::2])
    output.append(max(total_1,total_2))
for i in output:
    print(i)

