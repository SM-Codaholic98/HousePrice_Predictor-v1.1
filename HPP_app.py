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
        area_type = request.form['Area Type']
        if area_type == 'Super Built-Up Area':
            area_type = 1
        elif area_type == 'Plot Area':
            area_type = 2
        elif area_type == 'Built-Up Area':
            area_type = 3
        else:
            area_type = 4
            
        availability = request.form['Availability']
        if availability == 'Not Ready to Move':
            availability = 0
        else:
            availability = 1
            
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