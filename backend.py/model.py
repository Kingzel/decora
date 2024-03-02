from flask import Flask, redirect, url_for, render_template
app = Flask(__name__, template_folder="/Users/tavishisaxena/Desktop/decora-1/html" ,static_folder="/Users/tavishisaxena/Desktop/decora-1/css")
@app.route("/")
def home():
    return render_template('index.html')

# @app.route("/")
# def aboutus():
#     return render_template("html/about.html")

# @app.route("/")
# def search():
#     return render_template("html/creasingmatrices.html")

if __name__ == "__main__":
    app.run()