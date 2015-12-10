from flask import Flask, render_template

app = Flask(__name__)

@app.route("/platform")
def platform():
    #page="<h1>Platform</h1>"
    #return page
    return render_template("platform.html")

@app.route("/people")
def people():
    #page="<h1>People</h1>"
    #return page
    return render_template("people.html")

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
