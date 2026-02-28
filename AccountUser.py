import random as rd
class Account : 
    def __init__(self):
        self.user = ""
        self.password = ""  
        self.id= f"{rd.randint(0,100):03}"
        self.point = 0
        self.active =None
        self.balance = 0
        self.facture = {}
        self.currency = "DA"
    def __str__(self):
        cat = "Gold" if self.point >=450 else "Silver" if self.point >=150 else "Bronze"
        return f"{self.user}:{{\n'Id': {self.id}\n'Balance': {self.balance} {self.currency}\n'Password': {self.password}\n'Point': {self.point}\n'Categorie': {cat}}}"
    def deactivate(self):
        self.active = False
        print("Account Deactivated Successfully!!")
    def login(self):
        count=0
        self.user = input("Enter Your User : ")
        while len(self.user) <3 or len(self.user) > 8:
            count
            if len(self.user) < 3:
                if self.user == "":
                    self.user = input("Username Cant Be Empty\nEnter Again: ")
                else:
                    self.user = input("Username Must Be At Least 3 Characters\nEnter Again: ")
            elif len(self.user) > 8:
                self.user = input("Username Must Be At Most 8 Characters\nEnter Again: ")
            if count == 3:
                print("---Too Many Enter Try Again!!!---Sorry Your Data Lost---")
                break
        self.password = input("Enter Your Password : ")
        while len(self.password) < 3 or len(self.password) > 12:
            count+=1
            if len(self.password) < 3:
                if self.password == "":
                    self.password = input("Password Cant Be Empty\nEnter Again: ")
                else:
                    self.password = input("Password Must Be At Least 3 Characters\nEnter Again: ")
            elif len(self.password) > 12:
                self.password = input("Password Must Be At Most 12 Characters\nEnter Again: ")
            if count == 3:
                print("---Too Many Enter Try Again!!!---Sorry Your Data Lost---")
                break
        print("---Account Created Successfully!!---")
        self.active = True
        user.balance += 1500
        print("**Congratulation You Have 1500 DA In Your Account To Start Shopping!!**")
        print()
        return self.user,self.password
user = Account()


