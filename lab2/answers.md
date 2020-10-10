# Lab 2, Supervised Learning

* Jonas Bertilsson (jonbe354)
* Frans Johansson (frajo752)

---

## Part 1, Linear Regression

### 1. *When can you use linear regression?*

When we want to predict some quantity based on other known quantities and the relationship, and the weights of each feature for this prediction are linearly independent of one another.

### 2. *How can you generalize linear regression models to account for more complex relationships among the data?*

By transforming the data set into a higher dimension with the use of a basis function.

### 3. *What are the basis functions?*

The function that transforms our data set. For example, a polynomial basis function could look something like fn(x)=x^n, which when applied to some single dimensional model {a0 + a1\*x} we get some new higher-dimensional model {a0 + a1\*x + a2\*x^2 + a3\*x^3 + ... + an\*x^n}.

### 4. *How many basis functions can you use in the same regression model?*

As many as you like, however too many basis functions can lead to worse results due to overfitting.

### 5. *Can overfitting be a problem? And if so, what can you do about it?*

Yes, it can be a problem. To alleviate this problem, we can use regularization to penalize overfitting.

---

## Part 2, K-Nearest Neighbor (KNN)

### 1. *Why is choosing a good value for k important in KNN?*

Since a KNN model is charactarised completely by the choice of k (determining how many neighboring data points will vote when classifying new data), a good or bad value for k will make or break the model.

From the tutorial PDF: "In the case of a small number k, the noise will have a higher influence on the result.
Large value of k makes the algorithm computationally expensive. Also small values for k produce
models with the most flexible fit which will have low bias but high variance. Instead, a large value
of k will produce a smoother decision boundary with lower variance but higher bias."

### 2. *How can you decide a good value for k?*

A good starting point in choosing a k value is that it can't be a multiple of the number of classes you have. The elbow method can also be used to genereate a good K-value.

### 3. *Can you use KNN to classify non-linearly separable data?*

Yes.

### 4. *Is KNN sensitive to the number of features in the dataset?*

KNN will generally perform better with fewer features. As the number of dimensions increases, the probability of overfitting the model increases as well. This can, however, be addressed with more data.

### 5. *Can you use KNN for a regression problem?*

Yes, it can be used for both regression and classification problems. For regression problems, simply let the predicted value be the average of the K nearest neighbors' values.

### 6. *What are the Pros and Cons of KNN?*

**Pros:**
* It's faster to train, due to it being a lazy learner
* KNN is a versitile model, being able to handle non-linearities well as well as not being limited to regression or classification problems. 

**Cons:**
* The testing phase of KNN is slwoer and costlier in terms of time and memory. 
* It requires large memory for storing the entire training dataset
* If the Euclidean distance measure is used it requires rescaling of the data set. It will also be sensitive to magnitudes, features with high magnitudes will wheigt more then features with low magnitudes.
* It is not suitable for large dimensional data sets.

---

## Part 3, Support Vector Machines (SVM)

### 1. *What is the basic idea/intuition of SVM?*

To separate our data with a hyperplane (or line if the data is two dimensional) which has been selected such that the margin to nearby data points is as large as possible. 

### 2. *What can you do if the dataset is not linearly separable?*

(TODO: Get back to this question after recapping the lecture on SVMs)

You can project the data into a higher dimension, however this method can become very computationally expensive as the data sets grows. This can be effectively implemented using the "kernel trick", allowing us to implicitly fit the higher-dimensional data using kernel functions without hefty computations.One example of such a kernel function is the RBF (radial basis function).

### 3. *Explain the concept of Soften Margins*

We can allow some amount of data points to lie within the margins, which may lead to a better fit in the end. The "softnest" of the margin is related to the C varible. A large C results a hard margin and a small value of C results in a soft marging.

### 4. *What are the pros and cons of SVM?*

**Pros:**
* Depending only on a relatively small amount of support vectors (vectors on the margin border) makes an SVM model compact.
* Since SVM is an eager learner, prediction happens very fast in the testing phase
* Being able to use a variety of kernel functions make the algorithm highly versatile.

**Cons:**
* The computational cost can be prohibitive for large number of traning samples. At worst O(N^3) or O(N^2)
* The results are strongly tied to the softening parameter C. Which can be expensive to choose in large datasets.
* It's hard interpret if the results is correct or not and it's expensive to do a interal cross-validiation. 

"The results do not have a direct probabilistic interpretation??" que