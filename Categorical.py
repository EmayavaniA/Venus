import pandas as pd
import numpy as np
df= pd.read_csv('category_data.csv')
df1= pd.read_csv('category_data.csv')
df.head()

from sklearn.preprocessing import LabelEncoder
gle = LabelEncoder()
genre_labels = gle.fit_transform(df['RATING'])
df['ENCODED RATING']=genre_labels
df.head()
gle = LabelEncoder()
genre_labels = gle.fit_transform(df['EDUCATION '])
df['ENCODED EDUCATION']=genre_labels
df.head()
from sklearn.preprocessing import OneHotEncoder
gle = OneHotEncoder()
genre_labels = gle.fit_transform(df['EYE COLOR'])
df['ENCODED EYE COLOR']=genre_labels
df.head(10)
df[['EYE COLOR','ENCODED EYE COLOR']]
gen_ohe = OneHotEncoder()
gen_feature_arr = gen_ohe.fit_transform(
                              df[['EYE COLOR']]).toarray()
gen_feature_labels = list(gle.classes_)
gen_features = pd.DataFrame(gen_feature_arr, 
                            columns=gen_feature_labels)
df1= df1.drop(['RATING','EDUCATION '], axis=1)

pd.concat([df1, gen_features,df['RATING']], axis=1).iloc[1:7]
df1.head()
df2=pd.concat([df1, gen_features], axis=1).iloc[1:7]
df
data= pd.concat([df['ENCODED RATING'], df['ENCODED EDUCATION'], gen_features], axis = 1)
data
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3).fit(data)
centroids = kmeans.cluster_centers_               #represents the cluster centroids
print(centroids)
kmeans.labels_
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter( data[:,0], data[:,1], data[:,2],  c=kmeans.labels_, cmap='rainbow')
ax.scatter(centroids[:,0], centroids[:,1], centroids[:,2], c='black',marker='^', s=100)

ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
plt.show()
