from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    monthly_bill = None # सुरवातीला काहीच नाही

    if request.method == "POST":
        # 1. Form मधून Units घेणे
        units = int(request.form["units"])
        rate = 8
        monthly_bill = units * rate
        yearly_bill = monthly_bill * 12
        saving = yearly_bill * 0.90
        total_saving = saving * 25

        # 2. हे सगळं HTML कडे पाठवणे
        return render_template("index.html", 
                               units=units, 
                               monthly_bill=monthly_bill,
                               yearly_bill=yearly_bill,
                               saving=saving,
                               total_saving=total_saving)

    # 3. जर कोणी फक्त Page उघडला (GET), तर फक्त Form दाखव
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)