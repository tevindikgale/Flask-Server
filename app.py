from flask import Flask, request, jsonify

app = Flask(__name__)

def sanitize_input(input_str):
    return str(input_str)

@app.route('/', methods=['GET','POST'])
def process_request():
    try:
        # Get the POST parameters
        prompt = request.form.get('prompt')
        user = request.form.get('user')

        # Sanitize inputs
        prompt = sanitize_input(prompt)
        user = sanitize_input(user)

        return jsonify({'status': '200', 'message': 'Request processed successfully'})

    except Exception as e:
        return jsonify({'status': '500', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
