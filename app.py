#!flask/bin/python
import Adafruit_BBIO.ADC as ADC
ADC.setup()
from time import sleep
from flask import Flask, request, render_template
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
@app.route('/read')
def index():
	while(1):
		potVal=ADC.read("P9_33")
		potVolt=potVal*1.8
		olt=repr(potVolt)
 		#return olt
		#api.add_resource(olt)
        #print "The Potentiometer Voltage is: ",potVolt
		return render_template('index.html', username=olt)

if __name__ == '__main__':
	app.run(port='5002')
