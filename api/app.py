import flask
import numpy as np
from cfg import models as model_list
from flask import  render_template, request
from utils import SARIMAPredictions, FBPredictions

models = model_list.models

app = flask.Flask(__name__)
app.config["debug"] = True

@app.route("/")
def welocme():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html", models=models)


@app.route("/predict", methods=["POST"])
def predict():
    if models[0]==request.form.get("model_name"):
        model = FBPredictions(request.form.get("model_name"))
        pred = model.predict(request.form.get("date"))
        return render_template("fbprophet.html", DatePicked=request.form.get("date"), 
                            Date=model.get_next_date(),
                            price= np.round(list(pred['yhat']),2))
    else:
        model = SARIMAPredictions(request.form.get("model_name"))
        pred = model.predict(request.form.get("date"))
        return render_template("Sarima.html", DatePicked=request.form.get("date"), 
                            Date=model.get_next_date(),
                            price= np.round(list(pred),2))
    



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)