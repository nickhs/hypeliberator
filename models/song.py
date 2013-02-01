from app import db
from datetime import datetime


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    modified_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow(), index=True)
    deleted = db.Column(db.Boolean)

    title = db.Column(db.String(100), index=True)
    artist = db.Column(db.String(100))
    url = db.Column(db.String(200))
    hypem_id = db.Column(db.String(10), index=True)
    artist_thumb = db.Column(db.String(200))
    time = db.Column(db.Integer)

    downloaded = db.Column(db.Integer, default=1)

    def __init__(self, hypem_id):
        self.hypem_id = hypem_id

    @classmethod
    def get_by_hypem(cls, id):
        return Song.query.filter_by(hypem_id=id).first()

    def to_dict(self):
        return {
            'title': self.title,
            'artist': self.artist,
            'url': self.url,
            'hypem_id': self.hypem_id
        }
