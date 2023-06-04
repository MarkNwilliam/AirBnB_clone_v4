#!/usr/bin/python3
"""
Flask App that integrates the AirBnB static HTML Template
"""
from flask import Flask, render_template
import uuid

app = Flask(__name__)

@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    return render_template('0-hbnb.html', cache_id=uuid.uuid4())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
