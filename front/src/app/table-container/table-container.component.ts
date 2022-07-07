import { Component, OnInit } from '@angular/core';
import { BackCommsService } from '../back-comms.service';
import { DeviceService } from '../device.service';

@Component({
  selector: 'app-table-container',
  templateUrl: './table-container.component.html',
  styleUrls: ['./table-container.component.css']
})
export class TableContainerComponent implements OnInit {


  constructor(private devservice: DeviceService) { }

  ngOnInit(): void 
  {
  }

  /* testing function that will put text randomly on the screen */
  displayBullshit()
  {
    return this.devservice.getDevices()
  }


  /* test function for getting devices as json and
  putting them on the screen */
  getDevices()
  {

  }

}
