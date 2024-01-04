# #Crypto - Machine
# print('Project - Crypto')
# def enigma_light():
# # create keys string
#     keys = 'abcdefghijklmnopqrstuvwxyz !'
# # autogenerate the values string by offsetting original string
#     values = keys[-1] + keys[0:-1]
#     # print(keys)
#     # print(values)
# # create two dictionaries
#     dict_e = dict(zip(keys,values))
#     dict_d = dict(zip(values,keys))
# # OR create 1 and the flip
#     dict_e = dict(zip(keys,values))
#     dict_d = {value:key for key, value in dict_e.items()}
# # user input 'the message' and mode
#     msg = input('Enter your secret message quietly: ')
#     # mode = input('Crypto mode: encode (e) OR decode (d): ')
#     mode = input('Crypto mode: encode (e) OR decrypt as default: ')
# # run encode and decode
#     if mode.lower() == 'e':
#         # new_msg = [dict_e[letter] for letter in msg]
#         new_msg = [''.join([dict_e[letter] for letter in msg.lower()])]
#     # elif mode.lower() == 'd':
#     else:
#         new_msg = [''.join([dict_d[letter] for letter in msg.lower()])]
# # return result
#     # return new_msg
#     return new_msg.capitalize()
# # clean and beautify the code
    
# print(enigma_light())

def enigma_light():
# create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
# autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
    #print(keys)
    #print(values)
# create two dictionaries
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys)) 
# OR create 1 and then flip 
    dict_e = dict(zip(keys,values))
    dict_d = {value:key for key, value in dict_e.items()}
#user input 'the message' and mode
    msg = input('Enter your secret message quietly: ')
    mode = input('Crypto mode: encode (e) OR decrypt as default: ')
# run encode or decode
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])
    
    return new_msg.capitalize()
# return result
# clean and beautify the code 

print(enigma_light())