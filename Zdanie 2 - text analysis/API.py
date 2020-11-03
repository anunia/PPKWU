import flask

app = flask.Flask(__name__)

@app.route('/analysis/<text>', methods=['GET'])

     
app.run()