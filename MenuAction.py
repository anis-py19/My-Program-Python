from TradeMenu  import *
from AccountUser  import *
def create_account():
    return user.login()
def menu():
    print("1-Take Order\n2-Check My point\n")
    choice = input("Enter Your Choice : ")
    return choice
print("--Welcome To My Our MiniShop System--")
while True :
    #when the user tab in every choice 00 will return to the menu
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    choice = menu()
    if user.active :
        if choice =="1":
            if trader.products:
                count = 0
                trader.show_products()
                order= input("Enter The Name Of Product You Want To Buy : ")
                while order not in trader.products.keys():
                    count +=1
                    order = input("**Can't Find This Poroduct In Our Store**\nEnter-Again: ")
                    if count == 3:
                        print()
                        print("---Too Many Try---\nRerturn To Menu!!!-")
                        break
                if order in trader.products.keys():
                    try :
                        quantity = int(input(f"Enter The Quantity OF {order} Want To Buy: "))
                        count=0
                        while quantity <=0 or quantity > trader.products[order]["Stock"]:
                            count+=1
                            if quantity <=0 :
                                quantity = int(input("--Qantity Must Be Positive--\nEnter-Again: "))
                            elif quantity > trader.products[order]["Stock"]:
                                quantity = int(input(f"--We Only Have {trader.products[order]['Stock']} In Our Stock--\nEnter-Again: "))
                            if count ==3:
                                print()
                                print("---Too Many Try---\nRerturn To Menu!!!-")
                                break
                        trader.products[order]["Stock"] -= quantity
                        user.point += (quantity * trader.products[order]["Price"])/100
                        user.balance -= quantity * trader.products[order]["Price"]
                        trader.sells[order] = (order,quantity)
                    except ValueError:
                        print()
                        print("****Worng Value****\nRerturn To Menu!!!-")
            else:
                print("Wait For The ADMIN To Add Products!!......")

        else:
            print("---Your Account Is Deactivated Please ACTIVATE It To Take Order---")
    else:
        print("---You Must Create An Account---")
        create_account()
