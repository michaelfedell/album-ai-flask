from app import app, db
from app.models import Album, Genre, Guess


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Album': Album, 'Genre': Genre, 'Guess': Guess}
