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