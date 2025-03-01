from collections import Counter

def first_non_repeating_char(s):
    # Count the frequency of each character in the string
    char_count = Counter(s)
    
    # Iterate through the string to find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
    
    # If there is no non-repeating character, return None
    return None

# Example usage:
input_string = "swiss"
result = first_non_repeating_char(input_string)
print(f"The first non-repeating character is: {result}")
