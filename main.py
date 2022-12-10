from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import os

class DataForm(FlaskForm):
    step =  IntegerField("Step", validators=[DataRequired()])
    type = SelectField("Type", choices=[("PAYMENT"), ("TRANSFER"), ("CASH_OUT")])
    amount = IntegerField("Amount", validators=[DataRequired()])
    nameOrig = StringField("nameOrig", validators=[DataRequired()])
    oldB = StringField("Old Balance ", validators=[DataRequired()])
    newB = StringField("New Balane", validators=[DataRequired()])
    nameDest = StringField("Name od Destination", validators=[DataRequired()])
    oldBD = StringField("Old Balance Dest", validators=[DataRequired()])
    newBD = StringField("New Balance Dest", validators=[DataRequired()])
    submit = SubmitField()

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def home():
    form = DataForm()
    if form.validate_on_submit():
        step = form.step.data
        type = form.type.data
        amount = form.amount.data
        nameOrig = form.nameOrig.data
        oldB = form.oldB.data
        newB = form.newB.data
        nameDest = form.nameDest.data
        oldBD = form.oldBD.data
        newBD = form.newBD.data

        print(step,type,amount, nameOrig, oldB, oldBD, newBD,nameDest, newB)

        return redirect(url_for('home', message="sucessful data"))

    return render_template("home.html", form=form)


if __name__== "__main__":
    app.run(host="0.0.0.0", debug=True)