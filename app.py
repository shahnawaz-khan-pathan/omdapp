from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://omdappdbuser:omdappdbpassword@localhost/omdappdb'
CORS(app, support_credentials=True)

db = SQLAlchemy(app)

if __name__ == "__main__":

    from views import *
    app.run(debug=True, port=5000)
