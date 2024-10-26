from data_init import df, categories, glasses, alcoholic, tags, ingredients


# Kmeans class for initializing points based on data
class Clustering:
    def __init__(self):
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
            ingredient_nums = [ingredients[ingredient['name']] for ingredient in df.loc[i, 'ingredients']] if df.loc[
                i, 'ingredients'] else []
            # Append the ingredients as their own list in the existing point structure
            self.points[i].append(ingredient_nums)
        return self.points

    def compare(self, point):
        similar = []
        bm = 0  # biggest matches
        for ix, pt in enumerate(self.points):
            if point == pt:
                continue
            matches = [
                sum(1 for x, y in zip(pt[1:4], point[1:4]) if x == y),
                sum(1 for x in pt[4] if x in point[4]),
                sum(1 for x in pt[5] if x in point[5])
            ]
            matches = sum(matches)
            if bm <= matches:
                if bm < matches:
                    similar.clear()
                    bm = matches
                similar.append(pt)
        return similar


# Initialize Kmeans and points
clustering = Clustering()
points = clustering.points_init()
