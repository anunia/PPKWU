import flask

app = flask.Flask(__name__)

@app.route('/rev/<query>', methods=['GET'])


app.run()