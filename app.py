from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Simulating a database (replace this with an actual database connection)
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        message = request.form['message']
        # Saving the message to the database or list
        messages.append(message)
        # Optionally, perform other operations like saving to a file or database
        # For example: Save to a file
        with open('messages.txt', 'a') as file:
            file.write(message + '\n')
        return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
     return render_template('thank_you.html')

@app.route('/back_to_submit')
def back_to_submit():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
