/* model device class */
/* this class should only be used to create devices
that come from the python api */
import { Serializable } from "./Serializable";

export class Device implements Serializable<Device>
{
    uiName: String = "n/a";
    uid: Number = -1; 
    description : String = "";

    controlList: object = {};
    pollList: object = {};

    /*generation from file */
    deserialize(input: object) : Device
    {
        /* good enough */
        this.uiName = (input as any).uiName;
        this.uid = (input as any).uid;
        this.description = (input as any).description;

        this.controlList = (input as any).controls;
        this.pollList = (input as any).polls;

        return this;
    }

}