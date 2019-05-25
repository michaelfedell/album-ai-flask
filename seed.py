import csv


def parse_album(row):
    name = row[0]
    artist = row[1]
    genre_id = row[2]
    album_id = row[4]
    prediction = row[5]
    confidence = row[6]
    return Album(album_id=int(album_id), genre_id=(genre_id), name=name, prediction=int(prediction), artist=artist,
                 confidence=confidence)


albums = []
genres = []

with open('mock.csv') as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
        a = parse_album(row)
        g = Genre(genre_id=row[2], name=row[3])
        albums.append(a)
        genres.append(g)

for g in genres:
    exists = db.session.query(Genre).get(g.genre_id)
    if not exists:
        db.session.add(g)

for a in albums:
    exists = db.session.query(Album).get(a.album_id)
    if not exists:
        db.session.add(a)

db.session.commit()
