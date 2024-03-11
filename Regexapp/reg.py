from flask import Flask, render_template, request
import re

regex = Flask(__name__)

@regex.route("/")
def index():
    return render_template("index.html")

@regex.route("/results", methods=["POST"])
def results():
    text = request.form.get("text")
    pattern = request.form.get("pattern")
    matches = re.findall(pattern, text)
    return render_template("results.html", text=text, pattern=pattern, matches=matches)

@regex.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form.get('email')
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(email_pattern, email):
        result = f"{email} is a valid email address"
    else:
        result = f"{email} is an invalid email address"

    return render_template('email_validation.html', result=result)

if __name__ == "__main__":
    regex.run(debug=True,host = '0.0.0.0',port = 5001)
