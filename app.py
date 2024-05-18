"""
Author: Kanak Sachan
Date: 2024-05-18
Copyright (c) 2024 Kanak Sachan
Description: A basic Flask application using blueprint structure.
"""
from flask import Flask
from application import application as application_blueprint

app = Flask(__name__)
app.register_blueprint(application_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


