# exercise 1 
numbers = (10,20,30,40,50)
print(numbers)
print(numbers[0],numbers[-1])
print(len(numbers))
print(numbers[2])

# exercise 2
names = ("moishi","rachel","noa","tali","natan")
for name in names:
    print(name)

# exercise 3
numbers = (10,20,30,40,50)
print(numbers[:3])
print(numbers[-3:])
print(numbers[::-1])

# exercise 4 
item = ("table",300,10,"furniture")

# exercise 5
print(item[0])
print(item[1])
print(item[2])
print(item[3])

# exercise 6
numbers = (10,20,30,40,50)
count = 0
evan = 0
gratest = numbers[0]
for num in numbers:
    count += num
    if num > gratest:
        gratest = num 
    if num % 2 == 0:
        evan += 1
print(f"Total numbers: {count}, highest: {gratest}, Evan numbers: {evan}")

# exercise 7
products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
first_3 = products[:3]
last_2 = products[-2:]
new_products = first_3 + last_2
print(new_products)

# exercise 7 (dict)
student = {"name":"moishi","age":26,"grade":100,"city":"JLM"}
for key,value in student.items():
    print(value)

# exercise 8
car = {"brand":"tesla","modal":"Y","year":2024,"price":15000}
car["price"] = 10000
car["year"] = 2025
car["color"] = "blue"
print(car)

# exercise 9
salaries = {    "David": 12000,    "Moshe": 15000,    "Dana": 13500}
for key,value in salaries.items():
    print(value)
salaries["david"] = 1000000
salaries["natan"] = 290578
print(salaries)

# exercise 10
items = {"table":3000,"mouse":500}
user_item = input("Enter item: ")
if user_item in items:
    print(items[user_item])
else:
    print("Not found")

# exercise 11
grades = {"mosihi":100,"rachel":90,"tali":89,"natan":93,"noa":99}
for name,grade in grades.items():
    print(f"Student: {name} | Grade: {grade}")

# exercise 12
grades = {    "David": 90,    "Moshe": 75,    "Dana": 100,    "Noa": 55,    "Avi": 82}
count = 0
highest = 0
highest_name = None
faild = 0
exelent = []
for name,grade in grades.items():
    count += grade
    if grade >= 80:
        exelent.append(name)
    if grade > highest:
        highest = grade
        highest_name = name
    if grade < 60:
        faild += 1
print(f"Exelent: {exelent}\nAvg: {count / len(grades)}\nBest: {highest_name}\nFaild: {faild}")

# exercise 13
items = {"table":3000,"mouse":500}
user_item = input("Enter item: ")
items[user_item] = int(input("Enter price: "))
print(items)

# exercise 14
students = [{"name": "David", "age": 20, "grade": 90}, 
{"name": "Moshe", "age": 22, "grade": 75},
{"name": "Dana", "age": 21, "grade": 100},
{"name": "Noa", "age": 19, "grade": 55},
{"name": "Avi", "age": 23, "grade": 82}]
exelent = []
total = 0
for student in students:
    print(student["name"])
    print(student["grade"])
    total += student["grade"]
    if student["grade"] > 80:
        exelent.append(student["name"])
avg = total / len(students)
print(f"Best: {exelent}, Avg: {avg}")

# exercise 15
student = {"name":"moishi","age":26,"grade":100}
students.append(student)
students[0]["grade"] = 100
for student in students:
    if student["name"] == "moishi":
        students.remove(student)
print(students)

# exercise 16
classroom = {"Class A": ["David", "Moshe", "Dana"],
"Class B": ["Noa", "Avi", "Michael"],
"Class C": ["Daniel", "Shir", "Yossi"]}
for key,value in classroom.items():
    print(key)
print(classroom["Class A"])
classroom["Class B"].append("moishi")
classroom["Class C"].remove("Shir")
for kye,value in classroom.items():
    print(len(value))

# exercise 17
products = { "Laptop": {"price": 4500,"stock": 10},
"Mouse": {"price": 80,"stock": 50},
"Keyboard": {"price": 150, "stock": 20 }}
for product in products.values():
    print(product["price"])
    print(product["stock"])
products["Laptop"]["price"] = 5000
products["table"] = {"price":800,"stock":30}
for product,data in products.items():
    if data["price"] > 100:
        print(product)

# exercise 18
employees = [("David", "Development", 15000),("Moshe", "Marketing", 12000),
("Dana", "Development", 18000),    ("Noa", "HR", 11000)]
for employee in employees:
    print(employee[0])
highest = 0
highest_employee = None
total = 0
for employee in employees:
    if employee[1] == "Development":
        print(employee[0])
    if employee[2] > highest:
        highest = employee[2]
        highest_employee = employee[0]
    total += employee[2]
avg = total / len(employees)
print(f"Highest: {highest_employee}\nAvg: {avg}")

# exercise 19
inventory = {"Laptop": 10,"Mouse": 50,"Keyboard": 20}
item = input("Enter item: ")
quantity = int(input("Enter quantity: "))
if item not in inventory:
    print("Item not found\n")
else:
    if quantity > inventory[item]:
        print("There isn't enough")
    else:
        inventory[item] -= quantity
print(inventory)

# exercise 20
votes = {    "David": 0,    "Moshe": 0,    "Dana": 0}
exit = False
while not exit: 
    choise = input("1. Enter name:\n2. stop\nchoose: ")
    if choise == "1":
        name = input("Enter name: ")
        votes[name] += 1
    elif choise == "2":
        exit = True
print(votes)
gratest = 0
best = None
for name in votes:
    if votes[name] > gratest:
        gratest = votes[name]
        best = name
print(f"winner: {best}")

# exercise 21

names = {"moishi":123344545,"rachel":349384590}
while True:
    choise = input("""
1. Add a contact
2. Search a contact
3. Update a phone number
4. Delete a contact
5. View contacts
6. Exit

choose: """)
    if choise == "1":
        names[input("Name: ")] = input("number: ")
    elif choise == "2":
        name = input("Name: ")
        if name in names:
            print(names[name])
        else:
            print("Not found")
    elif choise == "3":
        name = input("Name: ")
        if name in names:
            names[name] = input("Number: ")
        else:
            print("Not found")
    elif choise == "4":
        name = input("Name: ")
        if name in names:
            del names[name]
        else:
            print("Not found")
    elif choise == "5":
        print(names)
    elif choise == "6":
        break

# exrcise 22 project
products = [{"name": "Laptop", "price": 4500, "stock": 10},
{"name": "Mouse", "price": 80, "stock": 50},
{"name": "Keyboard", "price": 150, "stock": 20},
{"name": "Screen", "price": 900, "stock": 15}]
while True:
    choise = input("""
===== Store Management =====

1. Show all products
2. Add product
3. Search product
4. Update product price
5. Update product stock
6. Sell product
7. Show products by price
8. Show products with low stock
9. Show total inventory value
0. Exit

Choose: """)
    if choise == "1":
        for product in products:
            print(product)
    elif choise == "2":
        name = input("Name: ")
        price = int(input("Price: "))
        stock = int(input("Stock: "))
        product = {"name":name,"price":price,"stock":stock}
        products.append(product)
    elif choise == "3":
        name = input("Name: ")
        for product in products:
            if product["name"] == name:
                print(product)
    elif choise == "4":
        name = input("Name: ")
        for product in products:
            if product["name"] == name:
                product["price"] = int(input("Price: "))
    elif choise == "5":
        name = input("Name: ")
        for product in products:
            if product["name"] == name:
                product["stock"] = int(input("Srock: "))
    elif choise == "6":
        name = input("Name: ")
        for product in products:
            if product["name"] == name:
                quantity = int(input("Quantity: "))
                if quantity <= product["stock"]:
                    product["stock"] -= quantity
    elif choise == "7":
        price = int(input("Price: "))
        for product in products:
            if product["price"] >= price:
                print(product)
    elif choise == "8":
        for product in products:
            if product["stock"] < 10:
                print(product)
    elif choise == "9":
        count = 0
        for product in products:
            count += product["price"] * product["stock"]
        print(count)
    elif choise == "0":
        break