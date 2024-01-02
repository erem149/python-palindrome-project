nums = [1, 2, 3, 4]
nums1 = '1234'
letters = ['a', 'b', 'c', 'd']
names = ['John', 'Eric', 'Michael', 'Graham', 'Joe']
combo = zip(nums, letters)
combo1 = zip(nums1, letters)
combo2 = dict(zip(nums,letters))
combo3 = list(zip(nums,letters,names))
print(combo) # zip combo
print(list(combo)) # list of tuple
print(list(combo1)) # list of tuple for strings
print(combo2) # dictionary
print(combo3)
num,let,nam = zip(*combo3) # unzip marked with *
print(num, let, nam) # return to tuple

keys = 'this parrot is deseased'
values = 'denna papegojan ar avliden'
keys = keys.split()
values = values.split()
print(keys, values) # list comprehension
en_sv_dict = dict(zip(keys,values))
print(en_sv_dict) # The first method
new_dict = {key:value for key,value in zip(keys,values)}
print(new_dict) # The second method
en, sv = list(en_sv_dict.keys()), list(en_sv_dict.values())
print(en, sv) # The first method to unzip with list output
en1, sv1 = zip(*en_sv_dict.items())
print(en1, sv1) # The second method to unzip with tuple output