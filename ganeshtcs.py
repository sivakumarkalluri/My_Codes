size=int(input())
array=[]
for i in range(size):
    array.append(int(input()))
total=array[0]
for i in range(1,size):
    total-=array[i]
print(total)
if total%2==0:
    print("Even")
else:
    print("Odd")