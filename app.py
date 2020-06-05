import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
#What I did was comment out the code below and pasted a copy of it on line 12 so you could see the difference. Mainly being I put the words MONGO_URI in quotes and removed the
# mongodb://localhost at the end
#Please do not push to github until you add the uri to an environment variable
# app.config["MONGO_URI"] = 'mongodb+srv://AndersOlesen:EnormousPassword@cluster0-1tddr.azure.mongodb.net/task_manager?retryWrites=true&w=majority'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")



mongo = PyMongo(app)

@app.route("/")
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get("PORT")),
            debug = True)


