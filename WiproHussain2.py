
value=input()
num=int(input())
output=""
for i in range(0,len(value),num):
    output+=value[i:i+num]+" "
print(output)