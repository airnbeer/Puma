def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

try:
    dict1_keys = input("Enter keys for the first dictionary (comma-separated): ").split(',')
    dict1_values = input("Enter values for the first dictionary (comma-separated): ").split()
    
    dict1 = dict(zip(dict1_keys, dict1_values))
except ValueError:
    print("Error: Please enter valid key-value pairs for the first dictionary.")

try:
    dict2_keys = input("Enter keys for the second dictionary (comma-separated): ").split(',')
    dict2_values = input("Enter values for the second dictionary (comma-separated): ").split()
    
    dict2 = dict(zip(dict2_keys, dict2_values))
except ValueError:
    print("Error: Please enter valid key-value pairs for the second dictionary.")

merged_dict = merge_dicts(dict1, dict2)
print("Merged Dictionary:", merged_dict)
