import os
def write_title(number):
    print(f"""
********** EXSERCISE {number} **********
---------------------------------\n
""")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_enter():
    input("\nenter to continue: ")
clear_terminal()
write_title(1)
count = 1
while count <= 10:
    print(count)
    count += 1
get_enter()
clear_terminal()
write_title(2)
count = 10
while count >= 1:
    print(count)
    count -= 1
print("START\n")
get_enter()
clear_terminal()
write_title(3)
count == 1
while count <= 50:
    if count % 2 == 0:
        print(count)
    count += 1
get_enter()
clear_terminal()
write_title(4)
number = int(input("Number: "))
mult = number
while mult <= number * 5:
    print(mult)
    mult += number
get_enter()
clear_terminal()
write_title(5)
num = 0
for i in range(101):
    num += i
print(num)
get_enter()
clear_terminal()
write_title(6)
valid = False
while not valid:
    password = input("Password: ")
    if password == "Python123":
        valid = True
        print("Welcome!")
get_enter()
clear_terminal()
write_title(7)
secret_number = 27
valid = False
while not valid:
    number = int(input("Guess the number: "))
    if number == secret_number:
        valid = True
get_enter()
clear_terminal()
write_title(8)
total = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    total += number
print(total)
get_enter()
clear_terminal()
write_title(9)
count = 0
total = 0
while True:
    grade = int(input("Grade: "))
    if grade == 999:
        break
    count += 1
    total += grade
avg = total/count 
print(f"\n{count} grades were entered; the total sum is {total}, and the average is {avg}.")
get_enter()
clear_terminal()
write_title(10)
count = 0
total = 0
while True:
    number = int(input("Number: "))
    if number < 0:
        break
    count += 1
    total += number
print(f"\n{count} numbers were entered; the total sum is {total}.")
get_enter()
clear_terminal()
write_title(11)
number = int(input("Enter number: "))
count = 0
for i in range(10):
    count += 1
    print(f"{number} x {count} = {number * count}")
get_enter()
clear_terminal()
write_title(12)
number = int(input("Number: "))
count = 0
while number > 0:
    number //= 10
    count += 1
print(f"Output: {count} digits")
get_enter()
clear_terminal()
write_title(13)
number = int(input("Number: "))
count = 0
while number > 0:
    num = number % 10
    number //= 10
    count *= 10 
    count += num
print(f"Output: {count}")
get_enter()
clear_terminal()
write_title(14)
number = int(input("Number: "))
count = 2
prime = True
for i in range(2,number**0.5):
    if number % i == 0:
        print("\nNot a prime number\n")
        prime = False
        break
if prime:
    print("\nprime number\n")
get_enter()
clear_terminal()
write_title(15)
balance = 5000
while True:
    choise = input(f"""
======= ATM ======
1. Check balance
2. Deposit 
3. Withdraw 
4. Exit
Chooose: """)
    if choise == "1":
        print(f"Balance: {balance}\n")
    elif choise == "2":
        number = int(input("Number: "))
        balance += number
    elif choise == "3":
        number = int(input("Number: "))
        if balance > number:
            balance -= number
    elif choise == "4":
        break
    else:
        print("Not valid choise")
get_enter()
clear_terminal()
write_title(16)
count = 1 
while True:
    if count > 15:
        break
    print(count)
    count += 1 
get_enter()
clear_terminal()
write_title(17)
count = 1 
while True:
    if count == 30:
        break
    elif count % 3 == 0:
        continue
    print(count)
get_enter()
clear_terminal()
write_title(18)
while True:
    number = int(input("Number: "))
    if number == 100:
        print("Succesfful")
        break
get_enter()
clear_terminal()
write_title(19)
for i in range(20):
    print(i+1)
get_enter()
clear_terminal()
write_title(20)
for i in range(1,101,5):
    print(i)
get_enter()
clear_terminal()
write_title(21)
count = 0
for i in range(100):
    count += i+1
print(count)
get_enter()
clear_terminal()
write_title(22)
number = int(input("Number: "))
for i in range(10):
    print(number * (i+1))
get_enter()
clear_terminal()
write_title(23)
number_1 = int(input("Start: "))
number_2 = int(input("End: "))
count = 0
for i in range(number_1,number_2+1):
    count += i
print(f"Result: {count}")
get_enter()
clear_terminal()
write_title(24)
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
get_enter()
clear_terminal()
write_title(25)
columns = int(input("Columns: "))
rows = int(input("Rows: "))
for i in range(rows):
    print ("*"*columns)
get_enter()
clear_terminal()
write_title(26)
for i in range(6):
    print("*"*i)
get_enter()
clear_terminal()
write_title(27)
for i in range(10):
    for j in range(10):
        print(i+1,(j+1)*(i+1))
get_enter()
clear_terminal()
write_title(28)
for i in range(5):
    for j in range(5):
        print(i+1,j+1)
get_enter()
clear_terminal()
write_title("29-PROJECT")
while True:
    choise = input(f"""
===== MATH GAME =====

1. Start Game
2. View Instructions
3. Exit

Choose: """)
    if choise == "1":
        count = 0
        for i in range(10):
            answer = input(f"{i+2} + {i+7}: ")
            if int(answer) == (i+2)+(i+7):
                count += 1
        print(f"The score is: {count}!")
    elif choise == "2":
        print("""
Ten arithmetic questions; each correct answer earns a point. 
You can see your total score at the end.""")
    elif choise == "3":
        print("goodby!")
        break
    else:
        print("Not vald choise\n") 