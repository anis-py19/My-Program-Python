#enter code to calculate the avg of module test
#first we have to take input from user "name and value of two test"
#we applied this in 3 person 
grade = {}
while len(grade) != 3 :
    for x in range(1,4,1):
        #enter name and asked [two test - test1 only - test2 only]
        enter_name = input(f"Enter Name Of Person {x}: ")
        asked1 = input("Please Tell Me what you Passed: ")
        while asked1 != "two test" and asked1 != "test1 only" and asked1 != "test2 only":
            asked1 = input("Please Re-Enter Correctly!!\nIm Pass: ")
        if asked1 =="two test":
            enter_test1 = int(input(f"Enter {enter_name} Test Grade:\ntest1: "))
            enter_test2 = int(input(f"test2: "))
            grade[enter_name]= {"test1":enter_test1,"test2":enter_test2}
        elif asked1 == "test1 only":
            enter_test1 = int(input(f"Enter {enter_name} Test1 Grade: "))
            grade[enter_name]={"test1":enter_test1}
        elif asked1 == "test2 only":
            enter_test2 = int(input(f"Enter {enter_name} Test2 Module: "))
            grade[enter_name]= {"test2": enter_test2}
    #key : name values : {test1 , test2} = garde items
    #calculate the avg now 
    for name , value in grade.items() :
        #hna name rah ydir loop ela keys li houma name
        #w value ela {}li fihm test1 w test2  
        #wki ndir b get rah yjibli l9ima wida mkch ydir 0
        test1 = value.get("test1",0)
        test2 = value.get("test2",0)
        avg= (test1+test2)/2
        print(f"{name} Avergae Is : {avg}")