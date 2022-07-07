"""
The core will be responsible to manage all 
"""
from model.Device import Dev
from model.dev.FakeBattery_ import FakeBattery

import json
from itertools import count, filterfalse


_D = 1 #debug level 

class Core:
    """Runs the core functionality of the system"""
    devices = {} # key : int, value : Device object
############################
    def __init__(self):
        pass
##############################

    def addNewDevice(self,new_device) -> str:
        #adds a new device to the list
        new_device.assignUID(self.allocateNewDeviceID())
        self.devices[new_device.uid] = new_device


    def allocateNewDeviceID(self) -> int:
        listOfKeys = self.devices.keys()
        value = self.__smallestPosInt(listOfKeys)
        if(_D):print ("New id"+ str(value)) #DEBUG
        return value

    def toJSON(self):
        """Converts all data to json"""
        jsonfile = self.getDevicesDict()
        if(_D):print ("toJson: " + str(jsonfile)) #DEBUG
        return json.dumps(jsonfile)


    def getDevicesDict(self) -> dict:
        """Gets a dictionary of all the devices"""
        values = self.devices.values()
        if(_D):print ("GetDevicesDict: " + str(values)) #DEBUG
        returnDict = {}

        for xx in values:
            returnDict[xx.uid] = xx.toDict()

        return returnDict

#################################### PRIVATE
    def __smallestPosInt(self, alist) -> int:
        """Returns the smallest positive int from a set"""
        #https://stackoverflow.com/questions/28176866/find-the-smallest-positive-number-not-in-list
        if(bool(alist) == False): #Empty List 
            return 1
        else: #Non empty list 
            value = min(set(range(max(alist) + 2)) - set(alist))
            if(_D):print ("##############"+str(value)) #DEBUG
            return value
