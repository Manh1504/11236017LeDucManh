from flask import Flask, render_template
from main.customer_api import customer_api

app = Flask(__name__)
app.register_blueprint(customer_api)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
