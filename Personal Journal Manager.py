#welcome in my simple personal journal manager
#list of categories:
categories = {"Saving":{"Emergency Fund":[],"Education":[]},
                "Home Exp":{"Electricity":[],"Gas/Oil":[],"Water":[],"Phone":[],"Internet":[]},
                "Transport":{"Vehicle":[],"Auto Assurance":[],"Fuel":[],"Transport City":[]},
                "Health":{"Dentist":[],"Health Insurance":[]},
                "Daily Living":{"Barber":[],"Clothing":[],"Eat Out":[],"Gym":[]}}

def menu():
    print("1-Show Catgorie\n2-Edit Categorie")
    choice = input("Which Service Want To Enter: ")
    return choice
data = {"Month":"","balance":0,"total_exp":0,"end_balance":0}
def log(data):
    #enter the balance and the month:
    data["Month"]=input("Which Month Want To Add: ")
    data["balance"]=float(input("Enter Your Monthly Balance: "))
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
    ask = input("Enter What Service You Want:\n(add/remove/edit): ")
    while ask not in ["add","remove","edit"]:
        ask=input("Wrong Enter:)\nTry Again: ")
    if ask == "add":
        #ask category key or values
        choice = input("What You Want to Add?\nCategory Key Or Category Value: ")
        while choice not in ["Category Key","Category Value"]:
            choice = input("Wrong Enter:)\nTry Again: ")
        if choice == "Category Key":
            #add key and value:
            add = input("Enter Your New Category To Add: ")
            categories[add]={}
            #value category 
            add_val = input(f"Enter Value [item of type] Of {add}:")
            categories[add][add_val]=[]
            print(f"{"-*"*8}\nItem Added SuccessFully In Cat Items:)\n")
        elif choice == "Category Value":
            if categories:
            #ask which type catgeory to addin
                ask = input("Which Category Want To Add Item In: ")
                while ask not in categories.keys():
                    ask = input(f"{ask} Not In Category List!!\n Enter Again: ")
                add_val = input(f"Enter New Value in {ask}: ")
                categories[ask][add_val]=[]
            else:
                 print("-- Cant Add Value , No Keys In List\n---Add  New Items:) --")        
    elif ask == "remove":
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
    elif ask == "edit":
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
                    ask= input("which one of this kye want to show his value: ")
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
                           
        else:
            print("-- Cant Edit , Add Some Item In Your List :) --")
        
    return categories

while True:
    choice = menu()
    if choice == "1":
        if categories:
            print(f"\nYou're Entered In Category:\n{"*"*15}")
            show_cat(categories)
            print("*"*15)
        else:
            print(f"{"-"*8}\nEmpty List Add new\n{"-"*8}")
    elif choice =="2":
        print(f"You're Entered In Edit Choice:\n{"*"*15}")
        edit_cat(categories)
        print("*"*15) 

