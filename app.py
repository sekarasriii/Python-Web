from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')
    if not name or not age:
        return "Please fill in both fields!"
    return f"Hello, {name}! You are {age} years old."

if __name__ == '__main__':
    app.run(debug=True)
