import json
import pickle

# # Sample Python object
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
#
# Serialize to a JSON string
json_string = json.dumps(data,indent=5)

# Save JSON string to a file
with open('data.json', 'w') as file:
    file.write(json_string)
#
# with open('data.json', 'r') as file:
#     file1 = json.load(file)
#     print(file1)

# Deserialize (unpickle) an object from a binary file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

print(loaded_data)  # Output: The original object (e.g., a dictionary, list, etc.)

