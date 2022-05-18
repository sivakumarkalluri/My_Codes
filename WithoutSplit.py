statement=input("Enter the statement : ")

word=input("Enter the character to split : ")
l=['']
count=int(input("Enter upto how many wordsto split : "))
print(l)

for i in statement:
    if i==word and len(l)<=count:
        l.append('')
    else:
        l[-1]+=i
print(l)
        
