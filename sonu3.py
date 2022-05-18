n=input()
if n.isalpha():
    if n[::-1]==n:
        print("you inputted a strong string")
    else:
        print('you inputted a weak string')
else:
    print('you inputted a weak string')