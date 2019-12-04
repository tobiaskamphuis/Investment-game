from flask import Flask, render_template
# Here we are importing the Flask module and creating a Flask web server from the Flask module.

app = Flask(__name__)
# _name means this current file. In this case, it will be web_gui.py. This file represents my web application
# We are creating an instance of the Flask class and calling it app. Here we are creating a new web application.

@app.route('/')
# default page, below function will be activated if default page is reached
def home():
    return render_template("home.html")

@app.route('/about')
# default page, below function will be activated if default page is reached
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
