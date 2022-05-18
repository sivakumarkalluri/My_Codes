def InterestingNumbers(start,end):
    def factors(num):
        array=[]
        for i in range(1,num+1):
            if num%i==0:
                array.append(i)
        return array
    count=0
    for i in range(start,end+1):
        factor_list=factors(i)
        if len(factor_list)%2!=0:
            count+=1
    return count
print(InterestingNumbers(1,9))
    



    