import numpy as np
import matplotlib.pyplot as plt

points = np.random.uniform(0, 100000, size=(10000, 3))
print(points)
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

        for _ in range(100):
            cluster_nums = []
            for point in self.points:
                distance = self.distance(point, centroids)
                cluster_num = np.argmin(distance)
                cluster_nums.append(cluster_num)
        return cluster_nums




# Initialize Kmeans with 3 clusters
kmeans = Kmeans(points, 5)

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