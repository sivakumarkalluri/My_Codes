

value=input()
small="aeiouaeiou"
large="AEIOUAEIOU"
output=""
for i in value:
    if i in small:
        
        output+=small[small.index(i)+1]
    elif i in large:
        output+=large[large.index(i)+1]
    else:
        output+=i
print(output)