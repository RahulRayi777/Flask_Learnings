from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Base Route
@app.route('/')
def home():
    return '''
    <h1>Welcome to the Student Evaluation Portal</h1>
    <p>Please <a href="/form">click here</a> to enter your subject scores and calculate your result.</p>
    '''

# Form Route
@app.route('/form')
def form():
    return '''
    <h1>Enter Your Subject Scores</h1>
    <form action="/calculate_result" method="POST">
        <label for="math">Math:</label><br>
        <input type="number" id="math" name="math" required><br><br>

        <label for="science">Science:</label><br>
        <input type="number" id="science" name="science" required><br><br>

        <label for="english">English:</label><br>
        <input type="number" id="english" name="english" required><br><br>

        <label for="history">History:</label><br>
        <input type="number" id="history" name="history" required><br><br>

        <label for="geography">Geography:</label><br>
        <input type="number" id="geography" name="geography" required><br><br>

        <input type="submit" value="Submit">
    </form>
    '''

# Calculate Result Route
@app.route('/calculate_result', methods=['POST'])
def calculate_result():
    # Retrieve scores from the form
    math = int(request.form['math'])
    science = int(request.form['science'])
    english = int(request.form['english'])
    history = int(request.form['history'])
    geography = int(request.form['geography'])
    
    # Calculate the average score
    average_score = (math + science + english + history + geography) / 5

    # Determine pass or fail based on the average
    if average_score < 35:
        result = "Failed"
    else:
        result = "Passed"
    
    return f'Your average score is {average_score}. You have {result}. <br><br><a href="/">Go back to Home</a>'

if __name__ == '__main__':
    app.run(debug=True)
