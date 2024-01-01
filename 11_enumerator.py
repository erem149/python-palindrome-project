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