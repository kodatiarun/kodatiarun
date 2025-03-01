def count_vowels(s):
    # Define the vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    
    # Initialize the counter to 0
    count = 0
    
    # Iterate through the string and check for vowels
    for char in s:
        if char in vowels:
            count += 1
    
    return count

# Example usage:
input_string = "Hello World"
result = count_vowels(input_string)
print(f"The number of vowels in '{input_string}' is: {result}")
