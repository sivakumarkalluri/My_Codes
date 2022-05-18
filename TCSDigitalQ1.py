num1=int(input())
num2=int(input())
count=0
if num1<num2:
    for i in range(num1,num2+1):
        for j in str(i):
            if str(i).count(j)==1:
                result=True
            else:
                result=False
                break
        if result:
            count+=1
    print(count)
else:
    print("INVALID INPUT")


#   THE PROBLEM STATEMENT
# Find and display count of how many numbers lying between num1 and num2 which are not having any repeated digits in that number
# EXPLANATION
# If Num1=11 ,Num2=15
# The numbers between 11 and 15 are 11,12,13,14,15 and the 11 is the only number which contain repeated digits(1 and 1) other numbers are not having any repeated digits  
# so the count of numbers with no repeated digits lying between 11 and 15 are 4 (12,13,14,15)
# similarly between num1=101 and num2=200 there are 72 numbers with non repeated digits