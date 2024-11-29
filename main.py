from flask import Flask, request, jsonify

app = Flask(__name__)

products = []

@app.route("/")
def Checking():
    return"successfull"

if __name__== '_main_':
    app.run(debug=True)