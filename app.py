from flask import Flask, render_template, request, redirect
import os
from flask_pymongo import PyMongo
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)

# FIX 1: हा Route GET असायला हवा!
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# FIX 2: हा Route POST असायला हवा, आणि नंतर परत / वर पाठवायला हवा!
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    bill = request.form.get('bill')
    if name:
        mongo.db.leads.insert_one({"name": name, "phone": phone, "bill": bill})
    return redirect('/') # POST नंतर GET वर!

@app.route('/leads', methods=['GET'])
def show_leads():
    leads = list(mongo.db.leads.find())
    return render_template('leads.html', leads=leads)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)