#import json
import csv


#database=[]

choise=input("""
login to login
register to reg
""")
if choise=='login':
    user=input("Enter Username :")
    pass1=input("Enter Password :")
    with open('deneme.txt') as myfile:
        if user and pass1 in myfile.read():
            print("Login Successful! :)")
        else:
            print("User doesn't exist or wrong password!")
elif choise=='reg':
    username=input("Create an Username :")
    password=input("Create a Password :")
    yey=username+" "+password
    appendfile=open('deneme.txt','a')
    appendfile.write(yey+'\n')
    appendfile.close()
    print("Registration Complated! (: ")
else:
	print("Sorry, I don't understand :(")

