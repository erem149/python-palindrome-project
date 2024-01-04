# Randomness
print("Randomness")

import random, string
for i in range(5):
    print('random()', random.random())
    print('random() * 6', random.random() * 6)
    print('uniform()', random.uniform(1,6))
    print('randint()', random.randint(1,6))
    print('randrange()', random.randrange(1, 100, 2))
friends_list = ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.choice(friends_list))
print(random.sample(friends_list, 3))
random.shuffle(friends_list)
print(friends_list)

smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
letters_numbers = string.ascii_letters + string.digits
print(letters_numbers)
word = ''
for i in range(7):
    # word = word + random.choice(letters_numbers)
    word += random.choice(letters_numbers)
word1 = ''.join(random.sample(letters_numbers, 7))
word2 = random.choices(letters_numbers, k=7)
print('word += random.choice(letters_numbers)', word)
print("''.join(random.sample(letters_numbers, 7))", word1)
print('random.choices(letters_numbers, k=7)', word2)