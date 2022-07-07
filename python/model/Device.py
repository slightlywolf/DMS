"""
The purpose of this file is to create an abstract device in the system
The device will have Controls that dictate functionality
and Polling will dictate getting data from the device
"""

from abc import ABC, abstractmethod
import json

class Dev(ABC):
    """
    The device will have Controls that dictate functionality
    and Polls will dictate getting data from the device
    """

    #Classfields
    controlList = {} #list of control classes: DeviceControl
    pollList = {} #list of polling functions: DevicePoll 

    uiName = None
    uid = None #unique device compared to all other devices
    description = None

    settings = {} #string : value pairs

    @abstractmethod
    def populateControls(self) -> None:
        """
        Populates the control dict with each control"""
        raise NotImplementedError

    @abstractmethod
    def populatePolls(self) -> None:
        """
        Populates the pollList with each Poll 
        """
        raise NotImplementedError

    def __init__(self, 
        uiName,
        deviceName, 
        description,
        uid=None,
        settings=None):

        self.uiName = uiName
        self.uid = uid
        self.deviceName = deviceName
        self.description = description
        self.populateControls() 
        self.populatePolls()
        self.settings = settings

    def toDict(self) -> dict:
        """ Converts a device to json"""
        controlDict = self.getControlsDict()
        pollsDict = self.getPollsDict()

        jsonDict = {
            "uiName": self.uiName,
            "uid": self.uid,
            "description": self.description,
            "controls": controlDict,
            "polls": pollsDict
        }
        return jsonDict

    def toJson(self):
        jsonfile = self.toDict()
        return json.dumps(jsonfile)
    
    def getControlsDict(self) -> dict:
        """ Gets a json/dict file of all of the controls"""
        values = self.controlList.values()
        returndict = {}

        for x in values:
            returndict[x.name] = x.toDict()

        return returndict

    def getPollsDict(self) -> dict:
        """ Gets a json/dict file of all of the polls"""
        values = self.pollList.values()
        returndict = {}

        for x in values:
            returndict[x.name] = x.toDict()

        return returndict

    
    def assignUID(self, uid) -> None:
        """assigns a unique id to the device"""
        self.uid = uid

    