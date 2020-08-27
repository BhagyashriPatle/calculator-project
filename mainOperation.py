# importing from main

from main import*

print("select operation")
print("1.add")
print("2.sub")
print("3.multiply")
print("4.divide")

while True:
    # Take input from the user
    choice=input("enter number(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1','2','3','4'):

        num1=int(input("enter first value:  "))
        num2=int(input("enter second value:  "))

        if choice =='1':
             print(num1+num2)

        elif choice=='2':
             print(num1-num2)

        elif choice=='3':
             print(num1*num2)

        elif choice=='4':
             print(num1/num2)

    else:

        print("invalid")




