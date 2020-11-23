# %% Imports
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

import numpy as np

# %% Loading data
reviews = load_files('./movie_reviews', shuffle=True)
len(reviews.data)

# %% Split data into training and testing partitions
(x_train,
 x_test,
 y_train,
 y_test) = train_test_split(reviews.data, reviews.target,
                            test_size=0.20, random_state=12)

# %% Create and fit pipeline to data
pipe = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier(loss='hinge', penalty='l2',
                          alpha=1e-3, random_state=42, max_iter=5, tol=None)),
])

params = {
    'vect__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'clf__alpha': (1e-2, 1e-3),
}
gs_model = GridSearchCV(pipe, params, cv=5, n_jobs=-1)
gs_model.fit(x_train[:500], y_train[:500])

# %% Evaluate accuracy of pipeline without GS
pipe.fit(x_train[:500], y_train[:500])
y_pred = pipe.predict(x_test)
print('Pipeline accuracy without GS: ', np.mean(y_pred == y_test)) 

# %% Test model on some new data
new_reviews = [
    'The Lion King remake was not very good, but the music was okay.',
    'The boys has very good boys so it is a very good movie for boys.',
    'Ah yes, a letter from the Jarl. Moving up in the world, eh?',
    'I liked the movie. But the popcorn tasted terrible. 0/10!!!'
]

predicted = gs_model.predict(new_reviews)

for (review, sentiment) in zip(new_reviews, predicted):
    print('%s => %s' % (review, reviews.target_names[sentiment]))

# %% Print the optimal parameters found by the GridSearch algorithm
print("Best score for GS model: ", gs_model.best_score_)

print("\nParameters")
for param_name in sorted(params.keys()):
    print("%s: %r" % (param_name, gs_model.best_params_[param_name]))

