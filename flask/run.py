import os
# import flask class
from flask import Flask, render_template


# store to app variable
app = Flask(__name__)

# app route decorator
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)