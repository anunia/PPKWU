import flask

app = flask.Flask(__name__)

@app.route('/analysis/<text>', methods=['GET'])
def analysis(text):
	uppercase = sum(map(str.isupper, text))

    return 
     
app.run()