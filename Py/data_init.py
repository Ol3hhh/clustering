import pandas as pd

# Specified path to the JSON file
path = 'D:/My/Pwr/SolVro/recrutation/Source/cocktail_dataset.json'

# Loading the JSON file into a DataFrame
df = pd.read_json(path)

# Creating dictionaries to store categories, glasses, alcoholic status, tags, and ingredients
categories = {}
glasses = {}
alcoholic = {}
tags = {}
ingredients = {}

# Variables to track the number of categories, glasses, alcoholic status, tags, and ingredients
category_number = 1
glass_number = 1
alcoholic_number = 1
tag_number = 1
ingredient_number = 1

# Filling dictionaries
for index, row in df.iterrows():
    category = row['category']
    glass = row['glass']
    alc = row['alcoholic']
    tag_list = row['tags'] if 'tags' in row and row['tags'] else []
    ingredient_list = row['ingredients'] if 'ingredients' in row else []

    # Assigning a unique number for each category
    if category not in categories:
        categories[category] = category_number
        category_number += 1

    # Assigning a unique number for each glass
    if glass not in glasses:
        glasses[glass] = glass_number
        glass_number += 1

    # Assigning a unique number for each alcoholic status
    if alc not in alcoholic:
        alcoholic[alc] = alcoholic_number
        alcoholic_number += 1

    # Assigning unique numbers for each tag
    for tag in tag_list:
        if tag not in tags:
            tags[tag] = tag_number
            tag_number += 1

    # Assigning unique numbers for each ingredient (by ingredient name)
    for ingredient in ingredient_list:
        ingredient_name = ingredient['name'] if 'name' in ingredient else 'Unknown'
        if ingredient_name not in ingredients:
            ingredients[ingredient_name] = ingredient_number
            ingredient_number += 1
