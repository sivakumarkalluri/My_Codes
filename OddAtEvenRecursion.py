def Odds(a,i=0):
    if i>=len(a):
        return
    if i%2==0 and a[i]%2!=0:
        print(a[i])
    return Odds(a,i+1)
print(Odds((2,3,5,6,7,9,11)))