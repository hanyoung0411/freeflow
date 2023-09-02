from dotenv import load_dotenv
from flask import Flask, request, jsonify
import os

from processor.api import process_blob, process_string


app = Flask(__name__)

@app.route('/process/conv', methods=['POST'])
def process_conversation():
    # TODO: this endpoint will communicate with whisper AI api
    blob_file = request.files['blob']
    response_data = process_blob(blob_file)
    return jsonify(response_data)

@app.route('/process/prompt', methods=['POST'])
def process_prompt():
    # TODO: this endpoint will communicate with GPT api
    prompt = request.form.get('prompt', '')
    response_data = process_string(prompt)
    return jsonify(response_data)

if __name__ == '__main__':

    load_dotenv()
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(debug=True)