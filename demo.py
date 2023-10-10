from flask import Flask
from diabetes.logger import logging

app = Flask(__name__)
@app.route ("/" , methods = ['GET' , 'POST'])

def index():
    logging.info("We are just testing the code logging moduls")
    return "Hello, This Project is Conduct by Mukul Singh"

if __name__ == "__main__":
    app.run(debug=True)