def love(ch):
    differences=[]
    for i in vowels_asciis:
        differences.append(abs(ord(ch)-i))
    return differences.index(min(differences))
word=input()
vowels_asciis=[ord('a'),ord('e'),ord('i'),ord('o'),ord('u')]
result=""
for i in word:
    result+=chr(vowels_asciis[love(i)])
print(result)
