import mysql.connector
import pickle 

mydb=mysql.connector.connect(user='', pass='', localhost='',pass-sql='', datab='')

mycursor=mydb.cursor(buffered=True)

def Menu():
    print(">>>>>>>>>>>>>>>>")
    print("Welcome to covid-19 testing management system. Please select from one of the options below. Enter digit next to chosen option.")
    print(">>>>>>>>>>>>>>>>")
    print("1. Enter new testing centre")
    print("2. Search for testing centre in your ")
    print("     a. city")
    print("     b. state")
    print("     c. nationwide data")
    print("3. Remove testing centre")
    print("4. Edit number of testing kits available at centre")
    print("5. End")