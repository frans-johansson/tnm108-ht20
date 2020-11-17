#%%
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_olivetti_faces
from sklearn.utils.validation import check_random_state

from sklearn.ensemble import ExtraTreesRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV

# Load the faces datasets
data, targets = fetch_olivetti_faces(return_X_y=True)

train = data[targets < 30]
test = data[targets >= 30]  # Test on independent people / Testar på folk som inte har deltagit i träningsfasen

# Test on a subset of people
n_faces = 5
rng = check_random_state(3)
face_ids = rng.randint(test.shape[0], size=(n_faces, ))
test = test[face_ids, :]

n_pixels = data.shape[1]
# Upper half of the faces
X_train = train[:, :(n_pixels + 1) // 2]
X_test = test[:, :(n_pixels + 1) // 2]
# Lower half of the faces
y_train = train[:, n_pixels // 2:]
y_test = test[:, n_pixels // 2:]

#%%
# Fit estimators
ESTIMATORS = {
    "Extra trees": ExtraTreesRegressor(n_estimators=10, max_features=32,
                                       random_state=0),
    "K-nn": KNeighborsRegressor(),
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),
}

# Additional estimators
ADDITIONAL_ESTIMATORS = {
    "Tree, d=10, f=50": DecisionTreeRegressor(max_depth=10, max_features=50, random_state=0),
    "Tree, d=20, f=50": DecisionTreeRegressor(max_depth=20, max_features=50, random_state=0),
    "Tree, d=20, f=25": DecisionTreeRegressor(max_depth=20, max_features=25, random_state=0),
    "Forest, d=10, f=50": ExtraTreesRegressor(max_depth=10, max_features=50, random_state=0),
    "Forest, d=20, f=50": ExtraTreesRegressor(max_depth=20, max_features=50, random_state=0),
    "Forest, d=20, f=25": ExtraTreesRegressor(max_depth=20, max_features=25, random_state=0),
}

y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train, y_train)
    y_test_predict[name] = estimator.predict(X_test)

y_test_additional_predict = dict()
for name, estimator in ADDITIONAL_ESTIMATORS.items():
    estimator.fit(X_train, y_train)
    y_test_additional_predict[name] = estimator.predict(X_test)

#%%
# Plot the completed faces
def plot_faces(estimators, predictions):
    image_shape = (64, 64)
    n_cols = 1 + len(estimators)
    plt.figure(figsize=(2. * n_cols, 2.26 * n_faces))
    plt.suptitle("Face completion with multi-output estimators", size=16)

    for i in range(n_faces):
        true_face = np.hstack((X_test[i], y_test[i]))

        if i:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 1)
        else:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 1,
                            title="true faces")

        sub.axis("off")
        sub.imshow(true_face.reshape(image_shape),
                cmap=plt.cm.gray,
                interpolation="nearest")

        for j, est in enumerate(sorted(estimators)):
            completed_face = np.hstack((X_test[i], predictions[est][i]))

            if i:
                sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j)
            else:
                sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j,
                                title=est)

            sub.axis("off")
            sub.imshow(completed_face.reshape(image_shape),
                    cmap=plt.cm.gray,
                    interpolation="nearest")

    plt.show()


plot_faces(ESTIMATORS, y_test_predict)
plot_faces(ADDITIONAL_ESTIMATORS, y_test_additional_predict)

# Notes on what the program does:
# Delar upp bilderna i över och undre del sedan använder man
# övre halvan för att predicta den undre halvan

# Notes on performance:
#   * Linear regression, very noisy and also quite unsettling results
#   * Ridge, something about the mouths seem off, the faces look leathery
#   * KNN, decent results but the facial features don't always line up correctly
#   * Extra trees, best performance overall

# Notes on the additional estimators:
# The results for the extra reggrsions trees are weird the program has choosen 
# the wrong lower half. We think thats because it just chooses a random lower half 
# that fits.

# Last question:
# Use haar features to compare the more important parts of the picture like the nose bridge area
# since thats where you can see a big difference beteween the faces
