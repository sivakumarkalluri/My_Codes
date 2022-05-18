value=input()
num=int(input())
array=list(input().split())
output=[]
for i in array:
    output.append(value.count(i)*ord(i))
print(sum(output))