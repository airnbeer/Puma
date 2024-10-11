def sort_key(input_dict, key_to_remove):
    sorted_dict = dict(sorted(input_dict.items()))
    sorted_dict.pop(key_to_remove, None)
    return sorted_dict

try:
    sample_dict = dict(input("Enter key-value pairs for the dictionary (comma-separated): ").split(','))
    key_to_remove = input("Enter the key to remove: ")
    
    result_dict = sort_key(sample_dict, key_to_remove)
    print("Sorted and Key Removed Dictionary:", result_dict)

except ValueError:
    print("Error: Please enter valid key-value pairs for the dictionary.")
