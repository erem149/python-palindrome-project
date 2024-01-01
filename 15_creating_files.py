#create greeting.txt
msg = 'Hello,\nWelcome to Monty Pythons Flying Circus!'
with open('greeting.txt', 'w') as f:
    f.write(msg)
with open('friends.csv', 'w') as f:
    f.write('John, 1939\nEric, 1943\nMichael, 1943\nGraham, 1941\nTerryG, 1940\nTerryJ, 1942')

# create cart.txt
msg = 'Iphone, 399\nHeadset, 65\nLaptop, 599\n'
with open('cart.txt', 'w') as f:
    f.write(msg)
with open('cart.txt', 'a') as f:
    f.write('display, 138\n')
with open('movies.txt', 'w') as f:
    f.write('Holy Grail, 1975\nLife of Brian, 1979\nMeaning of Life, 1983\n')
    