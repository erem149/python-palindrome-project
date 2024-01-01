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
    
# mode = input("\nEnter math operation (+,-,*,/) or f for Celcius to Fahrenheit conversion: ")
# num1 = float(input("Enter the first number: "))
# if (mode.lower() == 'f'):
#     print(f'{num1} Celcius is equivalent to {(num1*9/5) + 32} Fahreinheit')
# else:
#     num2 = float(input("Enter the second number: "))
#     if (mode == '+'):
#         print(f'Answer is: {num1 + num2}')
#     elif (mode == '-'):
#         print(f'Answer is: {num1 - num2}')
#     elif (mode == '*'):
#         print(f'Answer is: {num1 * num2}')
#     elif (mode == '/'):
#         print(f'Answer is: {num1 / num2}')
#     else:
#         print("Input error!")

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

# switch = input("\nWhat type of service do you want to use: \n1. Calculator\n2. Temperature Converter\nEnter the number 1 to 2: ")
# if(switch == '1'):
#     calculator()
# elif(switch == '2'):
#     temperature()
# else:
#     print("Wrong input.. Kindly enter the number 1 or 2~")

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

# switch = input("\nWhat type of service do you want to use: \n1. Calculator\n2. Temperature Converter\nEnter the number 1 to 2: ")
# if(switch == '1'):
#     calculator()
# elif(switch == '2'):
#     temperature()
# else:
#     print("Wrong input.. Kindly enter the number 1 or 2~")

# While Loops
# print("1.*Loops are great*")
# print("2.**Loops are great**")
# print("3.***Loops are great***")
# print("4.****Loops are great****")
# print("5.*****Loops are great*****")

i=0
while i < 5:
    # print(f"{i+1}." + '*' * (i+1) + "Loops are awesome" + '*' * (i+1))
    # i=i+1 # starting with 1
    i+=1 # starting with 1
    print(f"{i}." + '*' * i + "Loops are awesome" + '*' * i)
    # i=i+1 -> starting with 0
    
# While Loops - Exercise
print('Guessing game')
# Gues the correct number in 3 guesses. If you don't get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins, 2. If user loses
# Tip:( remember you won't see print statements during execution, so If you want to see prints during while loop, then print to the input box )
# This is specific to this platform)
# while condition:
#     code
#     iterator
# Three Loop Questions:
#1. What do I want to repeat?
# -> guesses
#2. What do I want to change each time?
# -> guess number and number of guesses
#3. How long should we repeat?
# -> until user loses, runs out of guesses, or wins

# secret_num = 12
# guess = 0
# guess_limit = 3
# guess_number = 0

# while guess_number < guess_limit:
#     guess = int(input(f"Guess #{guess_number+1} a number 1-20 (last guess: {guess}): "))
#     if guess == secret_num:
#         print(f"You Win! You Guessed it: {guess}")
#         break
#     else:
#         print(f"No, not {guess}!")
#         guess_number += 1
# if guess != secret_num:
#     print(f"Sorry you Lose! It was {secret_num}")
#Modification Version
#Modification 1: number 1-100, tell user if guess is too high/low, and let them have 5-10 guesses.
# Tip: ( remember you won't see print statements during execution, so If you want to see prints during while loop, print to the input box 
# secret_num = 76
# guess = 0
# guess_limit = 5
# guess_number = 0
# guess = int(input(f"Guess a number 1-100: "))
# guess_number += 1
# while guess_number < guess_limit:
#     if guess != secret_num:
#         guess_number += 1
#         if guess > secret_num:
#             guess = int(input(f"{guess} Too high - Guess again 1-100: "))
#         else:
#             guess = int(input(f"{guess} Too low - Guess again 1-100: "))
#     if guess == secret_num:
#         print(f"You Win! You Guessed it: {guess}")
#         break
# if guess != secret_num:
#     print(f"Sorry you Lose! It was {secret_num}")

# For Loops
for letter in 'Norwegian blue':
    print(letter)

for furgle in range(8):
    print(furgle)

for furgle in range(2, 8):
    print(furgle)

for furgle in range(1,15,3):
    print(furgle)

for name in ('John', 'Terry', 'Eric', 'Michael', 'George'):
    print(name)

friends = ['John', 'Terry', 'Eric', 'Michael', 'George']

for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(friends[index] + '\n')

for friend in friends:
    if friend == 'Eric':
        print('Found ' + friend + '! - break')
        break
    print(friend)

for friend in friends:
    if friend == 'Eric':
        print('Found ' + friend + '! - continue')
        continue
    print(friend)

for friend in friends:
    if friend == 'Eric':
        print('Found ' + friend + '! - no condition') #after we Found Eric, it will printed Eric again
    print(friend) #printed Eric

friends = ['John', 'Terry', 'Eric']
for friend in friends:
    for number in [1, 2, 3]:
        print(friend, number)
print("For Loops done!")

# For Loops - Exercise
print("Party Invitation")
# You're having a party and want to invite your friends.
# You want the print out invitations for each friend using for loops
# The names are in two lists, 'names' and 'names1'
# You also need to add two extra names to the list using an 'input' box, when you run the code
# Names should be properly capitalized
# Example of printout: John Cleese! You are invited to the party on Saturday.
# Example of printout: Eric Idle! You are invited to the party on Saturday.
# Hint: you may need two (for) loops to solve this exercise
names = ['john ClEEse', 'Eric IDLE', 'michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
msg = 'You are invited to the party on Saturday'
# names.extend(names1)
names += names1
# for index in range(2):
#     names.append(input('Enter a new name: '))

for name in names:
    msg1 = f'{name.title()}! {msg}'
    msg1 = name.title() + '! ' + msg
    print(msg1)

# Enumerate This
# Enumerate() is used with a list called l1. It first prints tuples of index and element pairs.
# Then it changes the starting index while printing them together. Finally, it prints the index and element separately, each on its own line.
print('Python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
eFriends = [(51, 'Brian'), (52, 'Judith'), (53, 'Reg'), (54, 'Loretta'), (55, 'Colin')]
i = 51
for friend in friends:
    print(i, friend, '\n')
    i = i + 1 # += 1

for num, friend in enumerate(friends, 51):
    print(num, friend)

for friend in enumerate(friends, 51):
    print(friend)

for friend in enumerate(enumerate(friends, 51), -100):
    print(friend)

for num, eFriend in enumerate(eFriends, 1):
    print(num, eFriend)

for num, letter in enumerate('python', start = 5):
    print(num, letter)

print(type(enumerate(friends)))
print(list(enumerate(friends)))

print(type(enumerate(eFriends)))
print(list(enumerate(eFriends)))

# Sort and Sorted
print('sort() and sorted()')
print('Immutability and return values')

my_list = [1, 5, 3, 7, 2]
my_dict = {'car':4, 'dog':2, 'add':3, 'bee':1}
my_tuple = ('d', 'c', 'e', 'a', 'b')
my_string = 'python'

print(my_list, 'original - sorted')
print(my_list.sort())
print(my_list,'new - sort')
print(my_list.reverse())
print(my_list,'new - reverse')
print(my_list, 'original - sorted')
print(sorted(my_list))
print(my_list,'new - sorted')
mylist_sorted = sorted(my_list)
print(mylist_sorted, 'mylist_sorted_var')

print(my_tuple, 'original - tuple')
print(sorted(my_tuple))
print(my_tuple, 'new - mytuple')

print(my_string, 'original - string')
print(sorted(my_string))
print(my_string, 'new - mystring')

print(my_dict, 'original - dict')
print(sorted(my_dict))
print(my_dict, 'new - mydict')

print(my_dict, 'original - dict w/ items')
print(sorted(my_dict.items()))
print(my_dict, 'new - mydict')

print(my_dict, 'original - dict w/ values')
print(sorted(my_dict.values()))
print(my_dict, 'new - mydict')

print(my_dict, 'original - dict w/ values')
print(sorted(my_dict.values(), reverse=True))
print(my_dict, 'new - mydict w/ val & reverse')

print(my_list, 'original - reversed w/ list')
print(list(reversed(my_list))) # same result
print(my_list,'new - reversed w/ list')
print(my_list[::-1]) # same result

my_list = [1, 5, -3, 7, -2]
my_llist = [['car',4,65], ['dog',2,30], ['add',3,10], ['bee',1,24]]
print(sorted(my_list, key = abs)) # we can added any function to this key
print(sorted(my_llist, key = lambda item : item[2]))

# Dictionaries
print("{Dictionaries}")
movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John', 'Eric', 'Michael', 'George', 'Terry']
}
print(movie)
print(movie['title'])
# print(movie['budget']) # doesn't exist and will get an error
print(movie.get('budget'))
print(movie.get('budget', 'not found')) 
movie['title'] = 'The Holy Grail'
print(movie.get('title'))
movie['budget'] = 250000
print(movie.get('budget'))
movie.update({'title' : 'The Holy Grail', 'year' : 1975, 'cast' : ['John', 'Eric', 'Michael', 'George', 'Terry']})
print(movie)
# del movie['year']
year = movie.pop('year') # this is the alternative of del
print(year)
print(movie)

print(len(movie))
print(movie.keys())
print(movie.values())
print(movie.items()) # tuple
for key in movie:
    print(key)
for key, value in movie.items():
    print(key, value)

# Dictionaries - II
python = {'John':35, 'Eric':36, 'Michael':35, 'Terry':38, 'Graham':37, 'TerryG':34}
holy_grail = {'Arthur':40, 'Galahad':35, 'Lancelot':39, 'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33, 'Reg':35, 'Stan/Loretta':32, 'Biccus Diccus':45}
#membership test
print('arthur' in holy_grail) # False as it's case sensitive
print('Arthur' in holy_grail)
if 'Arthur' not in holy_grail: # not will print nothing but if in it would be otherwise
    print('He\'s not here!')

people = {}
people1 = {}
people2 = {}
#method 1 update
people.update(python) # will add python
people.update(holy_grail) # will add python and holy_grail
people.update(life_of_brian) # will add python, holy_grail, and life_of_brian
print(people)
#method 2 comprehension
for groups in (python, holy_grail) : people1.update(groups)
print(people1)
for groups in (python, holy_grail, life_of_brian) : people1.update(groups)
print(people1)
#method 3 unpacking 3.5 version of python or later
people2 = {**python, **holy_grail, **life_of_brian}
print(people2)

#after sorted
people.update(life_of_brian) # will add python, holy_grail, and life_of_brian
print(sorted(people))
for groups in (python, holy_grail, life_of_brian) : people1.update(groups)
print(sorted(people1))
#method 3 unpacking 3.5 version of python or later
people2 = {**python, **holy_grail, **life_of_brian}
print(sorted(people2))

#after add items
people.update(life_of_brian) # will add python, holy_grail, and life_of_brian
print(sorted(people.items()))
for groups in (python, holy_grail, life_of_brian) : people1.update(groups)
print(sorted(people1.items()))
#method 3 unpacking 3.5 version of python or later
people2 = {**python, **holy_grail, **life_of_brian}
print(sorted(people2.items()))
print('The sum of the ages:', sum(people.values())) # if there's a string in the list it would be got error

# Exersise - Dictionary
#1. It's... not really an adventure game...#Ver 1.0
#2. Your village is being attacked by 'a germanic tribe' and you need to run the stores and get the right
#things to save your village, and probably some good looking girl or boy you want to marry.
#All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#3. The code should allow you to get 1 thing from each store and each item you get should be removed
#from the store inventory, then do same for next store...
#4. One way to buy by typing the key 'newt' in an input box... or something
#5. At the end you should print the 'items' you have taken.. in this version you don't have to pay for
#stuff or add it up
#6. Ver 1.2 add ability to exit store without buying and go to next by typing 'exit', and to exit if
#a non-existant item is bought(typed)
#7. Add pursue with 1000 gold pieces and payment for the items during or at end of code and show a message
#about total cost and how much gold you have left
#8. Ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop
#scrolling Tiktok/Facebook! ;-)
#9. Ver 1.5 print inventory before and after purchases as one department_store of stuff (combine
#inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant
#reporting for inventory management...)
#10. As in all games, there is a special way to do this that actually makes money and solves the problem
#...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
freelancers = {'name':'Freelancing Shop', 'brian':70, 'black night':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop', 'french castle':400, 'wooden grail':3, 'scythe':150}
pet_shop = {'name':'Pet Shop', 'blue parrot':10, 'white rabbit':5, 'newt': 2}

# #create an dempty shopping cart
# cart = {}
# #loop through stores/dicts
# for LOOP OVER THE SHOPS:
#     #inputbox to show what you can buy...capture text string of what was bought...make lowercase
#     buy_item = input(f'Welcome to {SHOPNAME}! what do you want to buy: {LIST ITEMS FOR SALE}')
#     #update the cart
#     cart.update({insert KEYVAL: VALUE}) # use pop...
# print(f'You Purchased {ITEMS PURCHASED} Today it is all free. Have a nice day of mayhem!')

#create an dempty shopping cart
cart = {}
#loop through stores/dicts
for shop in (freelancers, antiques, pet_shop):
    #inputbox to show what you can buy...capture text string of what was bought...make lowercase
    buy_item = input(f'\nWelcome to {shop["name"]}! what do you want to buy:\n{shop}\nWrite your order here: ').lower()
    #update the cart
    cart.update({buy_item:shop.pop(buy_item)}) # use pop...
    # cart[buy_item] = shop.pop(buy_item) -> the above code also can be written like this
    buy_items = ", ".join(list(cart.keys()))
print(f'\nYou Purchased {buy_items}. Today it is all free. Have a nice day of mayhem!\n')