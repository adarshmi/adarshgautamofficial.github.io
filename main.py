from flask import Flask, render_template,request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/inner-page")
def innerpage():
    return render_template('inner-page.html')


@app.route("/portfolio-details")
def portfoliodetails():
    return render_template('portfolio-details.html')


app.run(debug=True)

