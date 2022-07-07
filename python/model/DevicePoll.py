from abc import ABC, abstractmethod
from .DeviceInteraction import DeviceInt

class DevPoll(DeviceInt):
    """Separation Class to differentiate the the polls
    from the controls"""
    def __init__(self, name, uiName, description):
        super().__init__(name, uiName, description)
   