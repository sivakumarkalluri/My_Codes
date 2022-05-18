value1=int(input("enter the first value : "))
value2=int(input("enter the second value : "))
if value1 is value2:
    print(value1,"and",value2,"are pointing to same memory location")
else:
    print(value1,"and",value2,"are not pointing to same memory location")

    # or u can try these code also
    
# if id(value1)==id(value2):
#     print(value1,"and",value2,"are pointing to same memory location")
# else:
#     print(value1,"and",value2,"are not pointing to same memory location")