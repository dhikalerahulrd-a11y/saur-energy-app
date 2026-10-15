import os
from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)


mongo_uri = os.environ.get("MONGO_URI") or os.getenv("MONGO_URI")

if not mongo_uri:
    print("ERROR: MONGO_URI not found in Environment!")
else:
    print(f"MONGO_URI loaded: {mongo_uri[:20]}...")

app.config["MONGO_URI"] = mongo_uri
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
   
    name = request.form.get('name')
    phone = request.form.get('phone')
    bill = request.form.get('bill')
    mongo.db.leads.insert_one({"name": name, "phone": phone, "bill": bill})
    return redirect('/')

@app.route('/leads')
def leads():
    all_leads = mongo.db.leads.find()
    return render_template('leads.html', leads=all_leads)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)