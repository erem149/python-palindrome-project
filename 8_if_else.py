# Conditionals: IF Statements
is_raining = True
is_cold = False
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and Jacket")
elif is_raining and not(is_cold):
    print("Bring Umbrella")
elif is_cold and not(is_raining):
    print("Bring Jacket")
elif is_raining or is_cold:
    print("Bring Umbrella or Jacket or both")
else:
    print("Shirt is Fine!")

amount = 51
if amount <= 50:
    print("Purchase approved")
else:
    print("Please enter your pin!")
# IF ELIF ELSE - Exercise
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celcius to fahreinheit conversion
# formula is: temp in C*9/5 + 32 = temp in F
    
mode = input("\nEnter math operation (+,-,*,/) or f for Celcius to Fahrenheit conversion: ")
num1 = float(input("Enter the first number: "))
if (mode.lower() == 'f'):
    print(f'{num1} Celcius is equivalent to {(num1*9/5) + 32} Fahreinheit')
else:
    num2 = float(input("Enter the second number: "))
    if (mode == '+'):
        print(f'Answer is: {num1 + num2}')
    elif (mode == '-'):
        print(f'Answer is: {num1 - num2}')
    elif (mode == '*'):
        print(f'Answer is: {num1 * num2}')
    elif (mode == '/'):
        print(f'Answer is: {num1 / num2}')
    else:
        print("Input error!")

def calculator():
    print("\n===Welcome to the Calculator===")
    num1 = float(input("Enter the first number: "))
    mode = input("Which math operation do you want to used (+,-,*,/): ")
    num2 = float(input("Enter the second number: "))
    if (mode == '+'):
        print(f'Result: {num1 + num2}')
    elif (mode == '-'):
        print(f'Result: {num1 - num2}')
    elif (mode == '*'):
        print(f'Result: {num1 * num2}')
    elif (mode == '/'):
        print(f'Result: {num1 / num2}')
    else:
        print("Wrong input.. kindly enter the proper operator that available~")

def temperature():
    print("\n===Welcome to the Temperature Converter (Celcius to Fahreinheit)===")
    celcius = float(input("Enter your temp in celcius: "))
    print(f'{celcius} Celcius is equivalent to {(celcius*9/5) + 32} Fahreinheit')

switch = input("\nWhat type of service do you want to use: \n1. Calculator\n2. Temperature Converter\nEnter the number 1 to 2: ")
if(switch == '1'):
    calculator()
elif(switch == '2'):
    temperature()
else:
    print("Wrong input.. Kindly enter the number 1 or 2~")

# optimize/shorten the code in the function
# try to reduce the number of conditionals
def num_days(month):
    
    if month == 'jan':
        print('number of days in', month, 'is', 31)
    elif month == 'feb':
        print('number of days in', month, 'is', 28)
    elif month == 'mar':
        print('number of days in', month, 'is', 31)
    elif month == 'apr':
        print('number of days in', month, 'is', 30)
    elif month == 'may':
        print('number of days in', month, 'is', 31)
    elif month == 'jun':
        print('number of days in', month, 'is', 30)
    elif month == 'jul':
        print('number of days in', month, 'is', 31)
    elif month == 'aug':
        print('number of days in', month, 'is', 31)
    elif month == 'sep':
        print('number of days in', month, 'is', 30)
    elif month == 'oct':
        print('number of days in', month, 'is', 31)
    elif month == 'nov':
        print('number of days in', month, 'is', 30)
    elif month == 'dec':
        print('number of days in', month, 'is', 31)

num_days('jul')
# The 1st optimization
def num_days(month):
    
    if month == 'jan' or month == 'mar' or month == 'jan' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
        print('number of days in', month, 'is', 31)
    elif month == 'feb':
        print('number of days in', month, 'is', 28)
    elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
        print('number of days in', month, 'is', 30)

num_days('jan')
# The 2nd optimization
def num_days(month):
    
    if month == 'jan' or month == 'mar' or month == 'jan' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
        print('number of days in', month, 'is', 31)
    elif month == 'feb':
        print('number of days in', month, 'is', 28)
    else:
        print('number of days in', month, 'is', 30)

num_days('oct')
# The 3rd optimization
def num_days(month):
    days = 31
    if month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in', month, 'is', days)

num_days('feb')
# The 4th optimization
def num_days(month):
    days = 31
    if month in ['apr', 'jun', 'sep', 'nov']: # we can also use list, tuple and set. Set is a bit faster among those three membership functions.
    # if month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in', month, 'is', days)

num_days('sep')

#OPTIMIZATION
def calculator():
    print("\n===Welcome to the Calculator_OPT_===")
    num1 = float(input("Enter the first number: "))
    mode = input("Which math operation do you want to used (+,-,*,/): ")
    num2 = float(input("Enter the second number: "))
    if (mode == '+'):
        result = num1 + num2
    elif (mode == '-'):
        result = num1 - num2
    elif (mode == '*'):
        result = num1 * num2
    elif (mode == '/'):
        result = num1 / num2
    else:
        print("Wrong input.. kindly enter the proper operator that available~")
    print(f'Result: {result}')

def temperature():
    print("\n===Welcome to the Temperature Converter (Celcius to Fahreinheit)===")
    celcius = float(input("Enter your temp in celcius: "))
    print(f'{celcius} Celcius is equivalent to {(celcius*9/5) + 32} Fahreinheit')

switch = input("\nWhat type of service do you want to use: \n1. Calculator\n2. Temperature Converter\nEnter the number 1 to 2: ")
if(switch == '1'):
    calculator()
elif(switch == '2'):
    temperature()
else:
    print("Wrong input.. Kindly enter the number 1 or 2~")