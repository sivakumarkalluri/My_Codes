arr=[1,-2,9,4,1,-7]
def FindMid(arr):
    output=[]
    for i,j in enumerate(arr):
        output.append(j+((i+1)**2))
    return output
print(output)