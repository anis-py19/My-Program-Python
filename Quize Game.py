print("Hello Wolrd Is My Fisrt Practice In Python")
print("It's a Simple Quiz Game")
print("-------------------------------------------")
score = 0 
print(f"Your Score Now : {score}")
#answer1
print("Question 1 : \n-What Is The Capital of France : \n1-Berlin\n2-Madrid\n3-Paris ")
answer1 = int(input("Enter Your Answer Please (Only Number) : "))
if answer1 == 3 :
    score+=1
    print("Good Your Are Genius !!!")
    print(f"Score Now : {score}")
else : 
    answer1 != 3
    print("Try Again !")
#answer2
print("Question 2 : What is the largest ocean on Earth? \n1-Atlantic Ocean\n2-Indian Ocean\n3-Pacific Ocean ")    
answer2= int(input("What Is Your Answer Please ? : "))
if answer2 == 3 :
    score+=2
    print("oooh Great You Chose The Right Answer ")
    print(f"Score : {score}")
else : 
    answer2 != 3 
    print("Its Easy Why You Failed ?")
    print("Try Again")
#answer3 
print("Question 3 : What is the capital of Australia? \n1-Sydney\n2-Melbourne\n3-Brisbane\n4-NO One Is Correct")
answer3= int(input("Enter Your Answer : "))
if answer3 == 1 or answer3 == 2 or answer3 == 3 :
    print("OOps ! You have must To Search HAHA!!")
elif answer3 ==4 :
    score+=4 
    print("Greaat !! ")
    print(f"Your Score : {score}")
    answer = input("Enter Your Answer (Correct Word) : ").capitalize()
    if answer == "Canberra" : 
        print("Its Correct ! See You In Next Quiz Game")
    else : 
        answer != "Canberra"
        print("Okey , Search In Google To Memorise In Your Mind !!!")
print("----------------------------------------------------------")        
print(f"Your Total Score : {score}")   