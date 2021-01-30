from flask import Flask, render_template

app = Flask(__name__, template_folder="./src/views")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return "Sobre"

app.run(port=8080, debug=True)