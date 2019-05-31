import pandas as pd
import random

from app import db
from app.models import Genre, Album

sample = pd.read_csv('sample.csv')
sample['album_id'] = sample['album_id'].str.strip('.jpg').astype('int')
sample.drop(columns='genre', inplace=True)
albums = pd.read_csv('albums.csv')

joined = pd.merge(sample, albums, on='album_id', how='left')
removed = joined[~joined['remove'].isna()]
joined = joined[joined['remove'].isna()]

# Check that the database contains all 8 expected genres
genres = Genre.query.all()
genre_names = [g.name for g in genres]
all_genres = ['country', 'electronic', 'folk', 'indie', 'metal', 'pop', 'rap', 'rock']
for g in all_genres:
    if g not in genre_names:
        db.session.add(Genre(name=g))

# Create mapping of genre name to id to assign albums a proper genre id
genres = Genre.query.all()
genre_map = {g.name: g.genre_id for g in genres}

for album in joined.itertuples():
    db.session.merge(Album(album_id=album.album_id,
                           genre_id=genre_map.get(album.genre),
                           prediction_id=list(genre_map.values())[random.randint(0, 7)],
                           confidence=random.random() * 0.4,
                           name=album.album[:60], artist=album.artist))

db.session.commit()
