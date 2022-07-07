from abc import ABC, abstractmethod


class DeviceInt(ABC):
    """ 
    Controls for the device, this will determine what can be done to the device
    e.g. turn off turn on etc
    """
    #class fields
    name = None
    uiName = None #prettier name for UI
    description = None
      
    settings = {}

    def __init__(self, name, uiName, description):
        self.name = name
        self.uiName = uiName  
        self.description = description

    @abstractmethod
    def execute():
        raise NotImplementedError

    @staticmethod
    def execute_method(module, methodname):
        """    
        executes a method given the name of the method and the 
        module
        """
        foo = getattr(module, methodname)
        foo()

    def toDict(self):
        returnDict = {
            "name": self.name,
            "uiName": self.uiName,
            "description" : self.description,
            "settings" : self.settings
        }
        return returnDict
       

DeviceInt.execute_method=staticmethod(DeviceInt.execute_method)