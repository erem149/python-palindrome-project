#Function
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color'
# 2. Extend the function with another input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday
#    adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps
# 6. Favorite color should be in lowercase
def greeting(name, age=28, color='red'):
    # Greets user with 'name' from 'input box' and 'age' next year, if variable, default age is used
    # Also includes favorite color
    print("Hello " + name.capitalize() + ", you will be " + str(age+1) + " years old next birthday!")
    print(f"Hello {name.capitalize()}, you will be {age+1} years old next birthday!")
    print(f'We hear you like the color {color}!')
name = input("Enter your name: ")
age = input("Enter your age: ")
color = input('Enter your favorite color: ')
greeting(name, int(age), color)
greeting("Judith")

# Functions - Named Notation
def greeting(name, age=28, color="red"):
    #Greets user with "name" from "input box" and "age", if unavailable, default age is used
    print(f"Hello {name.capitalize()}, you will be {age+1} years old next birthday!")
    print(f"We hear you like the color {color.lower()}")
greeting(name="brian", color="Blue", age=27)

# Return Statements
def value_added_taxt(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return tax
price = value_added_taxt(100)
print(price, type(price)) # Output: <class 'float'>
def value_added_taxt(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return amount, tax, total_amount
price = value_added_taxt(100)
print(price, type(price)) # Output: <class 'tuple'>
def value_added_taxt(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return [amount, tax, total_amount]
price = value_added_taxt(100)
print(price[1], type(price)) # Output: <class 'list'>
def value_added_taxt(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return {amount, tax, total_amount}
price = value_added_taxt(100)
print(price, type(price)) # Output: <class 'set'>
def value_added_taxt(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return f"{amount}, {tax}, {total_amount}"
price = value_added_taxt(100)
print(price, type(price)) # Output: <class 'str'>