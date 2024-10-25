from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to store scores
scores = {}

# Route to handle PUT request (updating a score)
@app.route('/update_score', methods=['PUT'])
def update_score():
    data = request.get_json()
    name = data.get("name")
    subject = data.get("subject")
    score = data.get("score")

    # Update the score in the dictionary
    scores[subject] = {"name": name, "score": score}
    
    return f"Score for {subject} updated successfully!"

# Route to handle DELETE request (deleting a score)
@app.route('/delete_score/<subject>', methods=['DELETE'])
def delete_score(subject):
    if subject in scores:
        del scores[subject]
        return f"Score for {subject} deleted successfully!"
    else:
        return f"Score for {subject} not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
