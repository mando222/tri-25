#!/usr/bin/env python3

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "To use the api add /api to your url"


@app.route("/api/<command>")
def api(command):
    return command
    # crud=command.split('=',str)
    # if crud == 'update':
    #     return (f"{command}")
    # elif crud == 'delete':
    #     return (f"{command}")
    # elif crud == 'insert':
    #     return (f"{command}")
    # elif crud == 'select':
    #     return (f"{command}")

@app.route("/api/")
def api_page():
    return "this is the api
    
    "


if __name__ == "__main__":
    app.run()