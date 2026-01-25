modules = {"minhajiya":{"coef":2},
           "compta":{"coef":3},
           "macro":{"coef":2},
           "finance":{"coef":2},
           "managemnt":{"coef":2},
           "stat":{"coef":2},
           "math":{"coef":2},
           "eco-na9di":{"coef":1},
           "info":{"coef":1}
           }
def enter_data(modules):
    for module,data in modules.items():
        print(f"MODULE NAME: {module}:----------")
        enter_cour = float(input(f"Enter {module} COUR Grade: "))
        if module in  ["eco-na9di" ,"info"]:
            data["td"]= None
        else: 
            enter_td = float(input(f"Enter {module} TD Grade: "))
            data["td"]=enter_td
        data["cour"]=enter_cour
    return modules
def calc(modules):
    total = 0
    for data in modules.values():
        td= data["td"]
        cour = data["cour"]
        coef = data["coef"]
        if td is None:
            average = coef * cour
        else:
            average = (td*0.4+cour*0.6)*coef
        total += average
        sum_coef = sum(data["coef"]for data in modules.values())
    return total/sum_coef
data_enter = enter_data(modules)
result = calc(modules)
print(result)