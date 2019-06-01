import pandas as pd
import random
import sys

from app import db
from app.models import Genre, Album

path = sys.argv[1] if len(sys.argv) > 1 else 'sample.csv'

sample = pd.read_csv(path)
if '.jpg' in sample.iloc[0].album_id:
    sample['album_id'] = sample['album_id'].str.strip('.jpg').astype('int')
else:
    sample['album_id'] = sample['album_id'].astype('int')
sample = sample[sample['remove'].isna()]
# Create mapping of genre name to id to assign albums a proper genre id
genres = Genre.query.all()
genre_map = {g.name: g.genre_id for g in genres}

for album in sample.itertuples():
    db.session.merge(Album(album_id=album.album_id,
                           prediction_id=genre_map.get(album.predicted_genre),
                           confidence=album.correct_certainty))

p = {'country': 0.2727,
     'electronic': 0.3750,
     'folk': 0.1667,
     'indie': 0.1020,
     'metal': 0.4375,
     'pop': 0.1702,
     'rap': 0.930,
     'rock': 0.1667}

for g in p.keys():
    genre = Genre.query.get(genre_map.get(g))
    genre.model_performance = p.get(g)
    db.session.merge(genre)

db.session.commit()
