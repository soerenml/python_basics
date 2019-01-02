#######
# Lists
#######

# 'A list is a collection of items in a particular order' (p.37).
# Lists are indicated by bracets ([]).

numbers = ['zero', 'one', 'two', 'N']
print(numbers)

# Select part of a list.
print(numbers[1])

# The last item can always be accessed via -1
print(numbers[-1])

# Elements can be changed.
numbers[3] = 'last_item'
print(numbers)

# Adding elements to the list.
numbers.append('last_item+1')
print(numbers)

# Insert element into a specific position.
numbers.insert(0, 'zero-1')
print(numbers)

# Delete a number from a list.
del numbers[0]
print(numbers)

# Remove item by value.
numbers.remove('last_item+1')
print(numbers)

# Sorting a list.
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)