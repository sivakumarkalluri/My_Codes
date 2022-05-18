number=raw_input()
total=0
for i in number:
    flag=False
    if int(i)>1:
        for j in range(2,int(i)):
            if (int(i)%j)==0:
                flag=True
                break
    if flag:
        total+=int(i)
print(total)