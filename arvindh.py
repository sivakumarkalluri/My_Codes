size=int(input())
array=list(map(int,input().split()))
if min(array)<0:
    print(max(array)+ min(array))
else:
    array=sorted(array)
    
    print(array[1]+min(array))
    
