import flask
import ics
import bs4
from urllib.request import urlopen
from calendar import month

app = flask.Flask(__name__)

@app.route('/calendar/<year>/<month>', methods=['GET'])
def calendar(year,month):
    ret = get_info(year, month)
    return ret
          
def get_info(year, month):  
    url = "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=" + str(year) + "&miesiac=" + str(month) + "&lang=1"
    info = request.urlopen(url)
    print(info.prettify())
    return info     
app.run()