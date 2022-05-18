number=3
fib1=0
fib2=1
output=0
for i in range(number):
    output+=fib1
    fib3=fib2+fib1
    fib1,fib2=fib2,fib3
print(output)
