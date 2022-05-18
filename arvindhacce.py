array=list(map(int,input().split()))

for i in range(len(array)-1):
    for j in range(i+1,len(array)):
        if sum(array[:i+1])==sum(array[i+1:]):
            print(sum(array[:i+1]))
            break
        