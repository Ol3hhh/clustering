import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from Py.train import matches

# Вказаний шлях до JSON-файлу
path = 'D:/My/Pwr/SolVro/recrutation/Source/cocktail_dataset.json'

# Завантаження JSON-файлу в DataFrame
df = pd.read_json(path)

# Створення словників для збереження категорій, склянок, алкогольного статусу, тегів та інгредієнтів
categories = {}
glasses = {}
alcoholic = {}
tags = {}
ingredients = {}

# Змінні для відстеження номеру категорії, склянки, алкогольного статусу, тегів, та інгредієнтів
category_number = 1
glass_number = 1
alcoholic_number = 1
tag_number = 1
ingredient_number = 1

for index, row in df.iterrows():
    category = row['category']
    glass = row['glass']
    alc = row['alcoholic']
    tag_list = row['tags'] if 'tags' in row and row['tags'] else []
    ingredient_list = row['ingredients'] if 'ingredients' in row else []

    # Призначаємо унікальний номер для кожної категорії
    if category not in categories:
        categories[category] = category_number
        category_number += 1

    # Призначаємо унікальний номер для кожної склянки
    if glass not in glasses:
        glasses[glass] = glass_number
        glass_number += 1

    # Призначаємо унікальний номер для кожного алкогольного статусу
    if alc not in alcoholic:
        alcoholic[alc] = alcoholic_number
        alcoholic_number += 1

    # Призначаємо унікальні номери для кожного тегу
    for tag in tag_list:
        if tag not in tags:
            tags[tag] = tag_number
            tag_number += 1

    # Призначаємо унікальні номери для кожного інгредієнта (за назвою інгредієнта)
    for ingredient in ingredient_list:
        ingredient_name = ingredient['name'] if 'name' in ingredient else 'Unknown'
        if ingredient_name not in ingredients:
            ingredients[ingredient_name] = ingredient_number
            ingredient_number += 1


# Клас Kmeans для ініціалізації точок на основі даних
class Kmeans:
    def __init__(self, k):
        self.k = k
        self.points = []  # General points

    def points_init(self):
        self.points_name()
        self.points1_init()
        self.points2_init()
        self.points3_init()
        return self.points

    def points_name(self):
        for i in range(len(df)):
            self.points.append([df.loc[i, 'name']])

    def points1_init(self):
        for i in range(len(df)):
            self.points[i].append(categories[df.loc[i, 'category']])
            self.points[i].append(glasses[df.loc[i, 'glass']])
            self.points[i].append(alcoholic[df.loc[i, 'alcoholic']])

        return self.points

    def points2_init(self):
        for i in range(len(df)):
            tag_nums = [tags[tag] for tag in df.loc[i, 'tags']] if df.loc[i, 'tags'] else []
            # Append the tags as their own list in the existing point structure
            self.points[i].append(tag_nums)

        return self.points

    def points3_init(self):
        for i in range(len(df)):
            ingredient_nums = [ingredients[ingredient['name']] for ingredient in df.loc[i, 'ingredients']] if df.loc[i, 'ingredients'] else []
            # Append the ingredients as their own list in the existing point structure
            self.points[i].append(ingredient_nums)

        return self.points

    def compare(self, point):

        def mcount(x):
            return sum(x) / len(x)
        similar = []
        matches = []
        bm = 0 # biggest matches

        for ix, pt in enumerate(self.points):
            if point == pt:
                continue
            matches = []
            matches.append(sum(1 for x, y in zip(pt[1:4], point[1:4]) if x == y))
            matches.append(sum(1 for x in pt[4] if x in point[4]))
            matches.append(sum(1 for x in pt[5] if x in point[5]))
            print(pt, matches)
            matches = sum(matches)
            if bm <= matches:
                if bm < matches:
                    similar.clear()
                    bm = matches
                similar.append(pt)

        print()
        return similar


kmeans = Kmeans(2)
points = kmeans.points_init()

print(points[0])


print(kmeans.compare(points[7]))










