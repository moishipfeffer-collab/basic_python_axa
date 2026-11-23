# exercise 1

first_name = "Moishi"
last_name = "Pfeffer"
age = 26
city = "JLM"
email = "moishipfefferr@gmail.com"

print("===== User Details =====")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Email: {email}")
print("========================")

# exercise 2 

birth_year = 2000
current_year = 2026 
print(f"You are approximately {current_year - birth_year} years old.")

# exersise 3 

width = 4
height = 5 
print(f"The area of the rectangle is {width * height}")
print(f"The perimeter of the rectangle is {(width * 2) + (height * 2)}")

# exercise 4 

name = "David"
age = 25
height = 1.78
is_student = True
salary = 8500
print(type(name),type(age),type(height),type(is_student),type(salary))

# exersise 5 

user_name = input("First name: ")
user_last_name = input("Last name: ")
user_city = input("City: ")
user_age = input("Age: ")
print(f"Welcom {user_name} {user_last_name}! You live in {user_city}\nand you are {user_age} years old!")

# exercise 6 

number_1 = int(input("Numner 1: "))
number_2 = int(input("Number 2: "))
print(f"Add: {number_1 + number_2}\nSub: {number_1 - number_2}\nMult: {number_1*number_2}\nDev: {number_1 / number_2}")

# exercise 7 

item_name = input("Item name: ")
item_price = int(input("Item price: "))
quantity = int(input("Quantity: "))
print(f"""
====== Purchase Receipt ======
Product: {item_name}
Price: {item_price}
Quantity: {quantity}
Total: {item_price * quantity}
==============================

""")
# exercise 9

worker_name = input("Worker name: ")
hours = int(input("Hours: "))
salary_per_hour = int(input("Salary per hour: "))
print(f"""
====== Monthly Work Report ======
Employee Name: {worker_name}
Hourly Wage: {hours}
Total Monthly Hours: {salary_per_hour}
Total Monthly Salary: {hours * salary_per_hour}
""")

# exercise 10 

price = int(input("Total price per person: "))
tip_percent = int(input("Tip percent: "))
diners = int(input("Diners: "))
my_tip = price / 100 * tip_percent
print(f"The tip is: {my_tip}")
total_price = price + my_tip
print(f"Total price: {total_price}")
print(f"Price per person: {total_price / diners}")

# exercise 12

a = 10 
b = 20 
c = a 
a = b 
b = c 

# exercise 13

first_name = input("First name: ")
last_name = input("Last name: ")
age = input("Age: ")
educational_institution = input("Educational institution: ")
course_name = input("Course name: ")
study_months = int(input("Study months:"))
monthly_price = int(input("Monthly price: "))


print(f"""
================================
       STUDENT REGISTRATION
================================

Student: {first_name} {last_name}
Age: {age}
Institution: {educational_institution}
Course: {course_name}
Duration: {study_months} months
Monthly Price: {monthly_price}

Total Course Price: {monthly_price * study_months}

================================
    Registration completed!
================================

""")

