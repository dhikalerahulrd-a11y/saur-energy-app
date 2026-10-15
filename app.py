from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

@app.route("/test-db")
def test_db():
    try:
        mongo.db.test_collection.insert_one({"status": "OK"})
        return "<h1>✅ Atlas Connected!</h1>"
    except Exception as e:
        return f"<h1>❌ Error: {e}</h1>"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    monthly_bill = None
    units = None

    if request.method == "POST":
        try:
            units = request.form.get("units")
            name = request.form.get("name")
            phone = request.form.get("phone")
            city = request.form.get("city")

            # तुझा साधा Bill Calculation
            monthly_bill = float(units) * 8  

            # Database मध्ये Save
            if name and phone:
                mongo.db.leads.insert_one({
                    "name": name,
                    "phone": phone,
                    "city": city,
                    "units": units,
                    "bill": monthly_bill
                })
                result = f"धन्यवाद {name}! Data Save झाला!"

        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result, monthly_bill=monthly_bill, units=units)

@app.route("/leads")
def show_leads():
    all_leads = list(mongo.db.leads.find())
    return render_template("leads.html", leads=all_leads)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)