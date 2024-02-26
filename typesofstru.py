# Create a list of names
names = ['Alice', 'Bob', 'Charlie', 'Dave']
numbers = [1,2,5,3,1,3,5,8,89,1,2,1,4,6,1]
# Create a tuple of ages corresponding to the names
ages = (25, 32, 19, 41)
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# Create a dictionary that maps each name to its age
name_to_age = dict(zip(names, ages))
# Print the original list, tuple, and dictionary
print('Names:', names)
print('Ages:', ages)
print('Name to age:', name_to_age)
# Modify the list by appending a new name
names.append('Eve')
print('Append Eve in List',names)
# Insert at index 2 value 10
names.insert(2, 10)
print('insert in List index 2 value 10',names)
# Add List2 to List1
names.extend(numbers)
print('Extend the List',names)
print('Sum of Numbers ',sum(numbers))
print('Count 1 in numbers ',numbers.count(1))
print('length of Numbers',len(numbers))
print('index 2 on numbers is ',numbers.index(2))
print('min number of numbers',min(numbers))
print('max number of numbers',max(numbers))
numbers.sort()
print('sorted numbers',numbers)
print('Pop from numbers',numbers.pop())
print('Pop with indexing 0 of numbers',numbers.pop(0))
numbers.remove(3)
print('remove 3 form numbers',numbers)
del numbers[0]
print('delete numbers ',numbers)
# Modify the tuple by creating a new one with an additional age
ages = ages + (28,)
x = Tuple1.count(3)
print('Tuple count of 3 ' ,x)
x = Tuple1.index(3)
print(' Tulple index of 3',x)
# Modify the dictionary by adding a new key-value pair
name_to_age['Eve'] = 28
d = name_to_age. get("Dave")
print('using Get function Value of Dave',d)
items = name_to_age.items()
print('using item function ',items)
dict_keys = name_to_age.keys()
print('using keys function ',dict_keys)
dict_values = name_to_age.values()
print('Using values function',dict_values)
name_to_age.pop("Bob")
print('Pop function use on Bob',name_to_age)
name_to_age.popitem()
print('Popitem function',name_to_age)
name_to_age.update({"Editor": "Abbey Rennemeyer"})
print('used update function',name_to_age)
second_dict = name_to_age.copy()
print('Copy function',second_dict)
name_to_age.clear()
print('clear function',name_to_age)
# Print the modified list, tuple, and dictionary
print('Names:', names)
print('Ages:', ages)
print('Name to age:', name_to_age)