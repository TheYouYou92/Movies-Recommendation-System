# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 11:54:57 2023

@author: youyo
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
rot = pd.read_csv('reco/rotten_tomatoes_movies.csv')
rev = pd.read_csv('reco/IMDB Dataset.csv')
df = pd.read_csv('reco/movie_dataset.csv')
df.columns

rot.columns
features = ['movie_info','content_rating', 'genres', 'directors', 'authors',
                'actors','production_company',]
def com_features(row):
    return row['movie_info']+' '+row['content_rating']+ ' '+row['genres']+' '+row['directors']+' '+row['authors']+' '+row['actors']+ ' '+row['production_company']
for feature in features:
    rot[feature] = rot[feature].fillna(' ')

rot['combined'] = rot.apply(com_features,axis=1)



cv = CountVectorizer()
count_matrix = cv.fit_transform(rot['combined'])

cosine_sim = cosine_similarity(count_matrix)

def get_title_from_index(index):
    return rot[rot.index == index]["movie_title"].values[0]
def get_index_from_title(title):
    return rot[rot.movie_title == title].index.values[0]


movie_user_likes = "Bai ri yan huo (Black Coal, Thin Ice)"

movie_index = get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cosine_sim[movie_index])) 
rot.index

sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]



i=0
print("Top 5 similar movies to "+movie_user_likes+" are:\n")
for element in sorted_similar_movies:
    print(get_title_from_index(element[0]))
    i=i+1
    if i>5:
        break
















