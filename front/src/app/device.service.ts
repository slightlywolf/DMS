import { compileClassMetadata } from '@angular/compiler';
import { Injectable } from '@angular/core';
import { BackCommsService } from './back-comms.service';
import { Device } from './model/device';

@Injectable({
  providedIn: 'root'
})
export class DeviceService {
  devices: object = [];


  /* list of devices */

  getDevices() : object
  {
    this.update_devices
    return this.devices;
  }

  /* grabs ths observable off the back comms and subscribes
  to it to fill the list of devices */
  update_devices() 
  {
    this.backComms.getCore().subscribe(
        (x) => { this.devices = JSON.parse(x); },
        (err) => { console.log("ERROR:" + err)},
        () => {}
      );
  }

  constructor(private backComms: BackCommsService ) 
  { 
    this.update_devices(); /* should populate the obect immediately */
  }


}
export interface Devices{
  uiName : string;
  uid : string;
  description: string;

  controls : Controls;
  polls : Polls;

  settings : Settings;
}

export interface Controls{
  name : string;
  uiName : string;
  description : string;

  settings : Settings;
}

export interface Polls{
  name : string;
  uiName : string;
  description : string;

  settings : Settings;

}
export interface Settings{
  [setting: string]: string
}