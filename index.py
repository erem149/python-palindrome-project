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