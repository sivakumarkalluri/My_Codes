num=int(input())
array=sorted(list(map(int, input ().split())))[::-1]
print(sum(array[:2]))