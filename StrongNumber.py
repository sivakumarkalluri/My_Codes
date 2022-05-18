# >>>>>>>>>>sum of factorial of each digit in a number is equal to original number         <<<<<<<<<<<<<
# >>>>>>> EXAMPLE   number = 145 >>> 1!+4!+5! = 1+24+125 = 145 = number so 145 is Strong Number     <<<<<<<<<< 

def Strong(num):
    temp=num
    sum=0
    while temp!=0:
        remainder=temp%10
        
        sum+=fact(remainder)
        temp=temp//10
    if sum==num:
        return True
    return False   
def fact(num):
    i=1
    factorial=1
    while i<=num:
        factorial*=i
        i+=1
    return factorial
starting=int(input("Enter the starting number : "))
ending=int(input("Enter the last number : "))
print("Strong numbers between",starting,"and",ending,"are : ")
for i in range(starting,ending+1):
    if Strong(i):
        print(i,end=" ")
# num=int(input("Enter the number : "))
# if Strong(num):
#     print(num,"is a strong number")
# else:
#     print(num,"is not a strong number")
