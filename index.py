#intro
failed_subjects = str(int(float("6.5")))
pronouns='It\'s'
print(pronouns + " failing " + failed_subjects + " subjects.")
msg='Welcome to Python 101: Strings'
print(len(msg))
print(msg.count('o'))

#slicing
msg1=msg[-10] + ' ' + msg[:7] + ' ' + msg[-5:-1] + ' ' +  msg[8:10] + ' ' + msg[13] + msg[12] + msg[2] + msg[1] + msg[-5]
print(msg1[::-1].title()) # printed "1 Welcome Ring To Tyler" as backwards
print('Python' not in msg) # we can use 'not' or 'not in' commands to describe whether it's TRUE or FALSE
print(f'[{pronouns.capitalize()} lovely day!]')
# # - Create a distance converter converting Km to miles
# # - Take two inputs from user: Their first name and the distance in km
# # - Print: Greet user by name and show km, and mile values
# # - 1 mile is 1.609 kilometers
# # - hint: use correct types for calculating and print
# # - Did you capitalize the name
# user_name = input('Enter your name : ')
# distance_in_km = input('Enter your distance in km : ')
# distance_in_mi = float(distance_in_km) / 1.609
# print(f'Hi {user_name}! {distance_in_km} km is equivalent to {round(distance_in_mi, 1)} miles.')

#Lists
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
cars = [911,130,328,535,740,308]
print(friends[1], friends[4])
print(len(friends))
print(friends.index('Eric'))
print(friends.count('Eric'))
friends_sort = sorted(friends) # return the sorted list
print(friends_sort)
friends.sort() # sort the list in place
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)
print(min(cars))
print(min(friends))
print(max(cars))
print(sum(cars))
friends.append('TerryG1') # add word to the last position
print(friends)
friends.insert(1, 'TerryG2') # add word to the current by appointing index we choose
print(friends)
friends[2]='TerryG3' # replcae Terry with TerryG
print(friends)
friends.extend(cars) # join friends + cars lists
print(friends)
friends.remove("Terry")
print(friends)
friends.pop(-1) # pop will remove the last position by default 
                # and pop is stored into memory and can be used it again in the program
print(friends)
# friends.clear() # empty []
# print(friends)
# del friends # remove completely the element
del friends[2] # remove completely the element
print(friends)
new_friends = friends[:]
friends_copy = friends.copy()
friends_list = list(friends)
print(friends)
print(new_friends)
print(friends_copy)
print(friends_list)
# # Lists - Exercise (Selling Lemonade)
# # - You sell lemonade over two weeks, the lists show number of lemonades sold per week
# # - Profit for each lemonade sold is 1.5$
# # - Add another day to week 2 list by capturing a number as input
# # - Combine the two lists into the list called 'sales'
# # - Calculate / print how much you have earned on Best Day and Worst Day
# # - Separately and in total.
# # - hint: 3 prints in total
# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []
# new_day = input('Enter #of lemonades for new day: ')
# sales_w2.append(int(new_day))
# #sales.extend(sales_w1)
# #sales.extend(sales_w2)
# print(sales_w2)
# sales = sales_w1 + sales_w2
# #sales.sort()
# print(sales)
# worst_day_prof = min(sales) * 1.5
# best_day_prof = max(sales) * 1.5
# print(f'Worst day profit:$ {worst_day_prof}')
# print(f'Best day profit:$ {best_day_prof}')
# print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

#split and join
msg = 'Welcome  to  Python  101:  Split  and  Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric', 'John', 'Michael', 'Terry', 'Graham']
print(list(msg), type(list(msg))) # converted the string (sentence -> letter) into list
print(msg.split(), type(msg.split())) # converted the string (sentence -> word) into list
print(msg.split(' '), type(msg.split(' ')))
print(csv.split(','), type(csv.split(','))) # split type you will get is list
print(str(friends_list), type(str(friends_list)))
print('-'.join(friends_list), type('-'.join(friends_list))) # split type you will get is string
print('-'.join(friends_list + friends_list), type('-'.join(friends_list + friends_list)))
print(''.join(msg.split())) #the same result as below
print(msg.replace(' ', '')) #the same result as above
# - Split and Join - Exercise
# - From the list below fill a list(friends_list) properly
# - With the names of all the friends. One per "slot"
# - You may need to run same command several times
# - Use print() statements to work your way through the exercise
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
print(csv.split(','))
print('-'.join(csv.split(',')))
print(','.join(csv.split(',')))
print((','.join(csv.split(';')).split(':')))
print(','.join(','.join(csv.split(';')).split(':')))
print(','.join(','.join(csv.split(';')).split(':')).split(','))
# friends_list = ['Exercise: fill me with names']
friends_list = ','.join(','.join(csv.split(';')).split(':')).split(',')
print(f'Result = {friends_list}')
print('Replace = ', csv.replace(';',',').replace(':',',').split(','))

#Tuples - faster Lists you cannot change
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
friends_tuple = ('John', 'Michael', 'Terry', 'Eric', 'Graham')
friends_set = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
my_friends_set = {'Reg', 'Loretta', 'Colin', 'Eric', 'Graham'}
print(friends[2:4])
print(friends_tuple[2:4])
#Sets - blazingly fast unordered Lists
print(friends_set)
print(friends_set.intersection(my_friends_set)) 
print(friends_set.difference(my_friends_set)) 
print(friends_set.union(my_friends_set)) 
# List < Tuple < Set -> Faster
#empty Lists
empty_list = []
empty_list = list()
#empty Tuple
empty_tuple = ()
empty_tuple = tuple()
#empty Set
empty_set = {} # this is wrong, this is dictionary
empty_set = set()
# Sets - Exercise
#1. Check if 'Eric' and 'John' exist in friends -> using in
#2. Combine or add the two sets -> using union and |
#3. Find names that are in both sets -> using intersection
#4. Find names that are only in friends -> using difference and -
#5. Show only the names who only appear in one of the lists -> using ^ and symmetric_difference
#6. Create a new cars-list without duplicates -> using set and list
friends = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
my_friends = {'Reg', 'Loretta', 'Colin', 'John', 'Graham'}
cars = ['900', '420', 'V70', '911', '996', 'V90', '911', '911', 'S', '328', '900']
print('Eric' in friends and 'John' in friends)
print(friends.union(my_friends))
print(friends | my_friends)
print(friends.intersection(my_friends))
print(friends.difference(my_friends))
print(friends - my_friends)
print(my_friends.difference(friends))
print(my_friends - friends)
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)
cars_no_dupl = list(set(cars))
print(cars_no_dupl)

#Comments
print("#Comments")
#Hiding in the comments
'''
these are multiple comments~
'''
#Entry form for Ministry applications
#to-do: fix it! it doesn't work -Fixed
name = "Default"
# name = input(Enter your silly name: )
print("Thank you " + name + "!")
print("for applying to")
print("the Ministry of Silly Walks")

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
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# color = input('Enter your favorite color: ')
# greeting(name, int(age), color)
# greeting("Judith")

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

# Comparisons and Boolean
a = 7
b = 3
print('a == b is ', a == b) # Output: False
print('a != b is ', a != b) # Output: False
print('a > b is ', a > b) # Output: False
print('a < b is ', a < b) # Output: False
print('a >= b is ', a >= b) # Output: False
print('a <= b is ', a <= b) # we can use ==, >, <, >=, <=. Output: False
print('o' in 'John') # Output: True
print('o' not in 'John') # Output: False
print(a is b) # Output: True
print(id(a), id(b)) # Output: Same memory
a = [3,7,42]
b = [3,7,42]
print(a is b) # Output: False
print(id(a), id(b)) # Output: Different memory
print(int(True)) # Output: 1
print(int(False)) # Output: 0
print(bool('Parrot')) # Output: True
print(bool(' ')) # Output: True
print(bool('')) # Output: False
print(bool(42)) # Output: True
print(bool(0)) # Output: False
print(bool([1,2])) # Output: True
print(bool([])) # Output: False
print(42 + True) # Output: 43
print(42 + False) # Output: 42

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