value=input()
char=input()
array=[i for i in value]
data=[i for i in char]
for i in range(len(data)):
    for j in range(len(array)):
        if data[i]==array[j]:
            del(array[j])
print(array)