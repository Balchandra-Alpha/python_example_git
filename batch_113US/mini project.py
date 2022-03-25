# balance = 2000
# pin = 9987
# user_pin = int(input("enter your 4 digit atm pin: "))
# if user_pin == pin:
#     print("Welcome!!!!!",
#           "press 1 to balance check",
#           "press 2 to change the pin",
#           "press 3 to withdraw balance",
#           "press 4 to check last three transactions list",
#           "**************************", sep="\n")
#     print()
#     user_selection = int(input("enter your choice : "))
#     if user_selection == 1:
#         print("your balance is :  ", balance)
#     elif user_selection == 2:
#         new_pin_1 = int(input("please enter a valid 4 digit pin : "))
#         new_pin_2 = int(input("please confirm your pin : "))
#         if new_pin_1 == new_pin_2:
#             pin = new_pin_1
#             print("your new pin is : ", pin)
#         else:
#             print("confirmation failed!  pins mismatching")
#     elif user_selection == 3:
#         balance_withdraw = int(input("enter the amount : "))
#         if balance_withdraw <= balance:
#             print("transaction completed successfully")
#             print("your remaining balance is", balance - balance_withdraw)
#         else:
#             print("*********FAILED*********",
#                   "enter a valid withdraw amount", sep="\n")
#     elif user_selection == 4:
#         print("10/02/2022    100   transfer",
#               "05/02/2022    500   transfer",
#               "27/01/2022    300   transfer", sep="\n")
#         print("available balance is", balance)
#     else:
#         print("please select a valid option")
# else:
#     print("enter valid pin")
##########################33


balance = 2000
trans=["dummy1","dummy2","dummy3","dummy4"]
pin = 9987
com="c"
while com == "c":

    user_pin = int(input("enter your 4 digit atm pin: "))
    if user_pin == pin:
        print("Welcome!!!!!",
              "press 1 to balance check",
              "press 2 to change the pin",
              "press 3 to add money ",
              "press 4 to withdraw money ",
              "press 5 to see last  transaction",
              "**************************", sep="\n")
        print()
        user_selection = int(input("enter your choice : "))
        if user_selection == 1:
            print("your balance is :  ", balance)
            print("press c to contniue...")
        elif user_selection == 2:
            new_pin_1 = int(input("please enter a valid 4 digit pin"))
            new_pin_2 = int(input("please confirm your pin : "))
            if new_pin_1 == new_pin_2:
                pin = new_pin_1
                print("your new pin is : ", pin)
                print("press c to contniue...")
                com = input()
            else:
                print("confirmation failed!  pins mismatching")
        elif user_selection == 3:
            amt = float(input("enter the amount:"))
            balance = balance + amt
            print("The amount is updated successfully")
            print("Balance:", balance)
            stm = f"Deposited amount {amt} into the bank : Balance:{balance}"
            trans.append(stm)
            print("press c to contniue...")
            com = input()

        elif user_selection == 4:
            amt = float(input("Enter the amount to withdraw:"))
            if balance < amt:
                print("Does not have a sufficent balance!!!")
            else:
                balance = balance - amt
                print("The withdraw is Successful")
                print("Balance:", balance)
                stm = f"Withdraw amount {amt} into the bank: Balance:{balance}"
                trans.append(stm)
                print("press c to contniue...")
                com = input()
        elif user_selection == 5:
            a=trans[-3:]
            print(*a,sep="\n")
            print("press c to contniue...")
            com = input()
        else:
            print("please select a valid option")
    else:
        print("enter valid pin")


















