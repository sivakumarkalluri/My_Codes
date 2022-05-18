# >>>>>>The number is said to be perfect factorial if it is already a result of factorial of another number  <<<<<<<<
    #  >>>>  EXAMPLE 3!=6 so 6 is a perfect factorial numer     <<<<<<<<
def is_pf(num):
    fact=1
    i=1
    while fact<num:
        fact*=i
        i+=1
    if fact==num:
        return True
    return False
starting=int(input("Enter the starting number : "))
ending=int(input("Enter the last number : "))
for i in range(starting,ending+1):
    if is_pf(i):
        print(i,end=" ")
# num=int(input("enter the number : "))
# if is_pf(num):
#     print(num,"is perfect factorial")
# else:
#     print(num,"is not a perfect factorial")
