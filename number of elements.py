# Define the number of elements in the Fibonacci series
n = 50

# Initialize the first two Fibonacci numbers
fib_series = [0, 1]

# Use a lambda function along with a list comprehension to generate the Fibonacci series
fibonacci = lambda n: fib_series.append(fib_series[-1] + fib_series[-2]) if len(fib_series) < n else None
# The lambda function appends the sum of the last two elements of the list to the list itself

# Generate the Fibonacci series up to n elements
for _ in range(2, n):
    fibonacci(n)

# Print the Fibonacci series
print(fib_series)
