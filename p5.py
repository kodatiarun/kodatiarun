def remove_duplicates(lst):
    # Create an empty list to store the result
    result = []
    
    # Iterate through the original list
    for item in lst:
        # Add item to result if it's not already in the result list
        if item not in result:
            result.append(item)
    
    return result

# Example usage:
my_list = [1, 2, 2, 3, 4, 1, 5, 3]
result = remove_duplicates(my_list)
print(f"List after removing duplicates: {result}")

