import functions

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        artist = request.form["artist"]
        time_available = float(request.form["time_available"])
        minutes_per_artwork = int(request.form["minutes_per_artwork"])

        results = functions.search_artworks(artist, time_available, minutes_per_artwork)

        return render_template("results.html", artist=artist, time_available=time_available, results=results)
    else:
        return "Wrong HTTP method", 400

if __name__ == "__main__":
    app.run(debug=True)