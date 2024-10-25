from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Rahul's World of learnings"


if __name__=="__main__":
    app.run()