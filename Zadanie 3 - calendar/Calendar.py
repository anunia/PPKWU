import flask

app = flask.Flask(__name__)

@app.route('/calendar/<year>/<month>', methods=['GET'])

app.run()