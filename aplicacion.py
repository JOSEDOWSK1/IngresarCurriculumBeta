from flask import Flask, render_template, request # Import the class `Flask` from the `flask` module, written by someone else.

app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file


@app.route("/") 
def index():
	return render_template(index.html)
@app.route("/hola", methods=["POST"])
def hola():
	name = request.form.get("name")
	return render_template("hola.html",name=name)

