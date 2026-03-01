class Trader :
    def __init__(self,capital):
        self.capital = capital
        self.products = {"Luxe15": {"Price": 1500, "Stock": 15},
                         "Luxe20": {"Price": 2000, "Stock": 5},
                         "Luxe25": {"Price": 2500, "Stock": 2}}
        self.profit = 0
        self.sells = {}
        self.currency = "DA"
        self.password = "ADMIN"
    def __str__(self):
        return f"Capital: {self.capital} {self.currency}\nProducts: {self.products}\nProfit: {self.profit}"
    def add_product(self):
        name = input("Name Of Product: ")
        try :
            count = 0
            price = float(input(f"Price Of {name}: "))
            while price <= 0 or price > self.capital :
                count+=1
                if price <=0:
                    price = float(input("--Price Must BE postive--\nEnter Again: "))
                elif price > self.capital :
                    price = float(input(f"--Price Of {name} Must Be Less Than Your Capital\n--Enter Again: "))
                if count == 3:
                    return "---Too Many Enter Try Again!!!---Sorry Your Data Lost---"
                    
            stock = int(input(f"Stock Of {name}: "))
            self.products[name] = {"Price": price , "Stock": stock}
            print("Product Added Successfully!!")
        except ValueError:
            print("Error Try_Again!!")
    def modify_product(self):
        if self.products: 
            name = input("Name Of Product: ")
            asq = input(f"---What Do You Want To Modify In {name}---\n1-Price\n2-Stock\n--Enter Your Choice: ")
            count = 0
            while asq not in ["1","2"]:
                count +=1
                asq = input("---Coorect Your Choice Please---\n---: ")
                if count == 3 :
                    return "---Too Many Enter Try Again!!!---Sorry Your Data Lost---"
            if asq == "1":
                try :
                    price = float(input(f"New Price Of {name}: "))
                    self.products[name]["Price"]= price
                    print("---Price Modified Successfully---\nChek It........")
                except ValueError:
                    print("Error Enter!!!!")
            elif asq == "2":
                try :
                    stock = int(input(f"New Stock Of {name}: "))
                    if stock <=0 :
                        print(f"---{name} Is Out Of Stock---")
                    else:
                        self.products[name]["Stock"]= stock
                        print("---Stock Modified Successfully---\nChek It........")
                except ValueError:
                    print("Cant Modify Stock Enter Try Again!!") 
        else:
            print("No Products To Modify!!\n---Add Product Fisrt---")
    def show_products(self):
        if self.products:
            print("--Products List--")
            for name, info in self.products.items():
                print(name,end=" : ")
                print(info)
        else:
            print("No Product To Show !!\n---Add Product First---")
    def modify_capital(self,capital):
        self.capital = capital
        print(f"Capital Modified Successfully!!\nYour New Capital Is {self.capital} {self.currency}")
    def show_sells(self):
        if self.sells:
            print("--Sells List--")
            for name, quantity in self.sells.items():
                print(f"{name} : {quantity}")
        else:
            print("No Sells To Show!!\n---Take Order First---")
    def show_stock(self):
        if self.products:
            print("---Stock List---")
            for name , info in self.products.items():
                if info["Stock"] <=0:
                    print(f"{name} : Out Of Stock")
                else:
                    print(f"{name} : {info['Stock']} in Stock")
        else:
            print("---NO Product To Show!!---")
trader = Trader(10000)