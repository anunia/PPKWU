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
    return result

def button(company):
    return """
        <form method="post" action="/vcard">
            <input type="submit" value="Wizytówka" />
            <input type="hidden" name="name" value=\"""" + company["name"] + """\" />
            <input type="hidden" name="mail" value=\"""" + company["mail"] + """\" />
            <input type="hidden" name="phone" value=\"""" + company["phone"] + """\" />
            <input type="hidden" name="address" value=\"""" + company["address"] + """\" />
        </form>
    """
@app.route("/vcard", methods = ["POST"])
def vcard():
    vc = vCard()
    
    vc.add("fn")
    vc.fn.value = request.form.get("name")
    vc.add("tel")
    vc.tel.value = request.form.get("phone")
    vc.add("email")
    vc.email.value = request.form.get("mail")

    return vc.serialize()

def get_info(category, location):  
    url = "https://panoramafirm.pl/szukaj?k={}&l={}".format(category, location)
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
        tab.append({
            "name" : card.select(name_selector)[0].getText(),
            "address": card.select(address_selector)[0],
            "phone": card.select(number_selector)[0],
            "mail":  card.select(email_selector)[0]
        })
        
    return str(tab)
def page(content):
    page = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Mobilny vCard</title>
        </head>
        <body>
            """ + content + """
        </body>
        </html>
    """
    return page
    
   
app.run()