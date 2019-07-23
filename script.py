from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
# Import of classes from libraries

script = Flask(__name__)
# Create the flask object

#script.config["SQLALCHEMY_DATABASE_URI"]="please introduce your SQLALCHEMY_DATABASE_URI"
db = SQLAlchemy(script)
# Set up the database using SQLAlchemy


class Data(db.Model):
# Create Data class through db.Model
    __tablename__="data"
    # Assign "data" name to the data table
    id = db.Column(db.Integer, primary_key=True)
    # Create id column in the data table with integer data type and
    # set it as the index
    email_ = db.Column(db.String(120), unique =True)
    # Create email column in the data table.
    # Max length of string 120 and it can´t be repeated
    weight_ = db.Column(db.Integer)
    # Create weight column in the data table

    def __init__(self, email_, weight_):
    # __init__ function to initialise the variables
        self.email_ = email_
        self.weight_ = weight_


@script.route("/")
# route decorator used to deploy index page
def index():
# Create function to render index page
    return render_template("index.html")

@script.route("/success", methods=["POST"])
# route decorator that deploys "sucess" page and applies "POST" method
# method to the server
def success():
# Generate sucess function
    if request.method == "POST":
    # if block triggered in case method used is "POST"
        email = request.form["email_name"]
        # store the value from "email_name" into email variable
        weight = request.form["weight_name"]
        # store the value from "weight_name" into weight variable
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
        # if block triggered just if there is no email in the database repeated
            data = Data(email, weight)
            db.session.add(data)
            # Add the data to the database
            db.session.commit()
            # Commit the changes done in the database
            average_weight = db.session.query(func.avg(Data.weight_)).scalar()
            # Obtain numerical average weight from weight_ column
            average_weight = round(average_weight, 1)
            # Set the average weight to just one decimal
            count = db.session.query(Data.weight_).count()
            # Count the number of weights in the database to inform the user
            send_email(email, weight, average_weight, count)
            # Call send_email function inside send_email script
            return render_template("success.html")
            # render sucess page
        return render_template("index.html",
        text="We have the data from that email address already!")
        # when email address is repeated in the database return index page
        # and text


if __name__ == '__main__':
    script.debug = True
    script.run()

# If the script is called interactively then the code will be executed
