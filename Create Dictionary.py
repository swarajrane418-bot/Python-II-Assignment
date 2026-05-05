# 4.1 Create and access dictionary elements
my_dict1 = {'name': 'Shree', 'age': 25}
print("Dictionary:", my_dict1)
print("Access 'name':", my_dict1['name'])

# 4.2 Update Dictionary
my_dict1['age'] = 26
print("Updated Dictionary:", my_dict1)

# 4.3 Removing Elements
del my_dict1['name']
print("After removing 'name':", my_dict1)

remove = my_dict1.pop('age','26')
print("After removing :",remove)

# 4.4 Merging of Dictionaries
my_dict2 = {'gender': 'Female', 'place': 'Cnada'}
my_dict1.update(my_dict2)
print(my_dict1)   