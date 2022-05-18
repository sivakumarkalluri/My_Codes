size=raw_input()
array=list(map(int,raw_input().split()))
N=0
for i in array:
    N+=i
cube_root = round(N**(1/3))
temp=N
if cube_root* cube_root * cube_root == N :
    print("Yes")
else:
    while True:
        cube_root = round(N**(1/3))
        if cube_root* cube_root * cube_root == N :
            print(N-temp)
            break
        else:
            N+=1
        
