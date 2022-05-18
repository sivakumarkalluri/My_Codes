input1=[3,2]
input3=2
input2="PN"
total=0
for i in range(input3):
    if input2[i]=="P":
        total+=input1[i]
    else:
        total+=-input1[i]
return total
