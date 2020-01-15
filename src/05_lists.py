# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(f"APPEND 4: {x}")

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
for i in y:
    x.append(i)
print("APPEND Y DIGITS:", x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print("REMOVE 8:", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
index_of_nine = x.index(9) + 1
x.insert(index_of_nine, 99)
print(f"ADD 99: {x}")

# Print the length of list x
# YOUR CODE HERE
print(f"LENGTH OF X: {len(x)}")

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in x:
    print(i * 1000)
