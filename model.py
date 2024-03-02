from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='web/html', static_folder='web')
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/aboutus/")
def aboutus():
    return render_template("about.html")

@app.route("/search/")
def search():
    return render_template("creasingmatrices.html")

if __name__ == "__main__":
    app.run(debug=True)