dob=input("enter your date of birth in format dd/mm : ")
current_date="14/08"
speed=int(input("Enter speed : "))
if dob!=current_date:
    if speed<=60:
        print("your speed is",speed,"which is less than 60 so NO TICKET or",0)
    elif 80>=speed>=61:
        print("your speed is",speed,"which is inbetween 61 and 80 so SMALL TICKET or",1)
    else:
        print("your speed is",speed,"which is greater than or equal to 81 so BIG TICKET or",2)
else:
    if speed<=65:
        print("your speed is",speed,"which is less than 60 so NO TICKET or",0)
    elif 85>=speed>=66:
        print("your speed is",speed,"which is inbetween 61 and 80 so SMALL TICKET or",1)
    else:
        print("your speed is",speed,"which is greater than or equal to 81 so BIG TICKET or",2)