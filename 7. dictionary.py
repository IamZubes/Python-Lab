my_dict = {'name': 'Zubin', 'age': 19, 'city': 'Manjeri'}

print("Accessing Dictionary Elements:")
print(my_dict['name'])  

my_dict['country'] = 'India'
print("Updating a Dictionary:")
print(my_dict)  

del my_dict['age']
print("Deleting a Dictionary Element:")
print(my_dict)  

if 'name' in my_dict:
    print("Checking if a Key Exists:")
    print("Key 'name' exists")

print("Getting All Keys, Values, or Items:")
print(my_dict.keys())  
print(my_dict.values())  
print(my_dict.items())  

my_dict_copy = my_dict.copy()
print("Copying a Dictionary:")
print(my_dict_copy)  

my_dict.clear()
print("Clearing a Dictionary:")
print(my_dict)  