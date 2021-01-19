from  flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #http://127.0.0.1:5000/
def index_1():
    return render_template("index.html")

@app.route("/page2/")  #render_template("index.html")
def index_2():
    return render_template("pagina2.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1")
