import os
def write_title(number):
    print(f"""
********** EXSERCISE {number} **********
---------------------------------\n
""")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_enter():
    input("enter to continue: ")

clear_terminal()
write_title(1)
age = int(input("Enter your age: "))
if age >= 18:
    print("\nAdult\n\n")
else:
    print("\nMinor\n\n")
get_enter()
clear_terminal()
write_title(2)
number = int(input("Enter a number: "))
if number > 0:
    print("\nPositive\n\n")
elif number < 0:
    print("\nNegative\n\n")
else:
    print("\nZero\n\n")
get_enter()
clear_terminal()
write_title(3)
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("\nEven\n\n")
else:
    print("\nOdd\n\n")
get_enter()
clear_terminal()
write_title(4)
number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter another number: "))
if number_1 > number_2:
    print(f"\nThe big number is {number_1}\n\n")
elif number_1 < number_2:
    print(f"\nThe big number is {number_2}\n\n")
else:
    print(f"\nBoth numbers are the same\n\n")
get_enter()
clear_terminal()
write_title(5)
password = "Python123"
user_password = input("Enter password: ")
if user_password == password:
    print("\nAccess Granted\n\n")
else:
    print("\nAccess Denied\n\n")
get_enter()
clear_terminal()
write_title(6)
number = int(input("Enter a number: "))
if 1 <= number <= 10:
    print("\nBetween 1-10\n\n")
elif 50 >= number >= 11:
    print("\nBetween 11-50\n\n")
elif 100 >= number >= 51:
    print("\nBetween 51-100\n\n")
else:
    print("\nWow! this is a big number\n\n")
get_enter()
clear_terminal()
write_title(7)
grade = int(input("\nEnter grade (0-100): "))
if not 100 >= grade >= 0:
    print("\nInvalid Grade\n\n")
elif grade >= 90:
    print("\nExcellent\n\n")
elif grade >= 80:
    print("\nVery Good\n\n")
elif grade >= 70:
    print("\nGood\n\n")
elif grade >= 60:
    print("\nPassed\n\n")
else:
    print("\nFailed\n\n")
get_enter()
clear_terminal()
write_title(8)
correct_username = "admin"
correct_password = "123456"
name = input("Enter uaername: ")
password = input("Enter password: ")
if name == correct_username and password == correct_password:
    print("\nLogin Successful\n\n")
elif password != correct_password:
    print("\nWrong Password\n")
if name != correct_username:
    print("\nUnknown User\n")
get_enter()
clear_terminal()
write_title(9)
age = int(input("\nAge: "))
price = int(input("\nPrice: "))
if age > 60:
    print(f"Total price: {price - price / 100 * 20}\n\n")
elif age < 18:
    print(f"Total price: {price - price / 100 * 10}\n\n")
else:
    print(f"Total price: {price}\n\n")
get_enter()
clear_terminal()
write_title(10)
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("\nThe number can be devide by 3 and 5\n\n")
elif number % 3 == 0:
    print("\nThe number can be devide by 3\n\n")
elif number % 5 == 0:
    print("\nThe number can be devide by 5\n\n")
else:
    print("\nThe number can not be divide by 3 or by 5\n\n")
get_enter()
clear_terminal()
write_title(11)    
age = int(input("Age: "))
if 15 < age < 18:
    with_adult = input("With adult? ")
    if with_adult.lower() == "yes":
        with_adult = True
    else:
        with_adult = False
    if with_adult == True:
        print("\nCan come in!\n\n")
    else:
        print("\ncan not acces\n\n")
elif age > 18:
    print("\nCan come in!\n\n")
else:
    print("\ncan not acces\n\n")
get_enter()
clear_terminal()
write_title(12)
avg_grade = int(input("\nEnter avg grade: "))
monthly_income = int(input("\nEnter monthly income: "))
if avg_grade > 90 or avg_grade > 85 and monthly_income < 5000:
    print("\nEligible for a scholarship\n\n")
else:
    print("\nNot eligible\n\n")
get_enter()
clear_terminal()
write_title(13)
cottoct_name = "moishi"
correct_password = "1234"
active = True
name = input("Name: ")
password = input("Password: ")
if name == correct_username and password == correct_password and active:
    print("\nOK, can acces\n\n")
else:
    print("\nCan not acces\n\n")
get_enter()
clear_terminal()
write_title(14)
number = int(input("Enter a number: "))
if number >= 20 and number <= 80 or not 20 > number > 80:
    print("\nOK\n\n")
get_enter()
clear_terminal()
write_title(15)
balance = 5000
amount = int(input("\nEnter amount to withdraw: "))
if amount > 0:
    if amount <= balance:
        print(f"\nOK\nyour new balance: {balance - amount}")
    else:
        print("\nIt is not possible to withdraw an amount exceeding the remaining balance.\n\n")
else:
    print("\nThe withrow must be posirive\n")
get_enter()
clear_terminal()
write_title(16)
boy = 25 
lad = 35 
adolt = 50
age = int(input("\nEnter age: "))
membership = input("Do you have a membership card? ")
if age <= 12:
    price = boy
elif age <= 18:
    price = lad
else:
    price = adolt
if membership.lower() == "yes":
       print(f"\nThe price is: {price - price/100*10}")
else:
    print(f"\nThe price is: {price}")
get_enter()
clear_terminal()
write_title(17)
age = int(input("\nEnter age: "))
monthly_income = int(input("\nEnter monthly income: "))
seniority = int(input("Senyority: "))
if age >= 21 and monthly_income >= 7000 and seniority >= 1:
    print("\nEligible for a loan\n\n")
else:
    print("\nNot eligible for a loan\n\n")
get_enter()
clear_terminal()
write_title(18)
vehicle_type = input("Vehicle type: ")
hours = float(input("Parking Hours: "))
if vehicle_type.lower() == "motorcycle":
    price = 10 
elif vehicle_type.lower() == "commercial vehicle":
    price = 20 
elif vehicle_type.lower() == "private vehicle":
    price = 30 
if hours < 1:
    print(f"\nTotal price is: {price}\n\n")
elif hours < 5:
    print(f"\nTotal price is: {price - price/100*10}\n\n")
else:
    print(f"\nTotal price is: {price - price/100*15}\n\n")

get_enter()
clear_terminal()
write_title(19)
number_1 = int(input("number 1: "))
number_2 = int(input("number 2: "))
operation = input("operation: ")
if operation == "+":
    print(f"\n{number_1 + number_2}\n\n")
elif operation == "-":
    print(f"\n{number_1 - number_2}\n\n")
elif operation == "*":
    print(f"\n{number_1 * number_2}\n\n")
elif operation == "/":
    if number_2 == 0:
        print("\nCan not divide by zero!\n\n")
    else:
        print(f"\n{number_1 / number_2}\n\n")

get_enter()
clear_terminal()
write_title(20)
year = int(input("Year: "))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("\nIt’s a leap year!\n\n")
else:
    print("\nNot a leap year\n\n")

get_enter()
clear_terminal()
write_title(21)
hourly_wage = 50
hours = int(input("Hours: "))
addition_hours = hourly_wage - 182 
add = 0 
add_more = 0
if 0 < addition_hours < 2:
    add = addition_hours * hourly_wage / 100 * 125
elif addition_hours > 2:
    add_more = (addition_hours - 2) * hourly_wage / 100 * 150
print(f"\nTotal salary: {hourly_wage * hours + add + add_more}\n\n")
get_enter()
clear_terminal()
write_title("22-PROJECT")
age = int(input("Age: "))
price = int(input("Price: "))
item_open = input("Item open: ")
bying_paper = input("Bying paper: ")
valid = True
if bying_paper.lower() == "no":
    print("\nCan not give back, The bying paper dose not exist\n")
    valid = False
if item_open.lower() == "yes":
    print("Can not give back, The item wase open\n")
    valid = False
if price <= 0:
    print("The price must be grater then zero\n")
    valid = False
if valid ==  True:
    member = input("Member: ")
    if member.lower() == "yes":
        print("Can return till after 30 days\n")
    else:
        print("Can return till 14 days\n")