from flask import Flask, render_template, request, redirect, url_for
import pymongo
import yaml

app = Flask(__name__)

MAJORS = yaml.load(file('majors.yaml', 'r'))

if __name__ == '__main__':
    app.run(debug=True)
