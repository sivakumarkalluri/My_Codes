size=raw_input()
array=list(map(int,raw_input().split()))
divisors=list(map(int,raw_input().split()))
count=0
for i in array:
    if divisors[0]%i==0 and divisors[1]%i==0:
        count+=1
print(count)