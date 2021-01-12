import flask
import vobject
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello"
@app.route('/contact/<category>/<location>', methods=['GET'])
def contact(category,location):
    result = get_info(category, location)
    return 0

def get_info(category, location):  
    url = "https://panoramafirm.pl/szukaj?k={}y&l={}".format(category, location)
    company_selector = "#company-list li.company-item"
    name_selector = "a.company-name"
    address_selector = "div.address"
    number_selector = "a.icon-telephone"

    email_selector = "a.icon-envelope"

    info = urlopen(url)
    html = BeautifulSoup(info.read(), "html.parser")
    selected_elements = html.select(company_selector)
    
    tab = []

    for card in selected_elements:
        print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        tab.append({
            "name" : card.select(name_selector)[0].getText(),
            "address": card.select(address_selector)[0],
            "phone": card.select(number_selector)[0],
            "mail":  card.select(email_selector)[0]
        })
        
    return str("selected_elements")    

   
app.run()