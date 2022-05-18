word=input()
flag=False
for i in word:
    if word.count(i)%2==0:
        flag=True
    else:
        flag=False
        break
if flag:
    print("Pairing is possibe")
else:
    print("Pairing is not possibe")