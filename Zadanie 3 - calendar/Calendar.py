import flask
import ics
import bs4
from calendar import month

app = flask.Flask(__name__)

@app.route('/calendar/<year>/<month>', methods=['GET'])
def calendar(year,month):
    get_info(year, month)
    return 0
          
def get_info(year, month):  
    
    return 0     
app.run()