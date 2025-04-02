# app.py
from flask import Flask, render_template, request
from cipher import encode_message, decode_message, hide_in_sentence

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    hidden = None
    if request.method == 'POST':
        message = request.form['message']
        shift = request.form['shift']
        action = request.form['action']
        
        try:
            shift = int(shift)
            if not (1 <= shift <= 25):
                result = "Shift must be between 1 and 25!"
            elif action == "encode":
                encoded = encode_message(message, shift)
                result = f"Encoded: {encoded}"
                if 'hide' in request.form:
                    hidden = hide_in_sentence(encoded)
            elif action == "decode":
                decoded = decode_message(message, shift)
                result = f"Decoded: {decoded}"
        except ValueError:
            result = "Please enter a valid shift number!"

    return render_template('index.html', result=result, hidden=hidden)

if __name__ == '__main__':
    app.run(debug=True)