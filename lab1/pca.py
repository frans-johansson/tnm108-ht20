#%% Imports and loading data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

#%% Scale data to be "standardized"
scaler = StandardScaler()
scaler.fit(cancer.data)
X = scaler.transform(cancer.data)

#%% Perform PCA
pca=PCA(n_components=3)
pca.fit(X)
X_pca=pca.transform(X)

#%% Function to plot components
def plot_components(x, y):
    Xax = X_pca[:, x]
    Yax = X_pca[:, y]
    labels = cancer.target
    cdict = {0: 'red', 1: 'green'}
    labl = {0: 'Malignant', 1: 'Benign'}
    marker = {0: '*', 1: 'o'}
    alpha = {0: .3, 1: .5}
    fig, ax = plt.subplots(figsize=(7, 5))
    fig.patch.set_facecolor('white')
    for l in np.unique(labels):
        ix = np.where(labels == l)
        ax.scatter(Xax[ix], Yax[ix], c=cdict[l], s=40,
                   label=labl[l], marker=marker[l], alpha=alpha[l])
    plt.xlabel(f"Principal component: {x+1}", fontsize=14)
    7
    plt.ylabel(f"Principal component: {y+1}", fontsize=14)
    plt.legend()
    plt.show()

#%% Scatter plots
plot_components(0,1)
plot_components(0,2)
plot_components(1,2)

#%% Find the most relevant features for the first PC
idx_slice = np.argsort(pca.components_[0,:])[-4:]
cancer.feature_names[idx_slice]
