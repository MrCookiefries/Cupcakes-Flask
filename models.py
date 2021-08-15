"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """connects flask app to database"""
    db.app = app
    db.init_app(app)

CUPCAKE_IMAGE = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    """FSQLA model for cupcakes table"""
    __tablename__ = "cupcakes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False, default=CUPCAKE_IMAGE)

    def __repr__(self):
        c = self
        return f"<Cupcake id={c.id} flavor={c.flavor} size={c.size} rating={c.rating}>"
    
    def serialize(self):
        """puts cupcake into a JSONifiable format"""
        c = self
        return {"id": c.id, "flavor": c.flavor, "size": c.size, "rating": c.rating, "image": c.image}
