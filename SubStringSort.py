array=['hai','program','pink','collection','by','class']
for j in range(len(array)-1):
    for i in range(len(array)-1):
        if len(array[i])>len(array[i+1]):
            array[i],array[i+1]=array[i+1],array[i]
print("Final sorted array is : ",array)
# print("<<<<<<<<<<<<<<<<<<<<<----------------------------->>>>>>>>>>>>>>>>>>>>>>>>")
# print("Final sorted array is : ",array)
 # print("for",j+1,"step of sorting the array is",array)