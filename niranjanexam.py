n=int(input())
word=input()
closed=")"
open="("
a=0
b=0
for i in word:
    if i==closed: 
        a=word.count(i)
    if i==open:
        b=word.count(i)
maximum=max(a,b)
for i in range(maximum):
    print("(",end="")
for j in range(maximum):
    print(")",end="")