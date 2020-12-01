import flask
import ics
from bs4 import BeautifulSoup
from urllib.request import urlopen
from calendar import month
import datetime

app = flask.Flask(__name__)

@app.route('/calendar/<year>/<month>', methods=['GET'])
def calendar(year,month):
    ret = get_info(year, month)
    return flask.jsonify(ret)

@app.route("/events")
def calendar_current_month():
    current_month = datetime.datetime.now()
    return jsonify(get_info(current_month.year, current_month.month))
          
def get_info(year, month):  
    url = "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok={}&miesiac={}&lang=1".format(year, month)
    event_selector = "#kalendarz td.active"
    title_selector = "#kalendarz .InnerBox"
    day_and_url_selector = "#kalendarz a"
    
    info = urlopen(url)
    html = BeautifulSoup(info.read())
    
    return html  
   
app.run()