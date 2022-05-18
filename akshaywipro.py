number=raw_input()
result=""
for i in number:
    if int(i)%2==0:
        result+=str(int(i)+1)
    else:
        result+=str(int(i)-1)
print(int(result))