from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for('html/index.html'))

@app.route("/aboutus/")
def aboutus():
    return redirect(url_for("html/about.html"))

@app.route("/search/")
def search():
    return redirect(url_for("html/creasingmatrices.html"))

if __name__ == "__main__":
    app.run(debug=True)