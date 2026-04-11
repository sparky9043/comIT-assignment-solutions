# Example of list

fruits = ['apple', 'banana', 'grapes', 'tomato']

# Appending to the end of the list: O(1)
fruits.append('kiwi')

# Inserting to or deleting the beginning of the list: O(n) due to shift
fruits.insert(0, 'mango')
fruits.remove('mango')

# Reading one element inside an array: O(1)
print('Element at index 3',fruits[3])

# Reading all elements in the array: O(n)
for fruit in fruits:
    print(fruit)


print(fruits)