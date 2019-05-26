from datetime import datetime
from app import db


class Album(db.Model):
    album_id = db.Column(db.Integer, primary_key=True)

    genre_id = db.Column(db.Integer, db.ForeignKey('genre.genre_id'))
    prediction_id = db.Column(db.Integer, db.ForeignKey('genre.genre_id'))

    name = db.Column(db.String(64), unique=False, nullable=False)
    artist = db.Column(db.String(64), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=True)
    confidence = db.Column(db.Float)

    guesses = db.relationship('Guess', backref='album', lazy='dynamic')

    genre = db.relationship('Genre', backref='albums'
                             , primaryjoin='Genre.genre_id == foreign(Album.genre_id)')

    prediction = db.relationship('Genre', backref='predictions'
                                  , primaryjoin='Genre.genre_id == foreign(Album.prediction_id)')

    def __repr__(self):
        return '<{} by {}>'.format(self.name, self.artist)


class Genre(db.Model):
    genre_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(32), unique=True, nullable=False)

    def __repr__(self):
        return '<Genre: {}>'.format(self.name)


class Guess(db.Model):
    guess_id = db.Column(db.Integer, primary_key=True)

    album_id = db.Column(db.Integer, db.ForeignKey('album.album_id'))  # album guessed on
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.genre_id'))  # user's genre guess

    correct = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Guess - album{}: {}>'.format(
            self.album_id, 'Correct' if self.correct else 'Incorrect')
