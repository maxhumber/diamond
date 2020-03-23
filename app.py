import pickle
from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__, template_folder="templates")

@app.before_first_request
def load_model():
    global pipe
    with open("model/pipe.pkl", "rb") as f:
        pipe = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def predict():
    form = request.form
    new = pd.DataFrame({
        'carat': [form['carat']],
        'cut': [form['cut']],
        'color': [form['color']],
        'clarity': [form['clarity']],
    })
    price = max(int(round(pipe.predict(new)[0], -1)), 0)
    price = "${:,.2f}".format(price)
    return render_template("result.html", price=price)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
