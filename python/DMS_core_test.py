"""Testing file for DMS_core_test"""
from DMS_core import Core
from model.dev.FakeBattery_ import FakeBattery

__CORE = Core()

def main():
    __CORE.addNewDevice(FakeBattery())
    writeToFile(__CORE.toJSON(), "testfile2.json")
    

def writeToFile(jsonfile, filename):
    jsonfile = __CORE.toJSON()
    with open(filename,'w') as f:
        f.write(jsonfile)

if __name__ == "__main__":
    main()