productString="xyyxabcdefx"
flag=True

result=productString
while flag:
    st=True
    for i in range(len(result)-2):
        if result[i]==result[i+1]:
            st=False
            result=result.pop(i)
            result=result.replace(result[i+1],"")
    if st:
        print(result)
        break
