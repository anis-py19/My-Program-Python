from TradeMenu  import *
from AccountUser  import *
def create_account():
    return user.login()
def menu_trader():
    count = 0
    enter_pass = input("Enter Your Password To Access The Menu: ")
    while enter_pass != trader.password:
        count+=1
        enter_pass = input("\n---Wrong Password Try Again: ")
        if count == 3 :
            print("\n---To Many Try---\nCan't Access For Trader Menu!!---\n")
            return None
    print("="*25)
    print("--Welcome In Your Menu--")
    print("="*25)
    print("1-Add Product\n2-Modify Product\n3-Show Products\n4-Show Stock\n5-Show Sells\n6-Exit")
    choice = input("Enter Your Choice : ")
    return choice
def menu():
    print("1-Take Order\n2-Check My point\n3-Deactivate My Account\n4-Check Balance\n5-Check Bill\n6-Exit")
    choice = input("Enter Your Choice : ")
    return choice
print("--Welcome To My Our MiniShop System--")
while True :
    #when the user tab in every choice 00 will return to the menu
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    choice = menu()
    if user.active :
        if choice == "00":
            if trader.password :
                choice = menu_trader()
                while True :
                    if choice == "1" :
                        trader.add_product()
                    elif choice =="2":
                        trader.modify_product()
                    elif choice == "3":
                        trader.show_products()
                    elif choice == "4":
                        trader.show_stock()
                    elif choice == "5":
                        trader.show_sells()
                    elif choice == "6":
                        print("="*25)
                        print("--See You Later Sir--")
                        print("="*25)
                        break
                    else:
                        print("\n---Wrong Choice Try Again!!!---\n")
            else:
                print("----Wrong Password----")
        else:
            if choice =="1":
                if trader.products:
                    count = 0
                    trader.show_products()
                    order= input("Enter The Name Of Product You Want To Buy : ")
                    while order not in trader.products.keys():
                        count +=1
                        order = input("**Can't Find This Product In Our Store**\nEnter-Again: ")
                        if count == 3:
                            print("\n---Too Many Try---\nRerturn To Menu!!!-\n")
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
                                    print("\n---Too Many Try---\nRerturn To Menu!!!-\n")
                                    break
                            trader.products[order]["Stock"] -= quantity
                            user.point += (quantity * trader.products[order]["Price"])/100
                            user.balance -= quantity * trader.products[order]["Price"]
                            trader.sells[order]= {"QTY": quantity, "Price": trader.products[order]["Price"]*quantity}
                            print("---Order Taken Successfully---\nChek Your Bill Too Pay")
                        except ValueError:
                            print("\n****Worng Value****\nRerturn To Menu!!!-\n")
                else:
                    print("Wait For The ADMIN To Add Products!!......")
            elif choice =="2":
                print()
                user.check_point()
                print()
            elif choice =="3":
                print()
                user.deactivate()
                print()
            elif choice == "4":
                print()
                user.check_balance()
                print()
            elif choice == "5":
                print("---Your Bill---")
            else:
                print("\n---Wrong Choice Try Again!!!---\n")
    else:
        print("---Your Account Is Deactivated Please ACTIVATE It To Take Order---")
        create_account()
        print("---Now You Can Take Order---")