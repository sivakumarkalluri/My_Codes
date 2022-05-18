def sum_list(array,sum=0,i=0):
    if i>=len(array):
        return sum
    if type(array[i])==int:
        sum+=sum(array[i],sum,i+1)
    # i+=1
print(sum_list([1,2,3]))
    