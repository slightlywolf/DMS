import { TestBed } from '@angular/core/testing';

import { BackCommsService } from './back-comms.service';

describe('BackCommsService', () => {
  let service: BackCommsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BackCommsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
