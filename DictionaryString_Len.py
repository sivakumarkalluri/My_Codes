length=int(input("Enter the length of dictionary : "))
dictionary={}
for i in range(length):
    values=input("Enter the value : ")
    dictionary[values]=len(values)
print(dictionary)

