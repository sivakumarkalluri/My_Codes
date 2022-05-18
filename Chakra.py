size=int(input())
l=input()
array=[]
for i in l:
    if i!="{" and i!="}" and i!=",":
        array.append(int(i))

k=int(input())
out_list=[]

for j in range(3):
    sum=0
    for i in array:
        sum+=max(i-j,0)
    out_list.append(sum)
print(out_list)
diff=[]
for i in out_list:
    if i<=k :
        
        diff.append(k-i)
    else:
         diff.append(k+1)
print(diff)
print(diff.index(min(diff)))
