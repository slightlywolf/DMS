from ..Device import Dev
from ..DeviceControl import DevControl
from ..DevicePoll import DevPoll


class FakeBattery(Dev):
    def __init__(self, uid=None):
        super().__init__("Fake Battery", uid, "FakeBattery","A fake battery i made to test the front end")

    def populateControls(self) -> None:
        super().controlList[mosfet_toggle.name] = mosfet_toggle()
        super().controlList[shutdown.name] =  shutdown()

    def populatePolls(self) -> None:
        super().pollList[get_voltage.uiName] = get_voltage()
        super().pollList[get_current.name] = get_current()

######Controls ######
class mosfet_toggle(DevControl):
    name = "mosfet_toggle"
    uiName = "Toggle Mosfet"
    description = "Toggles the mosfets on and off"

    def __init__(self):
        super().__init__(self.name, self.uiName, self.description)

    def execute():
        print("Toggling Mosfet")
        return 50

class shutdown(DevControl):
    name = "shutdown"
    uiName = "Shutdown"
    description = "Shuts down the fake battery"

    def __init__(self):
        super().__init__(self.name, self.uiName, self.description)

    def execute():
        print("#############Shutting down#########")
        return 50

#####Polling########
class get_voltage(DevPoll):
    name = "get_voltage"
    uiName = "Get Voltage"
    description = "Gets the voltage"

    def __init__(self):
        super().__init__(self.name, self.uiName, self.description)

    def execute():
        """ Random 50 Voltage """
        return 50

class get_current(DevPoll):
    name = "get_current"
    uiName = "Get Current"
    description = "Gets the voltage"
    
    def __init__(self):
        super().__init__(self.name, self.uiName, self.description)

    def execute():
        """ Random 100 Current """
        return 100

