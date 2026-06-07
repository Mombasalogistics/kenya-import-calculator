from flask import Flask, render_template, request
from calculator import calculate_taxes, car_prices

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", cars=car_prices)

@app.route("/calculate", methods=["POST"])
def calculate():
    choice = request.form.get("car_choice")
    freight = float(request.form.get("freight", 163916))
    insurance = float(request.form.get("insurance", 13290))
    selected = car_prices[choice]
    result = calculate_taxes(
        selected["name"],
        selected["fob"],
        freight,
        insurance
    )
    return render_template("index.html", cars=car_prices, result=result)

if __name__ == "__main__":
    app.run(debug=True)
