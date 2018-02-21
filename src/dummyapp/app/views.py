from flask import render_template
from app import app
import systeminfo
from systeminfo import main
@app.route('/')
def index():
 returnDict = {}
 returnDict['user'] = 'ANJALI' # Feel free to put your name here!
 returnDict['title'] = 'Home'
 returnDict['message'] = main.main()
 return render_template("index.html", **returnDict)
