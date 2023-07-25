import { TestBed } from '@angular/core/testing';

import { TokenManagerService } from './token-manager-service.service';

describe('TokenManagerService', () => {
  let service: TokenManagerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TokenManagerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
