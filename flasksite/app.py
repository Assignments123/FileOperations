from flask import Flask
import pyqrcode
from PIL import ImageTk,Image
app = Flask(__name__)
@app.route('/home/<username>')
def home(username):
    return "<h> am %s</h>" % username

@app.route('/generate')
def generate():

    link = "https:/www.google.com"
    filename = link +'.png'
    url = pyqrcode.create(link)
    print(url)
    url.png(filename,scale = 8)
    return "inside generate"

app.run(debug=True) 
