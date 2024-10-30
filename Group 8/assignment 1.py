def reverse_string(s):
    # Print the original string for debugging
    print("Original string:", s)
    reversed_s = s[::-1]
    print("Reversed string (inside function):", reversed_s)  # Debug print inside function
    return reversed_s

# Take input from the user
user_input = input("Hello Doris: ")
print("User input received:", user_input)  # Confirm input

# Call the function and print the result
reversed_string = reverse_string(user_input)
print("Reversed string:", reversed_string)



def is_palindrome(word):
    # Normalize the word by converting it to lowercase
    normalized_word = word.lower()
    
    # Check if the normalized word is the same forwards and backwards
    return normalized_word == normalized_word[::-1]

# Example usage:
print(is_palindrome("Racecar"))  # Output: True
print(is_palindrome("Hello"))    # Output: False


def Fibonacci(n):
    # Initialize the list to store Fibonacci sequence
    fib_sequence = []

    # Generate Fibonacci numbers
    for i in range(n):
        if i == 0:
            fib_sequence.append(0)  # First Fibonacci number
        elif i == 1:
            fib_sequence.append(1)  # Second Fibonacci number
        else:
            # Each subsequent number is the sum of the two preceding ones
            next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_fib)

    return fib_sequence


# Example usage:
print(Fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

