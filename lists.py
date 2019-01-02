#######
# Lists
#######

# The following content is based on Erc Matthe's book, 'Python crash course' from 2016.

# 'A list is a collection of items in a particular order' (p.37).
# Lists are indicated by bracets ([]).

numbers = ['zero', 'one', 'two', 'N']
print(numbers)

# Select part of a list.
print(numbers[1])

# The last item can always be accessed via -1
print(numbers[-1])

# Slicing a list
print(numbers[0:3])

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


### Sorting ### 

# Sorting a list.
numbers.sort()
print(numbers)

# Reverse sorting.
numbers.sort(reverse=True)
print(numbers)

# Sort list non temporary.
# The previous commands change the order of the list.
# To avoid this issue, sorted() can be used.

numbers = ['zero', 'one', 'two', 'N']

print(
	'Sorted: ' +str(sorted(numbers))
	)

print(
	'Sorted reverse: '
	+str(sorted(numbers, reverse=True)))

# Length of a list
print(len(numbers))

# Looping though lists

# Print all objects in list 'numbers' 
for i in numbers:
	print(i)

# Create numerical list
# Have in mind the 'off-by-one' behavior.
# The list stops before 5.
list_a = []
for i in range(1,5):
	list_a.append(i)
print(list_a)

# Simpler solution.
list_b = list(range(1,5))
print(list_b) 

# Copy a list
numbers_copy = numbers
print(numbers_copy)