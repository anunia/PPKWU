import flask
import vcard

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def hrllo():
    return "Hello"
@app.route('/contact/<category>/<location>', methods=['GET'])
def contact(category,location):
    result = get_info(category, location)
    return 0

def get_info(category, location):  
    url = "https://panoramafirm.pl/szukaj?k={}y&l={}".format(category, location)
    list_selector = "#company-list .card.company-item.py-2.container.my-2"
    name_selector = "#company-list [title = \"Zobacz informacje szczegółowe o firmie\"]"
    address_selector = "#company-list .address"
    number_selector = "#company-list .icon-telephone.addax.addax-cs_hl_phonenumber_click"
    url_selector = "#company-list .icon-website.addax addax-cs_hl_hit_homepagelink_click"
    email_selector = "#company-list .ajax-modal-link.icon-envelope cursor-pointer.addax addax-cs_hl_email_submit_click"

    info = urlopen(url)
    html = BeautifulSoup(info.read())
    selected_elements = html.select(list_selector)
    
    c = []

    for contact in selected_elements:
       c
        
    return 0  
   
app.run()