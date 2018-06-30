from app import app
from service import UbsService
@app.route('/')
@app.route('/index')
@app.route('/ayn')

def index():
    return UbsService.pdConvertCSVtoJSON("resources/ubs.csv")

def ayn():
    return "ayn ayn ayn ayn AAAAAAAAYN!"