input1="aaabccd"
input2="abc"
input3="ac"
input4="aaa"
if input2 in input1:
    input1.replace(input2,"")
if input3 in input1:
    input1.replace(input3,"")
if input4 in input1:
    input1.replace(input4,"")
print(input1)