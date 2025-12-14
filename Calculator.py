print("Welcome In My Our Calculator Program")
enter_app = input("Do You Want To Enter In My App [Yes/Y] , [No/N]: ").capitalize()
if enter_app == "Yes" or enter_app == "Y":
    print("Welcome !! \n I Can Do These Operations : \n1-Addition[+]\n2-Subtraction[-]\n3-Multiplication[*]\n4-Division[/]")
    choice_user= int(input("Please Enter Your Choice : "))
    num1= float(input("Enter Your Fisrt Number: "))
    num2 = float(input("Enter Your Second Number: "))
    if choice_user == 1 :
        print("You Choose The Addition Operator!!")
        addition = num1+num2
        print(f"Result Of {num1} + {num2} Is : {addition}")
    elif choice_user == 2 :
        print("You Choose The Subtraction Operator!! ")
        subtraction = num1 - num2
        print(f"Result Of {num1} - {num2} Is : {subtraction}")
    elif choice_user == 3 :
        print("You Choose The Multiplication Operator!! ")
        multiplication = num1 * num2
        print(f"Result Of {num1} * {num2} Is : {multiplication}")
    elif choice_user == 4 :
        print("You Choose The Division Operator!! ")
        if num2 == 0 :
            print("Mais Nta Hmar Kifh T9sm Ela 0 Win 9rit")
        else : 
            division = num1 / num2
            print(f"Result Of {num1} / {num2} Is : {division}")
    else : 
        print("Ebad Kima Nta Bghoula\nYek Kayen Mel 1 heta 4")
elif enter_app == "No" or enter_app == "N":
    print("Okey Maybe In Next Time")
else : 
    print("Ha Ktb Mlih [Yes/Y] , [No/N]\nKima Drt Meak Hrt")