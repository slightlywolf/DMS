from .DeviceInteraction import DeviceInt

class DevControl(DeviceInt):
    """Separation Class to differentiate the the polls
    from the controls"""
    def __init__(self, name, uiName, description):
        super().__init__(name, uiName, description)