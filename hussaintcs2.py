word=input()
sentence=input()
output=""
for i in sentence:
    for j in word:
        if i==j:
            output+=j
print(output)