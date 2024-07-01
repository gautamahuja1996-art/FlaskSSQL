from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# route 1: index route
@app.route("/", methods=["GET", "POST"])
def index():

    # if request is post
    if request.method == "POST":

        # let's extract the form data from the request
        email = request.form.get('emailAddress')
        password = request.form.get('userPassword')  

        # let's connect with db
        connection= sqlite3.connect('users.db')
        cursor= connection.cursor() 

        # let's store/add/create this in the database
        cursor.execute("INSERT INTO user (email, password) VALUES (?, ?)", (email, password))

        # let's commit this
        connection.commit()

        # let's close the connection
        connection.close()

        # response to the client: redirect to the / route
        return redirect("/")
    # if request is get
    else:
        return render_template('index.html')

# let's run the flask app
if __name__ == "__main__":
    app.run(debug= True)