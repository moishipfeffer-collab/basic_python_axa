# def validate_number(number):
#     try:
#         int(number) 
#         return True
#     except ValueError:
#         return False


# # exercise 1
# def say_hello():
#     print("Hello World!")
# say_hello()
# say_hello()
# say_hello()

# # exercise 2
# def show_welcome():
#     print("Welcome to the system!")

# # exercise 3
# def show_menu():
#     print("""
# ===== Main Menu =====
# 1. Start
# 2. Settings
# 3. Exit

# """)

# # exercise 4
# def show_numbers():
#     for i in range(10):
#         print(i)

# # exercise 5
# def show_even_numbers():
#     for i in range(100):
#         if i % 2 == 0:
#             print(i)

# # exercise 6
# def show_stars():
#     for i in range(5):
#         for i in range(10):
#             print("*",end=" ")
#         print()

# # exercise 7
# def greet(name):
#     print(f"hello {name}")

# # exercise 8
# def show_age(age):
#     print(f"The user is {age} years old")

# # exercise 9
# def calculate_sum(num_1,num_2):
#     print(num_1 + num_2)

# # exercise 10
# def calculate_average(grade_1,grade_2,grade_3):
#     print((grade_1 + grade_2 + grade_3) / 3)

# # exercise 11
# def check_even(num):
#     if num % 2 == 0:
#         print("Evan")
#     else:
#         print("Odd")

# # exercise 12
# def check_password(password):
#     if password == "123456":
#         print("Access Granted")
#     else:
#         print("Access Denied")

# # exercise 13
# def calculate_discount(price,discount):
#     print(price - price / 100 * discount)

# # exercise 14
# def show_range(num_1,num_2):
#     for i in range(num_1+1,num_2):
#         print(i)

# # exercise 15 
# def print_rectangle(length,hight):
#     if validate_number(length) and validate_number(hight):
#         for i in range(length):
#             print("*"*hight)

# # exercise 16
# def multiply(num_1,num_2):
#     if validate_number(num_1) and validate_number(num_2):
#         return num_1 * num_2

# # exercise 17
# def get_full_name(first_name,last_name):
#     return f"{first_name} {last_name}"

# # exercise 18 
# def get_max(num_1,num_2):
#     if validate_number(num_1) and validate_number(num_2):
#         if num_1 > num_2:
#             return num_1
#         else:
#             return num_2

# # exercise 19 
# def is_positive(num):
#     if validate_number(num):
#         return int(num)>0

# # exercise 20 
# def calculate_tax(price,tax):
#     if validate_number(price) and validate_number(tax):
#         return (int(price) + int(price) / 100 * int(tax))

# # exercise 21 
# def get_grade_status(grade):
#     if validate_number(grade):
#         grade = int(grade)
#         if grade >= 90:
#             return "Excellent"
#         elif grade >= 75:
#             return "Good"
#         elif grade >= 60:
#             return "Average"
#         else:
#             return "Failed"

# # exercise 22        
# def count_digits(number):
#     if validate_number(number):
#         return len(str(number))

# # exercise 23
# def calculate_power(num,power):
#     if validate_number(num) and validate_number(power):
#         count = 0
#         for i in range(power-1):
#             count += num * num 
#         return count
#     return False

# # exercise 24 
# def print_list(numbers):
#     for n in numbers:
#         print(n)

# # exercise 25
# def get_list_sum(numbers):
#     count = 0
#     for n in numbers:
#         if validate_number(n):
#             count += int(n)
#     return count 

# # exercise 26
# def get_list_average(numbers):
#     count = 0
#     for n in numbers:
#         if validate_number(n):
#             count += int(n)
#     return count / len(numbers)

# # exercise 27
# def find_number(numbers:list,number:int):
#     for n in numbers:
#         if n == number:
#             return True
#     return False

# # exercise 28 
# def find_max(numbers):
#     gratest = 0
#     for n in numbers:
#         if n > gratest:
#             gratest = n 
#     return gratest

# # exercise 29
# def get_even_numbers(numbers):
#     evan = [num for num in numbers if num % 2 == 0]
#     return evan

# # exercise 30
# def get_long_names(names):
#     long_names = [name for name in names if len(name) > 4]
#     return long_names

# # exercise 31
# def reverse_list(my_list:list):
#     return my_list[::-1]

# # exercise 32 
# def count_occurrences(numbers,number):
#     count = 0
#     for num in numbers:
#         if num == number:
#             count += 1
#     return count 

# # exercise 33 
# def remove_duplicates(my_list:list):
#     new_list = []
#     for item in my_list:
#         if item not in new_list:
#             new_list.append(item)
#     return new_list

# # exercise 34
# def calculate_final_price(price,discount):
#     total = price - price / 100 * discount
#     if total > 500:
#         total = total - total /100 * 5
#     return total

# # exercise 35
# def check_list(numbers):
#     evan = 0
#     odd = []
#     count = 0
#     for num in numbers:
#         count += num
#         if num % 2 == 0:
#             evan += 1
#         else:
#             odd += 1
#     return count,evan,odd

# # exercise 36
# def analyze_grades(grades:list):
#     highest = grades[0]
#     lowest = grades[0]
#     total = 0
#     passed = 0
#     for grade in grades:
#         total += grade
#         if grade > highest:
#             highest = grade
#         if grade < lowest:
#             lowest = grade 
#         if grade >= 60:
#             passed += 1
#     avg = total / len(grades)
#     return avg,highest,lowest,passed

# # exercise 37 
# def validate_user(username:str,password:str):
#     return len(username.strip()) > 0 and len(password.strip()) >= 6

# # exercise 38
# def search_students(names:list,name:str):
#     for student in names:
#         if student["name"] == name:
#             return student

# # exercise 39
# def calculate_cart_total (cart:list):
#     count = 0
#     for item in cart:
#         count += item["price"]
#     return count

# # exercise 40
# def get_fibonacci(n):
#     fib_list = []
#     for i in range(n):
#         if len(fib_list) < 2:
#             fib_list.append(i)
#         else:
#             fib_list.append(fib_list[-1]+fib_list[-2])
        
#     return fib_list

# # exercise 41
# name = "David"
# def show_name():
#     name = "Moshe"
# print(name)
# show_name()
# print(name)

# # exercise 42
# counter = 10
# def increase():
# 	counter = 20
# 	print(counter)
# increase()
# print(counter)
# """
# The function cannot extend beyond its scope.
# """
# # exercise 43
# number = 9
# def add_to_num(num):
#     num += 10
#     return num
# print(number)
# add_to_num(number)
# print(number)

# # exercise 44
# numbers = [1,2,3,4,5]
# def add_number(numbers:list,num):
#     numbers.append(num)
# print(numbers)
# add_number(numbers,6)
# print(numbers)

# # exercise 45
# number_list = [1,2,3,4,5]
# def slice_list(numbers:list):
#     new_list = numbers[:3]
#     new_list.append(6)
#     return new_list

# print(number_list)
# print(slice_list(number_list)) 

# exercise 46 project
students = [{"name": "David", "age": 20, "grade": 90},
{"name": "Moshe", "age": 22, "grade": 75},
{"name": "Dana", "age": 21, "grade": 100},
{"name": "Noa", "age": 19, "grade": 55},
{"name": "Avi", "age": 23, "grade": 82}]

def show_menu():
    valid = False
    while not valid:
        choise = input("""
===== Student Management =====

1. Show all students
2. Add student
3. Search student
4. Update student grade
5. Remove student
6. Show passing students
7. Show class statistics
8. Show students above average
0. Exit

Choose: """)
        if choise in ["1","2","3","4","5","6","7","8","0"]:
            return choise
        print("Not valid choise")

def get_name():
    name = input("Name: ")
    return name
def get_grade():
    grade = int(input("Grade: "))
    return grade
def get_age():
    age = int(input("Age: "))
    return age

def show_students(students):
    if not students:
        print("no students!")
    else:
        for student in students:
            print(student)


def add_student(students:list):
    name = get_name()
    age = get_age()
    grade = get_grade()
    student = {"name":name,"age":age,"grade":grade}
    students.append(student)

def search_student(students:list, name):
    if not students:
        print("no srudents")
    else:
        for student in students:
            if student["name"] == name:
                print(student)

def update_grade(students, name, grade):
    if not students:
        print("no srudents")
    else:
        for student in students:
            if student["name"] == name:
                student["grade"] = grade 

def remove_student(students:list, name):
    if not students:
        print("no srudents")
    else:
        for student in students:
            if student["name"] == name:
                students.remove(student)

def get_passing_students(students):
    if not students:
        print("no srudents")
    else:
        passed = []
        for student in students:
            if student["grade"] >= 60:
                passed.append(student)
        return passed

def get_average(students):
    if not students:
        print("no srudents")
    else:
        total = 0
        for student in students:
            total += student["grade"]
        return total / len(students)

def get_highest_grade(students):
    if not students:
        print("no srudents")
    else:
        highest = students[0]["grade"]
        for student in students:
            if student["grade"] > highest:
                highest = student["grade"]
        return highest

def get_above_avg(students):

    avg = get_average(students)
    good = []
    for student in students:
        if student["grade"] > avg:
            good.append(student)
    for s in good:
        print(s)


def main():
    exit = False
    while not exit:
        choise = show_menu()
        if choise == "1":
            show_students(students)
        elif choise == "2":
            add_student(students)
        elif choise == "3":
            name = get_name()
            search_student(students,name)
        elif choise == "4":
            name = get_name()
            grade = get_grade()
            update_grade(students,name,grade)
        elif choise == "5":
            name = get_name()
            remove_student(students,name)
        elif choise == "6":
            print(get_passing_students(students))
        elif choise == "7":
            print(f"avg: {get_average(students)}")
            print(f"best grade: {get_highest_grade(students)}")
        elif choise == "8":
            get_above_avg(students)
        elif choise == "0":
            exit = True
main()