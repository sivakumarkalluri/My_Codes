def solve(N,X,A):
    import itertools
    from itertools import combinations_with_replacement
    size=N
    x=X
    array=A
    result=[]
    combs=[]
    numbers=[num for num in range(x+1)]
    for r in range(size+1):
        combs.append(list(itertools.combinations_with_replacement(numbers, r)))
    for sub in combs[size:]:

        for sub in sub:
            def find(sub):
                if sum(sub)==x:
                    flag=False
                    for i in range(size):
                        if sub[i]>=array[i]:
                            flag=True
                        else:
                            flag=False
                            break
                    if flag:
                        result.append(sub)
            find(sub)
            if size>1:
                find(sub[::-1])
    return len(result)
print(solve(1,7,[3]))