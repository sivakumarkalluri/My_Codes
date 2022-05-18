word=raw_input()
total=0
for i in word:
    if word.count(i)==1:
        total+=1
print(total)

