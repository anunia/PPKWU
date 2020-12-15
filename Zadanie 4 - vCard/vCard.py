import flask


app = flask.Flask(__name__)

@app.route('/contact/<category>/<location>', methods=['GET'])
def contact(category,location):
    result = get_info(category, location)
    return 0

app.run()