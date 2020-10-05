#%% Imports and reading CSV data
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv('./train.csv')
test = pd.read_csv('./test.csv')

#%% Impute missing data with mean values
train.fillna(train.mean(), inplace=True)
test.fillna(test.mean(), inplace=True)
 
#%% Plot some stuff with Seaborn
g = sns.FacetGrid(train, col='Survived')
g.map(plt.hist, 'Fare', bins=20)

#%% Column values
train.columns.values

#%% Examine which data fields seem relevant
field = 'Fare'
train[[field, 'Survived']].groupby(field).mean().sort_values(by='Survived', ascending=False)

#%% Drop insignificant data
test = test.drop(['Name', 'Ticket', 'Cabin', 'Embarked', 'Fare', 'Parch', 'SibSp'], axis=1)
train = train.drop(['Name','Ticket' ,'Cabin' ,'Embarked', 'Fare', 'Parch', 'SibSp'], axis=1)

#%% Transform 'Sex' column into numeric values using Label Encoding
labelEncoder = LabelEncoder()
labelEncoder.fit(train['Sex'])
labelEncoder.fit(test['Sex'])
train['Sex'] = labelEncoder.transform(train['Sex'])
test['Sex'] = labelEncoder.transform(test['Sex'])

#%% Training our K-Means model
X = np.array(train.drop(['Survived'], 1).astype(float))
y = np.array(train['Survived'])

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=2, max_iter=1800, algorithm='auto') # Two clusters, survived/died
kmeans.fit(X_scaled)

#%% Checking how good our model is
correct = 0

for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = kmeans.predict(predict_me)
    if prediction[0] == y[i]:
        correct += 1
    
correct / len(X)

#%% How many percent died?
1 - train['Survived'].sum()/len(train)