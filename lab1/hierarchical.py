#%% Handle imports and loading data
import requests
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

url = 'http://dellacqua.se/education/courses/tnm108/material/labs/Lab%201/shopping_data.csv'
user, password = 'pizza', 'margherita'
response = requests.get(url, auth=(user, password))

customer_data = pd.read_csv(StringIO(response.text))

#%% Example plotting
X = np.array([[5, 3],
              [10, 15],
              [15, 12],
              [24, 10],
              [30, 30],
              [85, 70],
              [71, 80],
              [60, 78],
              [70, 55],
              [80, 91]])

labels = range(1, 11)
plt.figure(figsize=(10, 7))
plt.subplots_adjust(bottom=0.1)

plt.scatter(X[:, 0], X[:, 1], label='True Position')

for label, x, y in zip(labels, X[:, 0], X[:, 1]):
    plt.annotate(label, xy=(x, y), xytext=(-3, 3),
                 textcoords='offset points', ha='right', va='bottom')
plt.show()

#%% Plot dendograms for example
linked = linkage(X, 'single')
labelList = range(1, 11)
plt.figure(figsize=(10, 7))
dendrogram(linked,
           orientation='top',
           labels=labelList,
           distance_sort='descending',
           show_leaf_counts=True)
plt.show()

#%% Run the algorithm with SKLearn
cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
cluster.fit_predict(X)

plt.scatter(X[:,0],X[:,1], c=cluster.labels_, cmap='rainbow')
plt.show()

#%% Look at shopping data
customer_data.head()

#%% Shopping data example
data = customer_data.iloc[:, 3:5].values
# data = customer_data.iloc[:, 2:4].values

linked = linkage(data, 'single')
labelList = range(0, len(data))
plt.figure(figsize=(10, 7))
dendrogram(linked,
           orientation='top',
           labels=labelList,
           distance_sort='descending',
           show_leaf_counts=False)
plt.show()

#%% Shopping data continued
cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster.fit_predict(data)

# Plotting spending score (y) by annual income (x)
plt.scatter(data[:,0],data[:,1], c=cluster.labels_, cmap='rainbow')
plt.show()