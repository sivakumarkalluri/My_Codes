# >>>>>>>>>>>>>>>> Sorting the dictionary based on keys <<<<<<<<<<<<<<<<<<<<<<<

dictionary={'hai':5,'program':9,'pink':67,'collection':4,'by':8,'class':6}
res=[]
for i in dictionary:
    res.append((i,dictionary[i]))
for j in range(len(res)-1):
    for k in range(j+1,len(res)):
        if res[j][0]>res[k][0]:
            res[j],res[k]=res[k],res[j]
print(dict(res))