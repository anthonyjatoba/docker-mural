import os

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "messages.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

port = int(os.environ.get("PORT", 5000))

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)

    def __repr__(self):
        return "<Id: {}, Content: {}, Name: {}>".format(self.id, self.content, self.name)

@app.route('/', methods=["GET", "POST"])
def home():
    messages = None
    if request.form:
        try:
            message = Message(content=request.form.get("content"), name=request.form.get("name"))
            db.session.add(message)
            db.session.commit()
        except Exception as e:
            print("Failed to add message")
            print(e)
    messages = Message.query.all()
    return render_template("home.html", messages=messages)

@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    message = Message.query.filter_by(id=id).first()
    db.session.delete(message)
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)
