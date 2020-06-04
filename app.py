import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid iport ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task-manager'
app.config[MONGO_URI] = 'mongodb+srv://AndersOlesen:Enormouspassword@cluster0-1tddr.azure.mongodb.net/tast_manager?retryWrites=true&w=majority'

@app.route("/")
def hello():
    return "Hello World .... again there.. mate....."

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get("PORT")),
            debug = True)
