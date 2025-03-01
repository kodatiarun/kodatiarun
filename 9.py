def intersection_of_lists(list1, list2):
    # Convert both lists to sets and use the intersection method
    return list(set(list1) & set(list2))

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = intersection_of_lists(list1, list2)
print(f"The intersection of the lists is: {result}")
