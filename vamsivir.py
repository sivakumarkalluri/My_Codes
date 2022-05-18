from itertools import combinations

def findOmegas( A):
    count=0
    def Omegas(num):
        squares=[]
        for i in range(2,num+1):
            if (i**(.5)==int(i**(.5))):
                squares.append(i)
        flag=1
        # print("squares under",num," are-------> ",squares )
        for i in squares:
            if num%i==0:
                return False
        
        # print("yes",num," is omega")
        return True
    
    for i in range(1,len(A)):
        combs=list(combinations(A,i))
        # print(combs)
        
        for j in combs:
            mul=1
            for k in j:
                mul=mul*k
            # print("mul of ",j," is ",mul)
            if Omegas(mul):
                count+=1
    return count
print(findOmegas([2,2,2]))
