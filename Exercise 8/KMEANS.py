import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Define data points (add more for better clustering)
X = np.array([[1, 2], [2, 3], [3, 4], [5, 5], [6, 7], [8, 9]])

# Create KMeans model with 2 clusters
m = KMeans(n_clusters=2, random_state=42)
m.fit(X)

# Plot data points with color-coding for clusters
plt.scatter(X[:, 0], X[:, 1], c=m.labels_, cmap='viridis', label="Data Points")
# Plot cluster centers
plt.scatter(m.cluster_centers_[:, 0], m.cluster_centers_[:, 1], s=200, c='red', marker='X', label="Cluster Centers")

plt.title("KMeans Clustering with Cluster Centers")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()