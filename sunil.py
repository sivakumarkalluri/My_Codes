array=list(map(int,input().split()))
number=str(array[0])
n=str(array[1])
number=number.replace(n,"")
print(len(number))