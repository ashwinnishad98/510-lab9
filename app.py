from flask import Flask, render_template, request

app = Flask(__name__)

db = [
    {"id": 1, "name": "photo1", "path": "images/1.jpg"},
    {"id": 2, "name": "photo2", "path": "images/2.jpg"},
    {"id": 3, "name": "photo3", "path": "images/3.jpg"},
]


@app.route("/")
def index():
    return render_template("index.html", photos=db, name="Ashwin")


@app.route("/photos", methods=["GET", "POST"])
def photos():
    if request.method == "POST":
        # save the photo
        # redirect to the photos page
        return "create photos"

    # show the list of photos
    return "list photos"


@app.route("/photos/new", methods=["GET"])
def new_photos():
    return "new photo"


@app.route("/photos/<int:id>", methods=["GET", "PUT", "DELETE"])
def show_photo(id):
    return "photo details for id: %s" % id


@app.route("/photos/<int:id>/edit", methods=["GET"])
def edit_photo(id):
    return "edit photo for id: %s" % id
