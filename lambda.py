# Define a list containing a mix of integers and strings
data = [10, 'hello', 22, 'world', 37, 'python']

# Define a lambda function to check if an element is an integer or a string
check_type = lambda x: isinstance(x, int) or isinstance(x, str)

# Apply the lambda function to every element in the list using the all() function
# The all() function returns True if all elements in the iterable are true
# It returns False if any element in the iterable is false
all_elements_checked = all(check_type(element) for element in data)

# Print the result
if all_elements_checked:
    print("All elements in the list are either integers or strings.")
else:
    print("The list contains elements other than integers or strings.")
