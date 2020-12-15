import flask


app = flask.Flask(__name__)

@app.route('/contact/<category>/<location>', methods=['GET'])
def contact(category,location):
    result = get_info(category, location)
    return 0

def get_info(category, location):  
    url = "https://panoramafirm.pl/szukaj?k={}y&l={}".format(category, location)
    event_selector = "#company-list card.company-item.py-2.container.my-2"
    title_selector = "#company-list "

    return 0  
   
app.run()