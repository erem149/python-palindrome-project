failed_subjects = str(int(float("6.5")))
pronouns='It\'s'
print(pronouns + " failing " + failed_subjects + " subjects.")
msg='Welcome to Python 101: Strings'
print(len(msg))
print(msg.count('o'))
#slicing
msg1=msg[-10] + ' ' + msg[:7] + ' ' + msg[-5:-1] + ' ' +  msg[8:10] + ' ' + msg[13] + msg[12] + msg[2] + msg[1] + msg[-5]
print(msg1[::-1].title()) # printed "1 Welcome Ring To Tyler" as backwards
print('Python' not in msg) # we can use not or in to describe whether it's TRUE or FALSE
print(f'[{pronouns.capitalize()} lovely day!]')