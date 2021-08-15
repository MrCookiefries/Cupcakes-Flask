"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake
from utils import get_cupcake_data

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "AGkajgea9i3kjaj45KDjskg"

connect_db(app)

@app.route("/")
def home_page():
    """shows the landing page"""
    return render_template("home.html")

@app.route("/api/cupcakes", methods=["GET", "POST"])
def cupcakes_api():
    """gets cupcakes data or creates a new cupcake"""
    if request.method == "GET":
        cupcakes = [c.serialize() for c in Cupcake.query.all()]
        return jsonify(cupcakes=cupcakes)
    c = get_cupcake_data(request.json)
    cupcake = Cupcake(**c)
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.serialize()), 201)

@app.route("/api/cupcakes/<int:id>", methods=["GET", "PATCH", "DELETE"])
def cupcake_api(id):
    """gets details about one cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    if request.method == "PATCH":
        c = get_cupcake_data(request.json)
        cupcake.rating = c["rating"]
        cupcake.size = c["size"]
        cupcake.flavor = c["flavor"]
        cupcake.image = c["image"] or cupcake.image
        db.session.commit()
    if request.method != "DELETE":
        return jsonify(cupcake=cupcake.serialize())
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")
