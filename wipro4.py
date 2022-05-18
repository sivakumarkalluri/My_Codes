size=int(input())
array=list(map(int,input().split()))
primes=[]
non_prime=[]
for i in array:
    flag=0
    if i==1 or i==2 or i==3:
        primes.append(i)
    else:
        for j in range(3,i):
            if i%j!=0 :
                flag=1
                
            else:
                flag=0
                non_prime.append(i)
                print("non prime",i)
                break
        if flag==1:
            primes.append(i)
print(primes+non_prime)