# a=[1,2,3,4,5]
# res=[]
# pos=int(input("Enter the position to delete : ")) 
# for i in range(len(a)):
#     if i!=pos:
#         res+=[a[i]]
# print(res)
a=[1,2,3,4,5]
res=[]
element=int(input("Enter the element to delete : ")) 
for i in a:
    if i!=element:
        res+=[i]
print(res)