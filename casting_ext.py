# exercise 1 

num1 = 25
num2 = 7

print(f"""
Add: {num1 + num2}
Sub: {num1 - num2}
Mult: {num1 * num2}
Dev: {num1 / num2}
Hole Dev: {num1 // num2}
Modulo: {num1 % num2}
Power: {num1 ** num2}
\n\n""")

# exercise 2 

balance = 1000
balance += 250
print(balance)
balance -= 100
print(balance) 
balance *= 2 
print(balance)
balance /= 4 
print(balance)


# exercise 3 

item_price = int(input("\n\nItem price: "))
discount = int(input("Discount: "))
print(f"The discount price is: {item_price / 100 * discount}")
print(f"The total price is: {item_price - item_price / 100 * discount}\n\n")

# exercise 4 

price = int(input("Price: "))
interest_rate = int(input("Interest rate: "))
print(f"The rate for one year is: {price / 100 * interest_rate}")
print(f"The total price is: {price + price / 100 * interest_rate}\n\n")

# exercise 5 

grade_1 = float(input("Enter grade 1: "))
grade_2 = float(input("Enter grade 2: "))
grade_3 = float(input("Enter grade 3: "))
grades = [grade_1,grade_2,grade_3]
print(f"The avg grade is: {sum(grades) / len(grades)}\n\n")


# exercise 6 

first_name = "David"
last_name = "Cohen"
city = "Tel Aviv"
print("Hello, my name is", first_name, last_name, "and I live in", city + ".")
print(f"Hello, my name is {first_name} {last_name} and I live in {city}.\n\n")

# exercise 7 

full_name = input("Enter your full name: ")
print(full_name)
print(len(full_name))
print(full_name.upper())
print(f"{full_name.lower()}\n\n")

# exercise 8 

sentence = input("Enter sentense: ")
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.title())

# exercise 9 

name = input("\n\nName: ")
print(name)
print(name.strip())
print(len(name))
print(len(name.strip()))

# exercise 10

sentence = "I love Java programming"
print()
print()
print(sentence.replace("Java","Python"))
print(sentence.count("love"))
print(sentence.startswith("I"))
print(sentence.endswith("programming"))


# exersise 11 

word = "Programming"
print(f"{word[0]}\n\n")
print(word[-1])
print(word[2])
print(word[:3])
print(word[-4:])
print(f"{word[::-1]}\n\n")

# exercise 12 

a = "100"
b = "25"
c = 10
d = 5.5
a = int(a)
b = float(b)
c = str(c)
d = int(b)
print(type(a),type(b),type(c),type(d))

# exercise 13

age = int(input("\n\nEnter your age: "))
print(age + 10)
"""
TypeError: Cannot add a string to an int; 
the input needs to be converted to an int.
"""

# exercise 14 

subtotal = float(input("\n\nEnter subtotal: "))
print(f"Total: {subtotal + subtotal / 100 * 18}\n\n")

# exercise 15 

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = input("Enter age: ")
month_salary =float(input("Enter monthly salary: "))
seniority = input("Seniority: ")
yearly_salary = month_salary * 12
print(f"""
====== EMPLOYEE CARD ========
Yearly salary: {yearly_salary}
Salary after 5% more: {yearly_salary + yearly_salary / 100 * 5}
Chars in name: {len(first_name) + len(last_name)} 
=============================
\n\n""")

# exercise 16 

usd_rate = 3.25
total = int(input("Enter price: "))
print(f"Tatal in Dollars: {total / usd_rate}")
print(f"Total in Euro: {total / 3.75}\n\n")

# exercise 17 

first_name = input("First name: ")
last_name = input("Last name: ")
birth = input("Birth year: ")
email = f"{first_name.lower()}.{last_name.lower()}.{birth}@gmail.com"
print(email)

# exercise 18 

sentence = input("\n\nSentence: ")
print(sentence)
print(len(sentence))
print(sentence.upper())
print(sentence.lower())
print(sentence[::-1])
print(sentence.count("a"))
print(sentence.replace(" ","-"))

# exercise 19 

cosumer_name = input("\n\nCosumer name: ")
item_name = input("Item name: ")
price = int(input("Price: "))
quantity = int(input("Quantity: "))
percent_discount = int(input("Persent discount: "))
vat = int(input("Persent vat: "))
subtotal = price * quantity
discount = subtotal / 100 * percent_discount
after_discount = subtotal - discount
print(f"""\n\n
================================
          PURCHASE INVOICE
================================

Customer: {cosumer_name}
Product: {item_name}

Unit Price: {price}
Quantity: {quantity}

Subtotal: {subtotal}
Discount: {discount}
After Discount: {after_discount}
VAT: {vat}%
VAT Amount: {after_discount / 100 * vat}

TOTAL: {after_discount + after_discount / 100 * vat}

================================
       THANK YOU FOR SHOPPING
================================

""")

