from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("D:\\EDA\\HousePrice_Predictor v1.1\\HousePrice.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("WebApp.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        area_type = int(request.form['Area Type'])
        availability = int(request.form['Availability'])
        bedrooms = float(request.form['Bedrooms'])
        bathrooms = float(request.form['Bathrooms'])
        balcony = float(request.form['Balcony'])
        total_sqft = float(request.form['Total Sqft'])
        
        prediction = model.predict([[area_type, availability, bedrooms, bathrooms, balcony, total_sqft]])
        output=round(prediction[0],2)

        return render_template('WebApp.html',prediction_text="Your House price is Rs. {} Lakhs".format(output))

    return render_template("WebApp.html")


if __name__ == "__main__":
    app.run(debug=True)