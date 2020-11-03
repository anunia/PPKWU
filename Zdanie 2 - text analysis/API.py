import flask

app = flask.Flask(__name__)

@app.route('/analysis/<text>', methods=['GET'])
def analysis(text):
	uppercase = sum(map(str.isupper, text))
	lowercase = sum(map(str.islower, text))
	number = sum(map(str.isdigit, text))
	special = sum(not ch.isalnum() for ch in text)
	result2 = {
		"Number of uppercase characters: " : uppercase,
		"Number of lowercase characters: " : lowercase,
		"Number of number characters: " : number,
		"Number of special characters: " : special}

	return result2

app.run()