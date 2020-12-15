import flask
import ics
from bs4 import BeautifulSoup
from urllib.request import urlopen
from calendar import month
import datetime

app = flask.Flask(__name__)

@app.route('/calendar/<year>/<month>', methods=['GET'])
def calendar(year,month):
    result = get_info(year, month)
    return flask.Response(result, mimetype="text/calendar")


@app.route("/events")
def calendar_current_month():
    current_month = datetime.datetime.now()
    result = get_info(year, month)
    return flask.Response(result, mimetype="text/calendar")

          
def get_info(year, month):  
    url = "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok={}&miesiac={}&lang=1".format(year, month)
    event_selector = "#company-list card.company-item.py-2.container.my-2"
    title_selector = "#company-list "

        
    return c  
   
   
app.run()