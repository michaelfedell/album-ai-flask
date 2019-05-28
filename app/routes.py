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
    if not album:
        print('ALBUM NOT FOUND')
        return

    # Build Guess object and save to database
    guess_id = int(request.args.get('guess'))
    correct = album.genre_id == guess_id
    guess = Guess(album_id=album_id, genre_id=guess_id, correct=correct)
    db.session.add(guess)
    db.session.commit()

    # Get genre information for this page
    genre = Genre.query.get(album.genre_id)
    genre_name = genre.name
    genre_guessed = Genre.query.get(guess_id)

    # Calculate performance for each scope. Note: we round(3) to limit numbers to percents to tenth
    album_guesses = [int(gus.correct) for gus in album.guesses.all()]
    album_performance = round(sum(album_guesses) / len(album_guesses), 3)

    genre_guesses = [int(gus.correct) for a in genre.albums
                     for gus in a.guesses.all()]
    genre_performance = round(sum(genre_guesses) / len(genre_guesses), 3)

    total_performance = db.session.query(
        db.func.avg(Guess.correct.cast(db.Integer)).
            label('avg_correct'))\
        .scalar()
    total_performance = round(float(total_performance), 3)

    performance = [{'scope': 'this album', 'humans': album_performance, 'model': round(float(album.confidence), 3)},
                   {'scope': 'this genre', 'humans': genre_performance, 'model': 0.401},  # replace 0.401 with genre.model_performance
                   {'scope': 'all albums', 'humans': total_performance, 'model': 0.215}]  # 0.215 will be static based on model's final acc

    return render_template('result.html', album=album, correct=correct,
                           genre_name=genre_name, genre_guessed=genre_guessed.name,
                           performance=json.dumps(performance, indent=2))
