import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { authUrl } from '../environments'

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }
  
  onLogin(obj: any) {
    this.http.post(`${authUrl}/login`, obj);
  }
}
