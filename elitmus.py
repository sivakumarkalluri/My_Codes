test=int(input())
array=[]
vowels=['A','E','I','O','U','a','e','i','o','u']
for i in range(test):
    word=input()
    output=""
    for i in word:
        if i not in vowels:
            output=output+'*'
            if i.isupper():
                output+=i.lower()
            else:
                output+=i
            
    array.append(output)
for i in array:
    print(i)
