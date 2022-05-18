word=list(input().split(","))
for letter in word:
    if letter[::-1]==letter:
        print("you inputted a strong string")
    else:
        print('you inputted a weak string')