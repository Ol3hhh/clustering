import config as cf
import numpy as np
import matplotlib.pyplot as plt

points = []

# Dictionaries to map categories and glass types to indices
category_dict = {}
glass_dict = {}

category_list = []
glass_list = []

# Read category and glass files, and populate lists and dictionaries
with open(cf.category_path, 'r') as category_file, open(cf.glass_path, 'r') as glass_file:
    category_index = 1
    glass_index = 1
    for index, (cat, glass) in enumerate(zip(category_file, glass_file)):  # cat - category line
        cat = cat.strip()
        glass = glass.strip()

        if cat not in category_dict:
            category_dict[cat] = category_index
            category_index += 1

        if glass not in glass_dict:
            glass_dict[glass] = glass_index
            glass_index += 1

        category_list.append(category_dict[cat])
        glass_list.append(glass_dict[glass])
        points.append([glass_list[index], category_list[index]])

# Convert points to a NumPy array for Kmeans
points = np.array(points)

class Kmeans:
    def __init__(self, points, k):
        self.points = points
        self.k = k
        self.centroids = self.centroids()

    def centroids(self):
        # Randomly choose `k` points from the dataset as initial centroids
        random_indices = np.random.choice(self.points.shape[0], self.k, replace=False)
        centroids = self.points[random_indices]
        return centroids

    @staticmethod
    def distance(point, centroids):
        return np.sqrt(np.sum((point - centroids) ** 2, axis=1))

    def fit(self, centroids):
        cluster_nums = []
        for point in self.points:
            distance = self.distance(point, centroids)
            cluster_num = np.argmin(distance)
            cluster_nums.append(cluster_num)
        return cluster_nums




# Initialize Kmeans with 3 clusters
kmeans = Kmeans(points, 3)

# Print initial centroids
centroids = kmeans.centroids
print(centroids)

# Scatter plot of the points
plt.scatter(points[:, 0], points[:, 1])

# Scatter plot of the initial centroids
labels = kmeans.fit(centroids)
plt.scatter(points[:, 0], points[:, 1], c=labels)
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c=range(len(kmeans.centroids)), marker='*', s=200)
plt.show()
