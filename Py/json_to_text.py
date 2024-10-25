import pandas as pd

# Define the file paths
json_file_path = 'D:/My/Pwr/SolVro/recrutation/Source/cocktail_dataset.json'
txt_file_path = 'D:/My/Pwr/SolVro/recrutation/Source/cocktail_dataset.txt'

# Read the JSON file into a DataFrame
df = pd.read_json(json_file_path)

# Write the DataFrame to a text file, converting to JSON format
with open(txt_file_path, 'w') as txt_file:
    # Use the 'to_json' method with 'lines=True' to separate entries
    # Then replace '}' with '}\n' to add a newline after every '}'
    formatted_data = df.to_json(orient='records', lines=True).replace('}', '}\n')
    txt_file.write(formatted_data)
