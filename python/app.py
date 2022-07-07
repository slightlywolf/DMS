#start of the api that the front end interacts with
from flask import Flask
from flask_cors import CORS
import sys
import json
import os
from DMS_core import Core

###########TEST IMPORTS#############
from model.dev.FakeBattery_ import FakeBattery

#################DEFINITIONS####################
app = Flask(__name__)
CORS(app) #allows cross origin resource sharing
_CORE_ = Core() #initialise the core

#########################INIT#####################
@app.before_first_request   #indicates to run the code before
                            #flask starts
def init():
    # for now just add a device to the core for testing 
    print("addings battery to the core")
    _CORE_.addNewDevice(FakeBattery())
 

#splits inits the other stuff and then starts the api
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

####################ROUTES###########################
@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'


@app.route('/get_data_test')
def get_data():
    return _CORE_.toJSON()


@app.route('/get_devices', methods=['GET'])
def get_devices():
    """returns a json file of all the devices"""
    return _CORE_.toJSON()

#################################################





