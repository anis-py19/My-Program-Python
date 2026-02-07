#welcome in my simple personal journal manager
#list of categories:
categories = {"Saving":{"Emergency Fund":0,"Education":0},
                "Home Exp":{"Electricity":0,"Gas/Oil":0,"Water":0,"Phone":0,"Internet":0},
                "Transport":{"Vehicle":0,"Auto Assurance":0,"Fuel":0,"Transport City":0},
                "Health":{"Dentist":0,"Health Insurance":0},
                "Daily Living":{"Barber":0,"Clothing":0,"Eat Out":0,"Gym":0}}

def menu():
    print("1-Enter Data\n2-Show Catgorie\n3-Edit Categorie\n4-Enter Amount\n5-Final Result")
    choice = input("Which Service Want To Enter: ")
    return choice
data = {"month":"","balance":0,"total_exp":0,"end_balance":0}
def log(data):
    #hadi tae ida zad dar mera whdakhra:
    if data["month"]!=""and data["balance"]!=0:
        print("--- You Already Enter Data ---")
        print(f"Month: {data["month"]}\nBalance: {data["balance"]}\n{"-"*8}\nRestart Program To Add New Data\n{"-"*8}")
    else:
        #enter the balance and the month:
        data["month"]=input("Which Month Want To Add: ").capitalize()
        month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        while data["month"] not in month  :
            data["month"]=input(f"{"-"*8}\ndosn't Exist This Month Ttry Again: ").capitalize()
        print(f"{"-*"*8}\nMonth Added!\n{"-*"*8}")
        data["balance"]=float(input("Enter Your Monthly Balance: "))
        while data["balance"]<=0:
            data["balance"]=float(input(f"Enter The Right Balance Please: "))
        print("Data Added Successfully:::")
    return data
def show_cat(categories):
    #now i going to show all category key and value
    #after we start enter the amount of every category ... must to clean [add/remove] Category
    print("----Categories----")
    for key , values in categories.items():
        print(key,end=" : ",)
        print(values)
    return categories
#ask which one of category want to edit
def edit_cat(categories):
    #add / edit / remove
    ask = input("Enter What Service You Want:\n1-add\n2-remove\n3-edit: ")
    while ask not in ["1","2","3"]:
        ask=input("Wrong Enter:)\nTry Again: ")
    if ask == "1":
        #ask category key or values
        choice = input("What You Want to Add?\n1-Category Key \n2-Category Value: ")
        while choice not in ["1","2"]:
            choice = input("Wrong Enter:)\nTry Again: ")
        if choice == "1":
            #add key and value:
            add = input("Enter Your New Category To Add: ")
            categories[add]={}
            #value category 
            add_val = input(f"Enter Value [item of type] Of {add}:")
            categories[add][add_val]=0
            print(f"{"-*"*8}\nItem Added SuccessFully In Cat Items:)\n")
        elif choice == "2":
            if categories:
            #ask which type catgeory to addin
                for x in categories.keys():
                    print(x,end=" -* ")
                print()
                ask = input("Which Category Want To Add Item In: ")
                while ask not in categories.keys():
                    ask = input(f"{ask} Not In Category List!!\n Enter Again: ")
                add_val = input(f"Enter New Value in {ask}: ")
                categories[ask][add_val]=0
            else:
                 print("-- Cant Add Value , No Keys In List\n---Add  New Items:) --")        
    elif ask == "2":
        if categories:
            #two choices [clear all list cat and remove one of list]:
            choice = input("You Have Two Choices:\n1-Clear All Categories List\n2-Remove Key/Value\nEnter[Clear-Remove]: ")
            while choice not in ["Clear" , "Remove"] :
                choice=input("Wrong Enter:)\nTry Again: ")
            if choice == "Clear":
                ask = input("Want To Clear All Item In Catgories List?: ")
                if ask =="yes":
                    print("---Clear Done\nEnter New List----")
                    categories.clear()
                else:
                    print("---Error---")
            elif choice == "Remove":
                ask = input("1-Remove Key\n2-Remove Value\nEnter: ")
                if ask =="1":
                    print("---List Of Keys---")
                    for x in categories.keys():
                        print(x,end="---")
                    print()
                    enter= input("What Key Want To Delete: ")
                    while enter not in categories.keys():
                        enter = input("Can't Find This Key:)\n Correct Please: ")
                    del categories[enter]
                    print(f"---{enter} Delete Done:) ---")
                elif ask == "2":
                    for x in categories:
                        print(x,end="---")
                    print()
                    enter = input("Enter Which Key: ")
                    while enter not in categories.keys():
                        enter= input(f"Can't Find {enter} In Categories List:)\n---Try Again: ")
                    print(f"---{enter} Finded---\n---{enter} Value---")
                    print("---List Key Of Value---")
                    for y in categories[enter]:
                        print(y,end=" / ")
                    print()
                    ask = input(f"{"*"*8}\nWhich One Of This Want To Delete: ")
                    while ask not in categories[enter]:
                        ask = input("Correct Your Answer Please: ")
                    del categories[enter][ask]
                    print(f"--{ask} Delete Done From {enter} Value--")    
        else:
            print(f"{"-"*15}\nCan't Remove Anything Your Category Is Empty!\nAdd Item Fisrt::)")
    elif ask == "3":
        if categories:
            choice = input(f"{"-"*8}\nThis What Can I Do For You:\n1-Change Name(key/Value)\n2-Change Amount\nEnter: ")
            #asnwer change name of key - value - change amount
            while choice not in ["1","2"]:
                choice = input("Correct Your Answer Please: ")
            if choice == "1":
                ask = input("Tell Me What Do You Want To Change:\n1-Change Name Key\n2-Change Name Value Of Key\nEnter: ")
                while ask not in ["1","2"]:
                    ask = input("Invalid! Try Again: ")
                if ask =="1":
                    for x in categories.keys():
                        print(x,end="---")
                    print()
                    enter= input("Enter Which Key Want To Change Her Name: ")
                    while enter not in categories.keys():
                        enter = input(f"Can't Find {enter} In Category Keys----\nTry Again: ")
                    new = input(f"--{enter} Keys Finded--\nEnter Your New Name Of This Key: ")
                    categories[new]=categories[enter]
                    del categories[enter]
                    print(f"---- Name Changed Successfully !\n--Old Name: {enter}\nNew Name: {new}\nChek It !!")
                elif ask == "2":
                    print("---List Of Key Value(key)")
                    for x in categories.keys():
                        print(x,end=" / ")
                    print()
                    ask= input("which one of this key want to show his value: ")
                    while ask not in categories.keys():
                        ask = input("Invalid Answer!!: ")
                    print(f"---List Value {ask}---")
                    for x in categories[ask]:
                        print(x,end=" / ")
                    print()
                    enter= input("Tell Me What Of This Want To Change The Name: ")
                    while enter not in categories[ask]:
                        enter = input("Can't Find!! Re-Enter: ")
                    new = input(f"Enter Your New Name of {enter}: ")
                    categories[ask][new]= categories[ask][enter]
                    del categories[ask][enter]
                    print(f"---- Name Changed Successfully !\n--Old Name: {enter}\nNew Name: {new}\nChek It !!") 
            elif choice == "2":
                print("--- You're Entered In Change Amount---")
                for x in categories.keys():
                    print(x,end=" / ")
                print()
                ask = input("Which One Of This Keys Want To Change Amount: ")
                while ask not in categories.keys():
                    ask = input(f"Can't Find {ask} In Category Keys\nRe-Enter Again: ") 
                if ask in categories.keys():
                    print(f"---{ask} Values---")
                    for x in categories[ask]:
                        print(x,end=" *- ")
                    print()
                enter= input("Enter Which Value Want To Change: ")
                while enter not in categories[ask]:
                    enter = input("Correct Your Answer Please: ")
                choice = input(f"{"-"*8}\n-This Is What Can Do In Amount Of Values:\n1-Add(+)\n2-Sub(-)\n{"-"*8}\nEnter Your Choice: ")
                while choice not in ["1","2"]:
                    choice = input("Re-Enter Your Answer Please: ")
                if choice == "1":
                    add = float(input(f"{"-"*8}\n{enter} Value: {categories[ask][enter]}\n{"-"*8}\nAdd In This Value: "))
                    while add <=0 :
                        add = float(input("Add Failed!!\nEnter Again: "))
                    print(f"{"-"*8}\n{add} Added Successfully !!\nCheck It!!!\n{"-"*8}")
                    categories[ask][enter]+=add
                elif choice == "2":
                    sub= float(input(f"{"-"*8}\n{enter} Value: {categories[ask][enter]}\n{"-"*8}\nSub In This Value: "))
                    while sub <= 0 or categories[ask][enter]<sub:
                        sub = float(input(f"{"-"*8}\nCan't Sub This Amount From His Value\n{"-"*8}\nEnter New: "))
                    print(f"{"-"*8}\n{sub} Subtraction Successfully !!\nCheck It!!!\n{"-"*8}")
                    categories[ask][enter]-=sub       
        else:
            print("-- Cant Edit , Add Some Item In Your List :) --")
def enter_amount(data,categories):
    if categories:
        #ns9si wch m lkey hab ydir lamount tae lvalue taeou
        for x in categories.keys():
            print(x,end="---")
        print()
        ask = input("What Key Want To Add Amount: ")
        while ask not in categories.keys():
            ask = input("Correct Your Answer Please: ")
        if ask in categories.keys():
            print("---Keys Values---")
            for y in categories[ask]:
                print(y,end=" ** ")
            print()
            enter = input("Which Value: ")
            while enter not in categories[ask]:
                enter= input(f"{enter} not in categorie key value\nEnter Again: ")
            if enter in categories[ask]:
                print("--Great--")
                amount = float(input(f"Enter Amount To Add In {enter}: "))
                #notice the user
                while amount <=0:
                    amount = float(input("Incorrect Amount\nRe-Enter Again: "))
                if amount > data["balance"]:
                    choice=input(f"---Notice !!!---\nAmount({amount}) > Balance({data["balance"]})\n1-Yes Keep It\n2-Enter Again\n-Select : ")
                    while choice not in ["1","2"]:
                        choice = input("Re-Correct Your Answer Please(1,2): ")
                    if choice =="1":
                        print("-----\nAmount Added\n-----")
                        categories[ask][enter]+=amount
                        data["total_exp"]+=amount
                        data["end_balance"]= data["balance"]-data["total_exp"]
                    elif choice == "2":
                        amount = float(input("---\nEnter New Amount: "))
                        while amount <=0 or amount > data["balance"]:
                            amount = float(input("Incoreccet Amount\nRe-Enter Again: "))
                        print("-----\nAmount Added\n-----")
                        categories[ask][enter]+=amount
                        data["total_exp"]+=amount
                        data["end_balance"]= data["balance"]-data["total_exp"]
    else:
        print(f"{"-"*15}\nCan't Add Amount  Your Category Is Empty!\nAdd Item Fisrt::)")
def final(data,categories):
    if categories:
        for x , y in data.items():
            print(x,end=" ------ ")
            print(y)
    else:
        print("----\nNo Data Entered\n----")
while True:
        choice = menu()
        if choice == "2":
            if data["month"]!="" and data["balance"]!=0:
                if categories:
                    print(f"\nYou're Entered In Category:\n{"*"*15}")
                    show_cat(categories)
                    print("*"*15)
                else:
                    print(f"{"-"*8}\nEmpty List Add new\n{"-"*8}")
            else:
                print(f"{"-"*8}\nAdd Data First !!!\n{"-"*8}")
        elif choice =="3":
            if data["month"]!="" and data["balance"]!=0:
                print(f"You're Entered In Edit Choice:\n{"*"*15}")
                edit_cat(categories)
                print("*"*15)
            else:
                print(f"{"-"*8}\nAdd Data First !!!\n{"-"*8}")
        elif choice == "1":
            print("---Data Center---") 
            log(data)
        elif choice == "4":
            if data["month"]!="" and data["balance"]!=0:
                if categories:
                    enter_amount(data,categories)
            else:
                print(f"{"-"*8}\nAdd Data First !!!\n{"-"*8}")
        elif choice =="5":
            if data["month"]!="" and data["balance"]!=0:
                print("---Final Month Result---")
                final(data,categories)
                print("----------------------")
            else:
                print(f"{"-"*8}\nAdd Data First !!!\n{"-"*8}")          
