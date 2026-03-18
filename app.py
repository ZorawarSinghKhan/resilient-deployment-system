from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "App is running!"

@app.route('/crash')
def crash():
    os._exit(1)

@app.route('/health')
def health():
    return "OK"

app.run(host='0.0.0.0', port=5000)
