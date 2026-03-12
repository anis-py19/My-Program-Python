#fisrt create data base to save our social media data
import sqlite3
from tabulate import tabulate
import time
db = sqlite3.connect("your_data.db")
cur=db.cursor()
data = []
listsocial = ["FACEBOOK","YOUTUBE","WHATSAPP","INSTAGRAM","TIKTOK","TELEGRAM","SNAPCHAT","DISCORD"]
def menu():
    print("----Our Menu----\n")
    print("1-TABLE NAME\n2-ADD COLUMN\n3-DATA ENTER")
    return input("Enter Your Choice: ")
def table_name():
    count=0
    name = input("Enter Your Social Media App Name: ").upper()
    while name not in listsocial :
        count+=1
        name = input("------Cannot Find This App Name-----\nTry Again: ")
        if count ==3:
            print()
            print("******Lot Of Tried******\nBack Again!!!!")
            break
    return name
#user/gmail-password by default by me
#insert data

