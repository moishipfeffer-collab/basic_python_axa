# exercise 1 
numbers = [10,20,30,40,50]
print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[2])

# exercise 2
names = ["moishi","rachel"]
print(len(names))
print(names[0][-1])
names[1] = "racheli"
print(names)

#exercise 3
grades = [89,90,98,100,98]
grades.append(89)
grades.insert(100)
grades[2] = 68
print(grades)

# exercise 4 
numbers = [1,2,3,4,5,6,7,8,9,0]
del numbers[0]
del numbers[-1]
del numbers[2]
print(numbers)

# exercise 5
items = ["shirt","table"]
print("shirt" in items)
print("shirt is in items")
print("sdlfk" not in items)
print("sdlfk not in items")

# exercise 6
numbers = [1,2,3,4,5,6,7,8,9,0]
for num in numbers:
    print(num)

# exercise 7
numbers = [1,2,3,4,5,6,7,8,9,0]
for num in numbers:
    if num % 2 == 0:
        print(num)

# exercise 8
grades = [89,90,98,100,98]
count = 0
for grade in grades:
    count += grade
print(count)

# exercise 9
numbers = [1,2,3,4,5,6,7,8,9,0]
biggest = numbers[0]
for number in numbers:
    if number > biggest:
        biggest = number
print(f"The gratest number is {biggest}")

# exercise 10
names = ["moishi","rachel"]
name = input("Enter name: ")
if name in names:
    print("Found")
else:
    print("Not Found")

# exercise 11 
numbers = [1,2,3,4,5,6,7,2,8,9,0]
number = int(input("Enter number: "))
if number in numbers:
    for i in range(len(numbers)):
        if numbers[i] == number:
            print(i)

# exercise 12
numbers = [1,2,3,4,5,6,7,2,8,9,0]
count = 0
for num in numbers:
    if num > 50:
        count += 1 
print(f"Grater then 5: {count}")

# exercise 13
numbers = [1,2,3,4,5,6,7,2,8,9,0]
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
print(f"The evan numbers: {even}")

# exercise 14
names = ["moishi","rachel"]
count = 0
while count < len(names):
    print(names[count],count)
    count +=1

# exercise 15
numbers = [1,2,3,4,5,6,7,2,8,9,0]
print(numbers[:3])
print(numbers[-3:])
print(numbers[2:6])
print(numbers[::-1])

# exercise 16
names = ["moishi","racheli","noa","tali","natan","gili","avi","eli","ester","tamar"]
for i in range(len(names)):
    if i % 2 == 0:
        print(names[i])
for i in range(len(names)):
    if i % 2 != 0:
        print(names[i])
print(names[::-2])

# exercise 17
numbers = [1,2,3,4,5,6,7,8,9,0,12,23,34,45,56,67,78,89,90,797]
new_numbers_1 = numbers[:len(numbers)//2]
new_numbers_2 = numbers[len(numbers)//2:]
new_numbers_3 = numbers[5:14]

# exercise 18 
numbers = [1,2,3,4,5,6,7,8,9,0,12,23,34,45,56,67,78,89,90,797]
new_numbers_1 = numbers[:len(numbers)//2]
new_numbers_2 = numbers[len(numbers)//2:]

# exercise 19 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mult = [num * 2 for num in numbers]
squared = [num ** 2 for num in numbers]
evan = [num for num in numbers if num % 2 == 0]
grater_5 = [num for num in numbers if num > 5]
print(mult,squared,evan,grater_5)

# exercise 20 
grades = [55, 90, 67, 100, 45, 82, 73, 30]
passed = [grade for grade in grades if grade >= 60]
faild = [grade for grade in grades if grade < 60]
plus_5 = [grade + 5 for grade in grades]

# exercise 21 
names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
new_names = [name for name in names if len(name) > 4]
upper = [name.upper() for name in names]
d_names = [name for name in names if name.startswith("D") > 4]

# exercise 22 
numbers = [12, 7, 25, 30, 9, 44, 18, 3]
new_numbers = [number for number in numbers if number % 3 == 0 and number > 10]

# exercise 23 
numbers = []
for i in range(10):
    numbers.append(int(input("Enter number: ")))
print(numbers)
gratest = numbers[0]
lowest = numbers[0]
for num in numbers:
    if num > gratest:
        gratest = num
    if num < lowest:
        lowest = num
print(gratest)
print(lowest)
print(sum(numbers) / len(numbers))

# exercise 24
names = ["moishi","racheli","noa","tali","natan"]
name = input("Enter naem: ")
if name in names:
    names.remove(name)
else:
    print("Name not found\n")
print(names)

# exercuse 25
numbers = [1,2,3,4,5,6,7,2,8,9,0]
evan = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]
grate = [num for num in numbers if num > 20]

# exercuse 26
numbers = [1,2,3,4,5,6,7,2,8,9,0]
num = int(input("Number: "))
count = 0
for i in range(len(numbers)):
    if numbers[i] == num:
        count += 1
if count == 0:
    print("Number not found\n")
else:
    print(f"Number found {count} times")

# exercise 27 
numbers_1 = [1,2,3,4,5]
numbers_2 = [6,7,8,9,0]
for n in numbers_2:
    numbers_1.append(n)
print(numbers_1)
print(numbers[:5])
print(numbers[5:])
print(numbers[::-1])

# exercise 28
numbers = [1,2,3,4,5,6,7,2,8,9,0]
num = int(input("Number: "))
exists = False
for n in numbers:
    if n == num:
        exists = True
if not exists:
    numbers.append(num)
print(numbers)

# exercise 29 project
grades = [85, 72, 90, 55, 100, 63, 48, 77]
want_exit = False
while not want_exit:
    choise = int(input("""
===== Grades Management =====

1. Show all grades
2. Add a grade
3. Search for a grade
4. Remove a grade
5. Show passing grades
6. Show failing grades
7. Show highest and lowest grade
8. Show average grade
9. Show first 3 grades
10. Show grades in reverse
0. Exit

Choose: """))
    if choise == 1:
        for grade in grades:
            print(grade)
    elif choise == 2:
        grades.append(input(f"Grade: "))
    elif choise == 3:
        grade = int(input("Grade: "))
        found = False
        count = 0
        indexes = []
        for i in range(len(grades)):
            if grade == grades[i]:
                count += 1
                indexes.append(i)
                found = True
        if found:
            print(f"\nFound in inexes {indexes}, {count} times")
        else:
            print("Not found")
    elif choise == 4:
        grade = int(input("Grade: "))
        for g in grades:
            if g == grade:
                found = True
        if found:
            grades.remove(grade)
        else:
            print("Not found")
    elif choise == 5:
        passed = [grade for grade in grades if grade >= 60]
        print(passed)
    elif choise == 6:
        faild = [grade for grade in grades if grade < 60]
        print(faild)
    elif choise == 7:
        highest = grades[0]
        lowest = grades[0]
        for g in grades:
            if g > highest:
                highest = g
            if g < lowest:
                lowest = g
        print(f"Highest: {highest}, Lowest: {lowest}")
    elif choise == 8:
        count = 0
        for g in grades:
            count += g
        if grades:
            print(f"Avg: {count / len(grades)}")
    elif choise == 9:
        print(grades[:3])
    elif choise == 10:
        print(grades[::-1])
    elif choise == 0:
        want_exit = True
    else:
        print("\nNot valid choise\n")