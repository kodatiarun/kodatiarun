def find_missing_number(lst, n):
    # Calculate the expected sum of numbers from 1 to n
    total_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of the numbers in the given list
    actual_sum = sum(lst)
    
    # The missing number is the difference between the total sum and the actual sum
    missing_number = total_sum - actual_sum
    
    return missing_number

# Example usage:
n = 10  # The range of numbers should be from 1 to 10
my_list = [1, 2, 3, 4, 6, 7, 8, 9, 10]  # Missing number is 5
missing = find_missing_number(my_list, n)
print(f"The missing number is: {missing}")
