# -*- coding: utf-8 -*-
"""Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

# Model that predicts which passengers survived the titanic ship

# Import Libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.naive_bayes import GaussianNB

from sklearn.svm import SVC


from sklearn.metrics import accuracy_score

data_train = pd.read_csv('train.csv')
data_test = pd.read_csv('test.csv')

"""# Explore Data"""

print(data_train.head(5))

print(data_train.tail(5))

data_train.sample(1)

data_train.shape

data_train.info()

data_train.describe()

data_train.isnull()

data_train.isnull().sum()

nu = data_train.isnull().sum()
nu[nu>0]

sns.heatmap(data_train.isnull())

"""# Clean Data"""

def Clean(data):
  data.drop(['Cabin','Name','Ticket','Embarked','Fare'],axis=1,inplace=True) # delete colomns
  data.Age = data.Age.fillna(data.Age.median())
  data.dropna()
  return data

Clean(data_train)

Clean(data_test)

sns.heatmap(data_train.isnull())

sns.heatmap(data_test.isnull())

"""# Transform Data

"""

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

le.fit(data_train['Sex'])
le.transform(data_train['Sex'])
data_train['Sex'] = le.transform(data_train['Sex'])

data_train.head(5)

le.fit(data_test['Sex'])
le.transform(data_test['Sex'])
data_test['Sex'] = le.transform(data_test['Sex'])

data_test.head(5)

"""# Data Analysis"""

data_train.corr()

sns.heatmap(data_train.corr(),annot=True,fmt='.1f',linewidths=5)

data_train.Survived.value_counts()

data_train.Sex.value_counts()

from enum import auto
data_train.Sex.value_counts().plot.pie(autopct='%1.1f%%')

sns.countplot(x='Sex', hue='Survived', data=data_train)

sns.countplot(x='Pclass',hue='Survived',data=data_train)

sns.histplot(data_train.Age)

"""# Create Model"""

X = data_train.drop('Survived',axis=1)
y = data_train.Survived

x_train , x_test , y_train , y_test = train_test_split(X,y,test_size=.2,random_state=42)

acuuraccies = []

def All(model_name):
  model_name.fit(x_train,y_train)
  prediction = model_name.predict(x_test)
  acuuracy = accuracy_score(prediction , y_test)
  print('Acuraccy  = ',acuuracy)
  acuuraccies.append(acuuracy)

model1 = LogisticRegression()
All(model1)

model2 = RandomForestClassifier()
All(model2)

model3 = GradientBoostingClassifier()
All(model3)

model4 = DecisionTreeClassifier()
All(model4)

model5 = KNeighborsClassifier()
All(model5)

model6 = GaussianNB()
All(model6)

model7 = SVC()
All(model7)

acuuraccies

algorithms = ['LogisticRegression', 'RandomForestClassifier', 'GradientBoostingClassifier', 'DecisionTreeClassifier',
          'KNeighborsClassifier', 'GaussianNB', 'SVC']

new= pd.DataFrame({'Algorithms':algorithms,'Acuuraccies':acuuraccies})

new

modelx = GradientBoostingClassifier()
modelx.fit(x_train,y_train)

Last_Prediction = modelx.predict(data_test)

final = data_test.PassengerId

Results = pd.DataFrame({'PassengerId':final,'Survived':Last_Prediction})

Results

Results.to_csv('Submission.csv',index=False)

