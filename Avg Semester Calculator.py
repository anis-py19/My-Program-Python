#module TD-Cour 
td_module = {"comptabilite": 0 ,
             "finance publique": 0,
              "intro management": 0 ,
              "macro":0,
              "math": 0 ,
              "stat": 0 ,
              "informatique":0}
cour_module = {"comptabilite": 0 ,
             "finance publique": 0,
              "intro management": 0 ,
              "macro":0,
              "math": 0 ,
              "stat": 0 ,
              "informatique":0}
coef = {
    "comptabilite": 3,
    "finance publique": 2,
    "intro management": 2,
    "macro": 2,
    "math": 3,
    "stat": 2,
    "informatique": 2,
    "minhajiya": 2,
    "economie monetaire": 1}

#minhajiya- economie monetaire No TD coef *1 
no_td= {"minhajiya":0,
        "economie monetaire":0}
#enter TD-Cour Grade
print("-----TD Module-----")
for td in td_module :
    enter_td = float(input(f"Enter Your {td} Grade : "))
    while enter_td <0 or enter_td >20 :
        enter_td= float(input(f"Please Re-Enter Your {td} GRADE !! : "))
    td_module[td] += enter_td
print("-----Cour Module-----")
for cour in cour_module:
    enter_cour  = float(input(f"Enter Your {cour} Grade: "))
    while enter_cour <0 or enter_cour > 20:
        enter_cour= float(input(f"Please Re-enter Your {cour} Grade!!: "))
    cour_module[cour]+= enter_cour
print("-----No TD Module-----")
for cour2 in no_td :
    enter_cour2  = float(input(f"Enter Your {cour2} Grade: "))
    while enter_cour2 <0 or enter_cour2 > 20:
        enter_cour2= float(input(f"Please Re-enter Your {cour2} Grade!!: "))
    no_td[cour2]+= enter_cour2
#TD Coef 0.4 - Cour coef 0.6 
for coef1 in td_module:
    td_module[coef1] = round(td_module[coef1]*0.4,2)
for coef2 in cour_module :
    cour_module[coef2] = round(cour_module[coef2]*0.6,2)
for coef3 in no_td:
    no_td[coef3] = no_td[coef3]*1
#final grade to calculate the avg
final_grade = {}
for avg in td_module and cour_module  :
    final_grade[avg]= td_module[avg]+cour_module[avg]
for avg2 in no_td :
     final_grade[avg2]= no_td[avg2]
#calculate the avg
total = 0 
total_coef = 0
for y in final_grade :
    total += final_grade[y]*coef[y]
    total_coef = 17
moyenne_general = round(total / total_coef)
if moyenne_general >=10 :
    print(f"successfully!!\nYour Avg In This Semester : {moyenne_general}")
else :
    print("Roh T9wd Tjri L rattrapage")
