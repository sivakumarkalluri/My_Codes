def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return True
    return False
starting=int(input("Enter the starting number : "))
ending=int(input("Enter the last number : "))
print("The perfect numbers between",starting,"and",ending,"are")
for i in range(starting,ending+1):
    if perfect(i):
        print(i,end=" ")
    
