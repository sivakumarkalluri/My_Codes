
l=['hi',"hello","how","are","you"]
word=input("Enter the character to split : ")


output=""
for i in range(len(l)):
    output+=l[i]

    if i!=len(l)-1:
        output+=" "
print(output)
        
