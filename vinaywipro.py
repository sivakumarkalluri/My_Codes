words=raw_input().split()
total=0
for i in words:
    if words.count(i)==1:
        total+=1
print(total)