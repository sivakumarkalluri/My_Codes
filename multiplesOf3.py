def multiples(a,i=0,array=[]):
    if i>=len(a):
        return array
    if a[i]%3==0:
        array.append(a[i])
    return multiples(a,i+1,array)
print(multiples([1,3,9,2,27,30,5,8]))