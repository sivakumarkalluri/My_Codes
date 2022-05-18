value=str(int(input()))
primes=[]
for i in value:
    flag=1
    for j in range(2,int(i)):
        if int(i)%j==0:
            flag=0
    if flag:
        primes.append(int(i))
print(sum(primes))
