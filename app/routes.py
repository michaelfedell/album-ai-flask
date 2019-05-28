from flask import render_template
from flask import request
from app import app, db
from app.models import Album, Genre, Guess
import random
import json

# genres = Genre.query.all()
# genres = sorted(genres, key=lambda x: x.name)


def get_random_album():
    query = Album.query
    row_count = int(query.count())
    random_row = query.offset(int(row_count * random.random())).first()
    return random_row


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/paper')
def paper():
    return render_template('paper.html')


@app.route('/game')
def game():
    genres = Genre.query.all()
    genres = sorted(genres, key=lambda x: x.name)

    return render_template('game.html', album=get_random_album(), genres=genres)


@app.route('/result')
def result():
    album_id = request.args.get('album')
    album = Album.query.get(album_id)
    print(album)
    if not album:
        print('ALBUM NOT FOUND')
        return
    guess_id = int(request.args.get('guess'))
    print(guess_id)
    correct = album.genre_id == guess_id
    print(correct)
    guess = Guess(album_id=album_id, genre_id=guess_id, correct=correct)
    print(guess)
    genre_name = Genre.query.get(album.genre_id)
    genre_guessed = Genre.query.get(guess_id)
    print(genre_guessed)
    performance = [{'scope': 'this album', 'humans': 0.348, 'model': 0.213},
                   {'scope': 'this genre', 'humans': 0.263, 'model': 0.401},
                   {'scope': 'all albums', 'humans': 0.315, 'model': 0.492}]
    # db.session.add(guess)
    # db.session.commit()
    return render_template('result.html', album=album, correct=correct,
                           genre_name=genre_name.name, genre_guessed=genre_guessed.name,
                           performance=json.dumps(performance, indent=2))
