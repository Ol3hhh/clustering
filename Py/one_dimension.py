import numpy as np
import config as cf
import matplotlib.pyplot as plt




points = []

with open(cf.id_path, 'r') as read_file:
    for line in read_file:
        line = line.strip()  # Remove any leading/trailing whitespace or newlines
        points.append([int(line), 1])
        # Create a new 2D array with shape (1, 2) to represent the new row
        # Append the new row to points along axis 0 (vertically)

        # Print the current row for demonstration
points.append([5500, 1])
points = np.array(points)



class Kmeans:
    def __init__(self, k):
        self.k = k
        self.centroids = None

    @staticmethod
    def euclidian_distance(data_point, centroids):
        return np.sqrt(np.sum((data_point - centroids)**2, axis=1))

    def fit(self, x, max_iterations=2):
        self.centroids = np.random.uniform(np.amin(x), np.amax(x), (self.k, points.shape[1]))
        for i in range(len(self.centroids)):
            self.centroids[i][1] = 1

        for _ in range(max_iterations):
            cluster_nums = []

            for point in x:
                distances = self.euclidian_distance(self.centroids, point)
                cluster_num = np.argmin(distances)
                cluster_nums.append(cluster_num)


            cluster_nums = np.array(cluster_nums)
        return cluster_nums


kmeans = Kmeans(k=2)

labels = kmeans.fit(points)

plt.scatter(points[:, 0], points[:, 1], c=labels)
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c=range(len(kmeans.centroids)), marker='*', s=200)
plt.show()
