from numpy import array


size=int(input())
array=sorted(list(map(int,input().split())))[::-1]
print(array[int(input())-1])