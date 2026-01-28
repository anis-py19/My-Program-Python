#welcome in my simple program stock management system
stock = {}
#fisrt we create menu function
def menu():
    print("Welcome To The Stock Management System")
    print("1-Add Item\n2-View Stock\n3-Update Quantity\n4-Remove Item\n5-Exit")
    return input("Select An Option Please: ")
#fucntion to add item 
def add_item():
    enter_item = input("Enter Item Name: ")
    item_qty = int(input(f"Enter The Quantity For {enter_item}: "))
    item_price = float(input(f"enter The Price For {enter_item}: "))
    item_pv = float(input(f"Enter Your {enter_item} Price OF Purchase: "))
    if enter_item in stock :
        print(f"The {enter_item} is lready In Your Stock, Update the QTY if neded!!")
    else : 
        stock[enter_item]= {"QTY": item_qty , "PRICE": item_price,"PV":item_pv,"BENEFICE":(item_pv-item_price)}
        print(f"Greet You Aded {enter_item} To Your Stock Succesffuly")
#function to view stock 
def view_stock():
    if len(stock)==0:
        print("Invalid Stock Items , Please Add Some Item In Your Stock!")
        return None
    else: 
        for key , values in stock.items():
            print(f"Item Name: {key},QTY: {values["QTY"]},PRICE: {values["PRICE"]},PV: {values["PV"]},Benifice: {values["BENEFICE"]}")
#function to update qty
def update_qty():
    if len(stock)==0:
        print("Invalid Stock Items , Please Add Some Item In Your Stock!")
        return None
    else:
        #ask which one to update
        ask = input("Enter The Item Name To Update The QTY: ")
        if ask not in stock:
            print(f"The {ask} Not In Your Stock!!!")
        else :
            #ask to add or remove some qty
            action = input("Do You Want To Add Or Remove QTY: ")
            while action.lower() != "remove" and action.lower()!="add":
                action = input("Invalid Enter!! (add/remove): ")
            if action.lower()=="add":
                new_qty = int(input(f"Enter The New QTY for {ask}: "))
                stock[ask]["QTY"]+= new_qty
                print(f"QTY Aded Succesffuly , New QTY IS {stock[ask]["QTY"]}")
            elif action.lower()== "remove":
                new_qty = int(input(f"Enter THE QTY To Remove FROM {ask}: "))
                if new_qty > stock[ask]["QTY"]:
                    print(f"You Cannot Remove {new_qty} From {ask}\nBecause The QTY IS: {stock[ask]["QTY"]}")
                else:
                    stock[ask]["QTY"] -= new_qty
                    print(f"QTY Removed Succesfuly From {ask}, New Qty is {stock[ask]["QTY"]}")
#fucntion to remove item
def remove_item():
    if len(stock)==0:
        print("Invalid Stock Items , Please Add Some Item In Your Stock!")
        return None
    else : 
        ask = input("Enter The Item Name And I Remove It From Stock List: ") 
        if ask not in stock :
            print(f"The {ask} Not In Your Stock!!!\nTry Again!!")
        else : 
            del stock[ask]
            print(f"The {ask} Removed Succesfully !!!")
            #ask if want to show stock after remove item
            choice = input("Do You Want To View Stock Now?: ").lower()
            if choice == "yes":
                for key , values in stock.items():
                    print(f"Item Name: {key},QTY: {values['QTY']},PRICE: {values['PRICE']},PV: {values['PV']},Benifice: {values['BENEFICE']}")
            else:
                print("Okey::)")
#function to exit 
def exit_prgrm():
    print("Thanks For Your Time , See You In Next Program!!")
    quit()        
                               
while True:
    print("\n")
    choice = menu()
    if choice == "1":
        add_item()
    elif choice == "2":
        view_stock()
    elif choice == "3":
        update_qty()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        exit_prgrm()
    else:
        print("Invalid Option , Please Try Again!!")