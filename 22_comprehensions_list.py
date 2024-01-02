numbers = [1,2,3,4,5,6,7,8,9]
# give me a list with num squared for each num in numbers
new_list = []
for num in numbers:
    new_list.append(num*num)
print(new_list)

# list comprehensions example
new_list = [ num*num for num in numbers ]
print(new_list)
# give me a list with num squared for each num in numbers if num is even
new_list = [ num*num for num in numbers if num % 2 == 0 ]
print(new_list)
# give me a list with num squared for each num in numbers if num is odd
new_list = [ num*num for num in numbers if num % 2 != 0 ]
print(new_list)

# list comprehensions using lambda
new_list1 = filter(lambda num: num % 2 == 0, numbers)
print(list(new_list1))

# I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
new_list3 = []
for letter in 'spam':
    for num in range(4):
        new_list3.append((letter,num))
print(new_list3)

new_list3 = [(letter, num) for letter in 'spam' for num in range(4)]
print(new_list3)

# The comprehensions contains the same code as the for loop
# new_list = []
# for num in numbers:
#     new_list.append(num*num)

# new_list = [ num*num for num in numbers ]
# # --------------------------------------
# new_list = []
# for letter in 'spam':
#     for num in range(4):
#         new_list.append(letter,num)
# new_list = [(letter,num) for letter in 'spam' for num in range(4)]