import flask
import ics

app = flask.Flask(__name__)

@app.route('/calendar/<year>/<month>', methods=['GET'])
def calendar(year,month):
    return 0
                 
app.run()