n=int(input())
array=list(map(int,input().split()))
output=[]
array=sorted(array,reverse=True)
for i in range(n):
    total=sum(array[i:])
    output.append(total)
output=sorted(output,reverse=True)
print(output)
for i in output:
    if i%2!=0:
        print(i)
        break