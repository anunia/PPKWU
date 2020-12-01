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
    event_selector = "#kalendarz td.active"
    title_selector = "#kalendarz .InnerBox"
    day_and_url_selector = "#kalendarz a"
    
    info = urlopen(url)
    html = BeautifulSoup(info.read())
    selected_elements = html.select(event_selector)
    
    c = ics.Calendar()

    for event in selected_elements:
        e = ics.Event()
        e.name = event.select(title_selector)[0].getText()
        day_and_url = event.select(day_and_url_selector)[0]
        e.begin = "{}-{}-{}".format(year, month, day_and_url.getText())
        e.url = day_and_url["href"]
        c.events.add(e)
        
    return c  
   
   
app.run()