starting=int(input("Enter the starting number : "))
ending=int(input("Enter the last number : "))
def prime(starting,ending):
    primes=[]
    for i in range(starting,ending+1):
        flag=True
        for j in range(2,i):
            if i%j==0:
                flag=False
                break
        if flag:
            primes.append(i)
    return primes
print(prime(starting,ending))
