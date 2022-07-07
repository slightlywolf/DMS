import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { catchError, retry } from 'rxjs/operators';
import { Observable, throwError  } from 'rxjs';


@Injectable({
  providedIn: 'root'
})

/* back coms service handles the interaction between the front end and the back end of the
system */
export class BackCommsService {
  
  private REST_API_SERVER = "http://10.22.30.88:5010" /* flask server */
  constructor(private http: HttpClient){ }
  
  /* gets headers for the http requests */
  private getHeaders() : HttpHeaders
  {
    const headers = new HttpHeaders()
    .set('content-type','application/json')
    .set('Access-Control-Allow-Origin','*');
    return headers
  }

  /* gets an observable from the link */
  /* gets a observable<json> from the rest api server given the end string */
  getObservable(appension: string): Observable<string>
  {
    return this.http.get<string>(this.REST_API_SERVER + appension,
      {'headers' : this.getHeaders()});
  }

  /* ****************************CORE**********************/
  /* gets all the devices in json format */
  private CoreObservable?: Observable<string>;
  private GET_DEVICES = "/get_devices";
  getCore() : Observable<string> /* returns a json object */
  { 
    if (this.CoreObservable)
      return this.CoreObservable
    else
      return this.get_core_observable()
  }

  /* gets the core observable, assigns it and returns it */
  get_core_observable() : Observable<string>
  {
    this.CoreObservable = this.getObservable(this.GET_DEVICES);
    return this.CoreObservable;
  }




}
