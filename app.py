# 1. Compare two numbers
'''
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print("Numbers are equal")
'''
# 2. Positive, Negative or Zero
'''
c = int(input("Enter a number: "))
if c > 0:
    print(f"{c} is positive")
elif c < 0:
    print(f"{c} is negative")
else:
    print(f"{c} is zero")
'''
# 3. Even or odd
'''
d = int(input("Enter a number: "))
if d % 2 == 0:
    print(f"{d} is even")
else:
    print(f"{d} is odd")
'''
# 4. Exam grade
'''
a = int(input("Enter your score: "))
if a >= 90:
    print("A")
elif a >= 80:
    print("B")
elif a >= 70:
    print("C")
elif a >= 60:
    print("D")
elif a >= 50:
    print("E")
else:
    print("F")
'''
# 5. Largest of three numbers
'''
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x >= y and x >= z:
    print(f"{x} is the largest number")
elif y >= x and y >= z:
    print(f"{y} is the largest number")
else:
    print(f"{z} is the largest number")
'''
# 6. Simple calculator
'''
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /, %, **, //): ")

if operation == "+":
    print(f"{x} + {y} = {x + y}")
elif operation == "-":
    print(f"{x} - {y} = {x - y}")
elif operation == "*":
    print(f"{x} * {y} = {x * y}")
elif operation == "/":
    print(f"{x} / {y} = {x / y}")
elif operation == "%":
    print(f"{x} % {y} = {x % y}")
elif operation == "**":
    print(f"{x} ** {y} = {x ** y}")
elif operation == "//":
    print(f"{x} // {y} = {x // y}")
else:
    print("Invalid operation")
'''
# 7. Age category
'''
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age")
elif age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")
'''

# 8. Discount system
'''
x = int(input("Enter the total purchase amount: "))
if x < 100:
    print("No discount")
elif x < 300:
    print("10% discount")
elif x < 500:
    print("15% discount")
else:
    print("20% discount")
'''

# 9. Order three numbers   
'''
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x <= y and x <= z:
    if y <= z:
        print(f"Order: {x}, {y}, {z}")
    else:
        print(f"Order: {x}, {z}, {y}")
else:
    if y <= x and y <= z:
        if x <= z:
            print(f"Order: {y}, {x}, {z}")
        else:
            print(f"Order: {y}, {z}, {x}")
    else:
        if x <= y:
            print(f"Order: {z}, {x}, {y}")
        else:
            print(f"Order: {z}, {y}, {x}")
'''
# 10. ATM Withdrawal
'''
account_balance = 1000
withdrawal_amount = int(input("Enter the amount to withdraw: "))
if withdrawal_amount <= 0:
    print("Invalid amount")
elif withdrawal_amount > account_balance:
    print("Insufficient balance")
else:
    account_balance -= withdrawal_amount
    print(f"Withdrawal successful. New balance: {account_balance}")
'''

# 11. Electricity bill
'''
Monthly_electricity_usage = int(input("Enter your monthly electricity usage in kWh: "))
if Monthly_electricity_usage <= 100:
    bill_amount = Monthly_electricity_usage * 0.08
    print(f"Your electricity bill is: ${bill_amount:.2f}")
    print(f"Your applied rate is: 0.08")
    print(f"Your Monthly electricity usage is: {Monthly_electricity_usage} kWh")
elif Monthly_electricity_usage <= 300:
    bill_amount = Monthly_electricity_usage * 0.12
    print(f"Your electricity bill is: ${bill_amount:.2f}")
    print(f"Your applied rate is: 0.12")
    print(f"Your Monthly electricity usage is: {Monthly_electricity_usage} kWh")
else:
    bill_amount = Monthly_electricity_usage * 0.15
    print(f"Your electricity bill is: ${bill_amount:.2f}")
    print(f"Your applied rate is: 0.15")
    print(f"Your Monthly electricity usage is: {Monthly_electricity_usage} kWh")
'''

# 12 Taxi fare
'''
Starting_fee = 2.00
travel_distance = int(input("Enter the travel distance in kilometers: "))
if travel_distance <= 5:
    fare = Starting_fee *0.7
    print(f"Your taxi fare is: ${fare:.2f}")
    print(f"Your applied rate is: {Starting_fee}")
    print(f"Your travel distance is: {travel_distance} km")
elif travel_distance <= 15:
    fare = Starting_fee * 0.6
    print(f"Your taxi fare is: ${fare:.2f}")
    print(f"Your applied rate is: {Starting_fee} + (distance - 5) * 0.50")
    print(f"Your travel distance is: {travel_distance} km")
else:
    fare = Starting_fee * 0.5
    print(f"Your taxi fare is: ${fare:.2f}")
    print(f"Your applied rate is: {Starting_fee} + 10 * 0.50 + (distance - 15) * 0.30")
    print(f"Your travel distance is: {travel_distance} km")
'''
'''
# 13. Mini loan decision system
age = int(input("Enter your age: "))
monthly_salary = int(input("Enter your monthly salary: "))
requested_loan_amount = int(input("Enter the requested loan amount: "))
if age < 18:   
    print("You are not eligible for a loan due to age restrictions.")
elif monthly_salary < 500:
    print("You are not eligible for a loan due to insufficient salary.")
elif requested_loan_amount > 10 * monthly_salary:
    print("You are not eligible for a loan due to high loan amount.")
else:
    print("Your loan application is approved.")
'''
# 14. Triangle type
'''
side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))
if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    print("Invalid triangle sides. The sum of any two sides must be greater than the third side.")
elif side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Invalid triangle sides. All sides must be positive.")
elif side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
'''
# 15. University admission decision
'''
exam_score = int(input("Enter your exam score: "))
school_score = int(input("Enter your school score: "))
age = int(input("Enter your age: "))
if age < 16:
    print("You are not eligible for admission due to age restrictions.")
elif exam_score > 600:
    print("You are eligible for admission.")
else:
    print("You are not eligible for admission.")
'''
#16. pass of fail - Ternary operator
'''
grade = int(input("Enter your grade: "))
if grade > 100 or grade < 0:
    print("Invalid grade. Please enter a grade between 0 and 100.")
else:
    result = "Pass" if grade >= 50 else "Fail"
    print(f"You have {result}ed the exam.")
'''
#17. delivery fee - Ternary operator
'''
order_total = int(input("Enter the order total: "))
membership = input("Are you a member? (yes/no): ")
if order_total < 0:
    print("Invalid order total. Please enter a non-negative value.")
else:
    delivery_fee = 0 if order_total >= 50 or membership.lower() == "yes" else 5
    print(f"Your delivery fee is: ${delivery_fee}")
'''
#18 day planner - match/case
'''
day = int(input("Enter a day number (1-7): "))
match day:
    case 1:
        print("Monday")
        print("study day")
    case 2:
        print("Tuesday")
        print("study day")
    case 3:
        print("Wednesday")
        print("study day")
    case 4:
        print("Thursday")
        print("study day")
    case 5:
        print("Friday")
        print("study day")
    case 6:
        print("Saturday")
        print("weekend")
    case 7:
        print("Sunday")
        print("weekend")
    case _:
        print("Invalid day number. Please enter a number between 1 and 7.")
'''
#19. cafe order - match/case
'''
drink_code = input("Enter the drink code (T, C, J): ")
quantity = int(input("Enter the quantity: "))
match drink_code.upper():
    case "T":
        print("You ordered Tea.")
        print("Price: $2.00")
        print(f"Total: ${2.00 * quantity:.2f}")
    case "C":
        print("You ordered Coffee.")
        print("Price: $3.00")
        print(f"Total: ${3.00 * quantity:.2f}") 
    case "J":
        print("You ordered Juice.")
        print("Price: $4.00")
        print(f"Total: ${4.00 * quantity:.2f}")
    case _:
        print("Invalid drink code. Please enter T, C, or J.")
'''
#20. student ID validation
student_id = input("Enter your student ID: ")
if len(student_id) != 8:
    print("Invalid student ID. It must be 8 characters long.")
else:
    if student_id[0].isalpha() and student_id[1:].isdigit():
        print("Valid student ID.")
    else:
        print("Invalid student ID. It must start with a letter followed by 7 digits.")