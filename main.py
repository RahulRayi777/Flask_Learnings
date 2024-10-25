from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1> Welcome to the Flask Course<H1><html>"
@app.route("/index")
def index():
    return render_template('index1.html')
@app.route("/about")
def about():
    return render_template('index2.html')


if __name__=="__main__":
    app.run()