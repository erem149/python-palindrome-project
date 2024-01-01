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