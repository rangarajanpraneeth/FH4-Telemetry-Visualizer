import json
import os

def get_file_path(file):   
    current_directory = os.path.dirname(os.path.abspath(__file__))
    database_directory = os.path.join(current_directory, '..', '..', 'database')
    file_path = os.path.join(database_directory, file)
    return file_path

def getJSON(file_name):
    file_path = get_file_path(file_name)
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in '{file_path}'. Check the file format.")
        return None

def uploadJSON(file_name, data):
    file_path = get_file_path(file_name)
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        print(f"Data successfully uploaded to '{file_path}'.")
    except Exception as e:
        print(f"Error: Unable to upload data to '{file_path}'. {e}")

# Example Usage:
# Assuming you have a file named 'example.json' with {"key": "value"}
file_data = getJSON('test.json')
print("Data from JSON file:", file_data)

# Modify the data if needed
if file_data:
    file_data['new_key'] = 'new_value'

# Upload the modified data
uploadJSON('example.json', file_data)
