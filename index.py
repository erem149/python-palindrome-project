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
print('Python' not in msg) # we can use 'not' or 'not in' commands
                           #to describe whether it's TRUE or FALSE
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