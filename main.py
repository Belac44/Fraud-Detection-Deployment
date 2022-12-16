from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
from model_build import ModelBuild
import os

class DataForm(FlaskForm):
    step = IntegerField("Step", validators=[DataRequired()])
    type = SelectField("Type", choices=[(0, "PAYMENT"), (1, "TRANSFER"), (2, "CASH_OUT")], coerce=int)
    amount = IntegerField("Amount", validators=[DataRequired()])
    nameOrig = IntegerField("Credit card Making Payment", validators=[DataRequired()])
    oldB = IntegerField("Old Balance Payer ", validators=[DataRequired()])
    newB = IntegerField("New Balance Payer", validators=[DataRequired()])
    nameDest = IntegerField("CreditNo receiving Payment", validators=[DataRequired()])
    oldBD = IntegerField("Old Balance Destination", validators=[DataRequired()])
    newBD = IntegerField("New Balance Destination", validators=[DataRequired()])

    submit = SubmitField()

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def home():
    form = DataForm()
    model = ModelBuild()
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

        data = (step, type, amount, nameOrig, oldB, newB, nameDest, oldBD, newBD)

        model.make_prediction(data)
        print("Model Prediction is: ", pred[0])
        return redirect(url_for('home', message="successful data"))

    return render_template("home.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
