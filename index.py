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
antiques = {'name':'Antique Shop', 'french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
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

#morning inventory
department_store = {}
for department in (freelancers, antiques, pet_shop):
    department_store.update(department)
department_store.pop('name')
print('Morning inventory of stores', sorted(department_store.items()))
print('-----------------')
#create an dempty shopping cart
cart = {}
#create pursue with 1000Gp
purse = 1000
buy_items1 = ''
#loop through stores/dicts
for shop in (freelancers, antiques, pet_shop):
    #inputbox to show what you can buy...capture text string of what was bought...make lowercase
    buy_item = input(f'\nWelcome to {shop["name"]}! (type exit to exit store)\nWhat do you want to buy:\n{shop}\nWrite your order here: ').lower()
    #exit on exit typed or buying nonexistant item
    if buy_item == 'exit':
        continue
    if buy_item not in shop:
        continue
    #update string
    buy_items1 = buy_items1 + f'{buy_item}:{shop[buy_item]} Gp, '
    #update the cart
    cart.update({buy_item:shop.pop(buy_item)}) # use pop...
    # cart[buy_item] = shop.pop(buy_item) -> the above code also can be written like this line
    buy_items = ", ".join(list(cart.keys()))
    if buy_items is None:
        continue
    total_sum = sum(cart.values())
print(f'\nYou Purchased {buy_items}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')
print(f'You Purchased {buy_items1}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!\n')
#evening inventory
department_store_after = {**freelancers, **antiques, **pet_shop} #pyth 3.5
department_store_after.pop('name')
print('-----------------')
print('Evening inventory of stores', sorted(department_store_after.items()))