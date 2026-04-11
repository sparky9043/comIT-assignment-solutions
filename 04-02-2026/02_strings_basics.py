# String Implementation

# Inefficient Rebuilding of string: O(n^2)
result = ""
chars = "inefficient example"
for index, char in enumerate(chars):
    result += char
    print(f"Number of strings created count: {index + 1}", result)
print(f"{index + 1} strings created", result)

# A more efficient way to rebuild strings: O(n)
result = []
chars = 'much more efficient'
for char in chars:
    result.append(char)
    print(result)
print(''.join(result))
print(f'The above method is much more efficient because you '
      f'only created one list and joined at the end into one string')