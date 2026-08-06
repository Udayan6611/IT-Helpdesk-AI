from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    # This tells Flask to look inside the templates folder and send index.html to the browser
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)