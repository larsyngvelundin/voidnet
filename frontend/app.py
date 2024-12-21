import argparse
import os

from flask import Flask, render_template
from dotenv import load_dotenv
from waitress import serve

load_dotenv(override=True)
FLASK_PORT = os.getenv("FLASK_PORT")
API_BASE = os.getenv("API_BASE")

app = Flask(__name__)


parser = argparse.ArgumentParser()
parser.add_argument("--debug", action="store_true", help="run in debug")
args = parser.parse_args()


@app.route("/listing/<int:id>")
def listing(id):
    data = {"id": id, "api_base": API_BASE}
    return render_template("listing.html", data=data)


@app.route("/")
def main_page():
    return render_template("main.html")


if __name__ == "__main__":
    if args.debug:
        app.run(debug=True, port=FLASK_PORT)
    else:
        serve(app, host="0.0.0.0", port=FLASK_PORT)
