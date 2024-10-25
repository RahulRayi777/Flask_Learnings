from flask import Flask,render_template,request
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        # Retrieving form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Respond with a personalized message
        return f'Hello {name}, thank you for your message: "{message}". We will contact you at {email} soon!'
    
    # If GET request, render the form.html template
    return render_template('form.html')

 

if __name__=="__main__":
    app.run(debug=True)