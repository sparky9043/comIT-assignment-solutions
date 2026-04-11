# Example of list

fruits = ['apple', 'banana', 'grapes', 'tomato']

# Appending to the end of the list: O(1)
fruits.append('kiwi')
print('Append to the end of list:', fruits)

# Inserting to or deleting the beginning of the list: O(n) due to shift
fruits.insert(0, 'mango')
print('Insert to the beginning', fruits)
fruits.remove('mango')
print('Remove from the beginning', fruits)

# Reading one element inside an array: O(1)
print('Reading element at index 3',fruits[3])

# Reading all elements in the array: O(n)
for index, fruit in enumerate(fruits):
    print(f"Display index {index}", fruit)
