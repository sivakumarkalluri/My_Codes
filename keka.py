n=int(input())
ones_array=[0,0,0,0,0]
tens_array=[0,0,0,0,0]
if n==5:
    ones_array[0]=1
if n<5:  
    for i in range(1,n+1):
        ones_array[-i]=1
if n>5 and n<=9:
    diff=n-5
    ones_array[0]=1
    for i in range(1,diff+1):
        ones_array[-i]=1
if n>9:
    quotient=n//10
    if quotient==5:
        tens_array[4]=1
    if quotient<5:
        for i in range(quotient):
            tens_array[i]=1
    elif quotient>5 and quotient<=9:
        diff=quotient-5
        tens_array[4]=1
        for i in range(diff):
            tens_array[i]=1
    remainder=n%10
    if remainder<=5:
        for i in range(1,remainder+1):
            ones_array[-i]=1
    if remainder>5 and remainder<=9:
        diff=remainder-5
        ones_array[0]=1
        for i in range(1,diff+1):
            ones_array[-i]=1
print(tens_array+ones_array)