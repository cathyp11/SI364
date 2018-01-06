# Import statements necessary
from flask import Flask, render_template
import requests
import json

# Set up application
app = Flask(__name__)

# Routes

@app.route('/')
def another_function():
    return 'Hello World!'

@app.route('/user/<yourname>')
def hello_name(yourname):
    return '<h1>Hello {}</h1>'.format(yourname)

# new route: /itunes/<artist>
@app.route('/itunes/<aritst>')
def get_artist_data(artist):
	# use artist to make req to itunes
	# get the res
	# get the data out of the res
	# manage the data so I pull a list of strings out of the nested data
	# return it (with any specific html I want, I guess)

	return list_of_strs


if __name__ == '__main__':
    app.run()
