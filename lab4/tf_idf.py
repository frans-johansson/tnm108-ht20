#%% Imports
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.naive_bayes import MultinomialNB

# Data set
from sklearn.datasets import fetch_20newsgroups

#%% Defining our documents, stop words and vocabulary
d1 = "The sky is blue."
d2 = "The sun is bright."
d3 = "The sun in the sky is bright."
d4 = "We can see the shining sun, the bright sun."
Z = (d1, d2, d3, d4)

my_stop_words = {"the", "is"}
my_vocabulary = {'blue': 0, 'sun': 1, 'bright': 2, 'sky': 3}
vectorizer = CountVectorizer(
    stop_words=my_stop_words, vocabulary=my_vocabulary)

#%% Printing the stop words and vocabulary list
print(vectorizer.vocabulary)
print(vectorizer.stop_words)

#%% Create a sparse matrix representing the document set Z
smatrix = vectorizer.transform(Z)
print(smatrix)

#%% IDF weights
tfidf_transformer = TfidfTransformer(norm="l2")
tfidf_transformer.fit(smatrix)

feature_names = vectorizer.get_feature_names()
df_idf = pd.DataFrame(tfidf_transformer.idf_, index=feature_names, columns=["idf_weights"])
df_idf

#%% Compute TF-IDF scores in matrix
tf_idf_vector = tfidf_transformer.transform(smatrix)
print(tf_idf_vector)

#%% Observe TF-IDF reults of first document
first_document = tf_idf_vector[0]

df = pd.DataFrame(first_document.T.todense(),
                  index=feature_names, columns=["first_doc"])
df.sort_values(by=["first_doc"], ascending=False)

#%% Use TF-IDF vectorizer to create a matrix
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(Z)
print(tfidf_matrix.shape)

#%% Calculate the cosine similarities between document 1 and the rest
cos_similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix)
print(cos_similarity)

#%% Classifying text from the 20 Newsgroups data set
my_categories = ['rec.sport.baseball','rec.motorcycles','sci.space','comp.graphics']
train = fetch_20newsgroups(subset='train', categories=my_categories)
test = fetch_20newsgroups(subset='test', categories=my_categories)

#%% Look at the data
print(train.data[1])
print(train.target[1])

#%% Vectorize with TF-IDF weighting and create model
cv = CountVectorizer()
X_train_counts = cv.fit_transform(train.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf=tfidf_transformer.fit_transform(X_train_counts)

model = MultinomialNB().fit(X_train_tfidf, train.target)
#%% Apply the model
docs_new = ['Pierangelo is a really good baseball player', 'Maria rides her motorcycle', 'OpenGL on the GPU is fast',
            'Pierangelo rides his motorcycle and goes to play football since he is a good football player too.']
X_new_counts = cv.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
predicted = model.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, train.target_names[category]))
