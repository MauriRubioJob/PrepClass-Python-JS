import functools

# Recursion
# A function that calls itself.

# Fibonacci sequence
# 1, 1, 2, 3, 5, 8, 13, 21, 34

counter = 0

@functools.lru_cache()
def fibonacci(n):
    global counter
    counter = counter + 1
    # print("Calculating the fibonacci", n)

    if n <= 1:
        # print("Returning value.")
        return 1
    else:
        # Calculate and cache the number
        return fibonacci(n - 1) + fibonacci(n - 2)


# Solution to recursive problem is cache
print("Fibonacci term", fibonacci(300))
print("Function was called", counter, "times")
