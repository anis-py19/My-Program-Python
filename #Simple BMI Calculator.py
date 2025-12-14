#Simple BMI Calculator 
height = {}
weight = {}
BMI = {}
#Add 4 Items To Calculate [Name : Height : Weight ]
while len(height) !=4 and len(weight) != 4  :
    enter_name= input("Enter Your Name : ")
    enter_height= int(input("Enter Your Height(Tol) : "))
    height[enter_name]= enter_height
    enter_weight = int(input("Please Add Your Weight (Mizan): "))
    weight[enter_name]= enter_weight
#change in CM 
for cm in height :
    height[cm]= height[cm]/100
#get the BMI (weight/height)
for k in height :
    BMI[k] = weight[k]/(height[k]**2)
#add empty note to classify 
note = ""
for person in BMI :
    if BMI[person] <18 :
        note = "UnerWeight(Na9s Mizan)"
    elif BMI[person] >=18 and BMI[person]<25 :
        note = "Normal"
    elif BMI[person] >=25 and BMI[person] <30 :
        note = "OverWeight(Rak Zayd Bezaf)"
    print(f"{person} : {note}")