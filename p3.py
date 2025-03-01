from collections import Counter

def most_frequent_element(lst):
    # Use Counter to count occurrences of each element
    counter = Counter(lst)
    
    # Find the element with the highest frequency
    most_common_element, frequency = counter.most_common(1)[0]
    
    return most_common_element

# Example usage:
my_list = [1, 3, 3, 2, 1, 1, 4, 3, 5]
result = most_frequent_element(my_list)
print(f"The most frequent element is: {result}")
