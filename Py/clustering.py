from data_init import df, categories, glasses, alcoholic, tags, ingredients

# Clustering class that initializes points and provides comparison functionality
class Clustering:
    def __init__(self):
        self.points = []  # List to store all points representing cocktails

    # Initialize all points with names and attributes for clustering
    def points_init(self):
        self.points_name()
        self.points1_init()
        self.points2_init()
        self.points3_init()
        return self.points

    # Initialize points with names of cocktails
    def points_name(self):
        for i in range(len(df)):
            self.points.append([df.loc[i, 'name']])

    # Initialize points with category, glass, and alcoholic status
    def points1_init(self):
        for i in range(len(df)):
            self.points[i].append(categories[df.loc[i, 'category']])
            self.points[i].append(glasses[df.loc[i, 'glass']])
            self.points[i].append(alcoholic[df.loc[i, 'alcoholic']])
        return self.points

    # Initialize points with tags as a list of unique tag identifiers
    def points2_init(self):
        for i in range(len(df)):
            tag_nums = [tags[tag] for tag in df.loc[i, 'tags']] if df.loc[i, 'tags'] else []
            self.points[i].append(tag_nums)
        return self.points

    # Initialize points with ingredients as a list of unique ingredient identifiers
    def points3_init(self):
        for i in range(len(df)):
            ingredient_nums = [ingredients[ingredient['name']] for ingredient in df.loc[i, 'ingredients']] if df.loc[i, 'ingredients'] else []
            self.points[i].append(ingredient_nums)
        return self.points

    # Compare the selected cocktail with others to find similar cocktails based on attributes
    def compare(self, point):
        similar = []
        max_matches = 0  # Track maximum matches for best similarity
        for pt in self.points:
            if point == pt:
                continue
            matches = [
                sum(1 for x, y in zip(pt[1:4], point[1:4]) if x == y),  # Match category, glass, and alcoholic status
                sum(1 for x in pt[4] if x in point[4]),  # Match tags
                sum(1 for x in pt[5] if x in point[5])  # Match ingredients
            ]
            total_matches = sum(matches)
            if max_matches <= total_matches:
                if max_matches < total_matches:
                    similar.clear()
                    max_matches = total_matches
                similar.append(pt)
        return similar


# Initialize clustering and points
clustering = Clustering()
points = clustering.points_init()
