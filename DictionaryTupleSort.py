dictionary={(1,2,3,4):"a",(1,2,3):"b",(1,2):"c",(1,2,3,4,5):"d"}
out_put={}
for i in dictionary:
    if type(i)==tuple and len(i)>=3:
        out_put[i]=dictionary[i]
print(out_put)
