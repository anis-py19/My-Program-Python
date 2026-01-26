#register to continue using the app 
def resgister_user():
    data = {}
    print("Welcome In My Simple To-Do APP----")
    username = input("Please Enter Your Username: ")
    while len(username) > 8 :
        username = input("Re-Enter Your Username 8 Charchters: ")
    password = input(f"{username}: Enter Password: ")
    while len(password) > 8 :
        password = input("Re-Enter Your Password 8 Charchters: ")
    confirm_password = input("Confirm Your Password: ")
    while password != confirm_password:
        confirm_password = input("Password Not Match, Confirm Your Password Again: ")
    data[username] = {"password": password, "tasks": {}}
    print("Registered Successfuly In This Program")
    return data
def login_user(data):
    print("Welcome Back!----")
    enter_username = input("Enter Your Username: ")
    enter_password = input("Enter Your Password: ")
    while enter_username not in data :
        enter_username= input("Username Not Found , Try Again : ")
    while data[enter_username]["password"] != enter_password:
        enter_password = input("Incorrect Password!!!: ")
    print("Login Successfuly", end=" ")
    print(f"Welcome Back {enter_username}!")
    return enter_username
def menu(data,enter_username):
    while True: 
        print("Menu:-----------\n1-Add Task: \n2-View Tasks: \n3-Delete task: \n4-Quit: ")
        choice = int(input("Enter Your Choice: "))
        while choice >4 or choice <1:
            choice = int(input("Invalid Choice , Try Again(1-4): "))
        if choice == 1 :
            #ask how many task to Add :
            ask = int(input(f"Please {enter_username},How Many Tasks You Want To Add: "))
            for i in range(ask):
                task_enter = input(f"Enter Your Task {i+1}: ")
                data[enter_username]["tasks"][i+1] = task_enter
            print("Task Added Successfuly")
        if choice == 2:
            while len(data[enter_username]["tasks"]) == 0:
                print("You Have NO Task Recently , Add Some Task !!!")
                ask = int(input(f"Please {enter_username},How Many Tasks You Want To Add: "))
                for i in range(ask):
                    task_enter = input(f"Enter Your Task {i+1}: ")
                    data[enter_username]["tasks"][i+1] = task_enter
            print(f"{enter_username}'s Tasks: ")
            for name, task in data[enter_username]["tasks"].items():
                print(f"{name} - {task}")
        if choice == 3 :
            #show teh task and which one want to delete
            print(f"You Have {len(data[enter_username]['tasks'])} Tasks")
            for name , task in data[enter_username]["tasks"].items():
                print(f"{name} - {task}")
            delete = input("Enter The Task You Want To Delete: ")
            while delete not in data[enter_username]["tasks"].values():
                delete= input("Task Not Found Try Again:")
            for key , values in data[enter_username]["tasks"].items():
                if values == delete:
                    del data[enter_username]["tasks"][key]
                    print("Task Deleted Successfuly")
                    break
        if choice == 4 :
            print("Thanks For Using My Simple Program Good Bye:)")
            break
data = resgister_user()
enter_username = login_user(data)
menu(data,enter_username)   