# my_file = open('reading_files/greeting.txt', 'r') #w = write, a=append
# print(my_file.read(100))

# print(my_file.read(10))

# print(my_file.readline())

# line_by_line = my_file.readlines()
# print('readlines: ',line_by_line)

# line_by_line1 = my_file.readline().splitlines()
# print('splitlines: ',line_by_line1)

# my_file.close()
with open('friends.csv', 'r') as f:
#     # print(f.read())

    friends = f.read().splitlines()
#     print(friends)

    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year = int(friend[1].strip())
        print(f'In 2030 {name} will be {2030 - year} years old')
        
with open('movies.txt', 'r') as f:
    #for line in f: #not in Skip
    for line in f.readlines(): #Skip workaround
        print(line)
#Important Hints:
#We learned that if we want to reading files, we need to run it one by one by commenting each code line