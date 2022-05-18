num=int(input())
n=int(input())
num=str(num)
if n<=len(num):
    print(int(num[n-1]))
else:
    print(-1)