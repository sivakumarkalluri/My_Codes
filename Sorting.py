array=[8,3,7,2,5,1]
#<<<<<<<<<<<<<<<<<<  Normal Sorting technique   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# for i in range(len(array)-1):
#     for j in range(i+1,len(array)):
#         if array[i]>array[j]:
#             array[i],array[j]=array[j],array[i]
# print(array)

# <<<<<<<<<<<<<<<<<<<<<  Sorting by step wise    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

for j in range(len(array)-1):
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            array[i],array[i+1]=array[i+1],array[i]
    print("for",j+1,"step of sorting the array is",array)
print("<<<<<<<<<<<<<<<<<<<<<----------------------------->>>>>>>>>>>>>>>>>>>>>>>>")
print("Final sorted array is : ",array)