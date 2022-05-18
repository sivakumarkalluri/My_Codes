statement=raw_input()
output=""
for i in statement:
    if ord(i)>=65 and ord(i)<=90:
        output+=chr(ord(i)+32)
    elif ord(i)>=97 and ord(i)<=122:
        output+=chr(ord(i)-32)
    else:
        output+=" "
print(output)