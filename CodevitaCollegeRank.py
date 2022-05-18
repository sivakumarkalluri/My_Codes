C,N=list(map(int,input().split()))
seats=list(map(int,input().split()))
data=[]
for i in range(N):
    info=list(input().split(","))
    info[0]=info[0].split("-")[1]
    for j in range(3):
        info[2+j]=info[2+j].split("-")[1]
    data.append(info)
data=sorted(data, key=lambda x: (-float(x[1]),str(x[0])))
print(data)
for student in data:
    for choices in student[2:]:
        if seats[int(choices)-1]>0:
            seats[int(choices)-1]=seats[int(choices)-1]-1
            print("Student-{reg} C-{choice}".format(reg=student[0],choice=choices))
            break
