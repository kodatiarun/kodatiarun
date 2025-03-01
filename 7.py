def second_largest(lst):
    # Remove duplicates by converting to a set and back to a list
    lst = list(set(lst))
    
    # If the list has fewer than two unique numbers, return None (no second largest)
    if len(lst) < 2:
        return None
    
    # Sort the list in descending order and return the second largest
    lst.sort(reverse=True)
    
    return lst[1]

# Example usage:
my_list = [12, 35, 1, 10, 34, 1]
result = second_largest(my_list)
print(f"The second largest number is: {result}")
