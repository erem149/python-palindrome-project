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
# Lists - Exercise (Selling Lemonade)
# - You sell lemonade over two weeks, the lists show number of lemonades sold per week
# - Profit for each lemonade sold is 1.5$
# - Add another day to week 2 list by capturing a number as input
# - Combine the two lists into the list called 'sales'
# - Calculate / print how much you have earned on Best Day and Worst Day
# - Separately and in total.
# - hint: 3 prints in total
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
#sales.extend(sales_w1)
#sales.extend(sales_w2)
print(sales_w2)
sales = sales_w1 + sales_w2
#sales.sort()
print(sales)
worst_day_prof = min(sales) * 1.5
best_day_prof = max(sales) * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')