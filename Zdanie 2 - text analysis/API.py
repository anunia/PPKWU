import flask

app = flask.Flask(__name__)

@app.route('/analysis/<text>', methods=['GET'])
def analysis(text):
	uppercase = sum(map(str.isupper, text))
	lowercase = sum(map(str.islower, text))
	number = sum(map(str.isdigit, text))
    return 
     
app.run()