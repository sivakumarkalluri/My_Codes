array=list(map(int,input().split()))
a=array[0]
r=array[1]
term=array[2]
output_list=[a]
digit=a
for i in range(term-1):
    digit=digit*r
    output_list.append(digit)
print(output_list[term-1])
