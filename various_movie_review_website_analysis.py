# -*- coding: utf-8 -*-
"""Various movie review website analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TZ4sv_wYz1znHrB6RonhMHnS7iqLPWso
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

data=pd.read_excel(r"/content/fandango_score_comparison.xlsx")

data

data.isnull().sum()

data.dtypes

for i in data.columns:
    print(i,':','\n',data[i].unique())

sns.scatterplot(x=data.RottenTomatoes,y=data.RottenTomatoes_User)

sns.scatterplot(x=data.Metacritic,y=data.Metacritic_User)

#relationship between vote counts on MetaCritic versus vote counts on IMDB
sns.scatterplot(x=data.Metacritic_user_vote_count,y=data.IMDB_user_vote_count)

sns.scatterplot(x=data.RT_norm,y=data.RT_user_norm)

df=data[['IMDB_user_vote_count','Metacritic_user_vote_count','Fandango_votes']]

sns.kdeplot(data=df)

#norm_scores DataFrame that only contains the normalizes ratings include both STARS and RATING from the original Fandango table

norm_score=data[['Fandango_Stars','Fandango_Ratingvalue','RT_norm_round','RT_user_norm_round','Metacritic_norm',
                 'IMDB_norm','Metacritic_user_norm_round','IMDB_norm_round']]

norm_score

sns.kdeplot(data=norm_score,fill=True)

data

sns.histplot(data['Fandango_Stars'])
plt.title('Fandango Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10,5))
sns.boxplot(data=data[['Fandango_Stars','RT_user_norm','Metacritic_user_nom','IMDB_norm']])

data1=data.drop(['FILM'],axis=1)

d=data1.corr()
plt.figure(figsize=(20,10))
sns.heatmap(d,annot=True)

# We'll predict Fandango rating using other ratings
ip=data1.drop(['Fandango_Stars'],axis=1)
op=data1['Fandango_Stars']

#train test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(ip,op,test_size=0.45,random_state=42)

#standard scalar transform
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)

from sklearn.linear_model import LinearRegression
alg=LinearRegression()
alg.fit(x_train,y_train)

yp=alg.predict(x_test)

df=pd.DataFrame({'y':list(y_test),'prediction':yp})

#accuracy
from sklearn.metrics import mean_squared_error,r2_score
mse=mean_squared_error(y_test,yp)
r2=r2_score(y_test,yp)

print(mse)
print(r2)







