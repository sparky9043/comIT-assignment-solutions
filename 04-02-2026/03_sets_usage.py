# Using sets

numbers = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5, 6, 6]

print('List of numbers (not set):', numbers)

numbers_set = set(numbers)

print('Converting to sets (Displaying uniques only):', numbers_set)

# Checking to see if an item exists: O(1)
print('Is the number 2 in the list?', 2 in numbers_set)
print('Is the number 1 in the list?', 1 in numbers_set)
print('Is the number 3 in the list?', 3 in numbers_set)
print('Is the number -5 in the list?', -5 in numbers_set)
print('Is the number 10 in the list?', 10 in numbers_set)