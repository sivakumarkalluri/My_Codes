number=input()
output=""
for i in number:
    if int(i)%2==0:
        output+=str(int(i)+1)
    else:
        output+=str(int(i)-1)
print(int(output))