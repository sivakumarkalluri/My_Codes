size=int(input())
data=list(input().split())
m=int(input())
array=list(map(int,input().split()))
output=""
for i in range(size):
    output+=data[i]+" "+str(array[i])+" "
print(output)