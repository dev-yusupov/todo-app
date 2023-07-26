import { HttpRequest } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { JwtHelperService, } from '@auth0/angular-jwt'

@Injectable({
  providedIn: 'root'
})
export class TokenManagerService {

  private _jwtHelper = JwtHelperService;

  constructor( private jwtHelper: JwtHelperService ) { }

  isExpired(accessToken: string): boolean {
    return this.jwtHelper.isTokenExpired(accessToken);
  }

  getToken() {
    const token = localStorage.getItem('token');

    if(token) {
      return JSON.parse(token);
    }
    return null;
  }

  // addTokenHeader(request: HttpRequest<any>, token: string) {
  //   return request.clone({
  //     headers: request.headers.set(TOKEN)
  //   })
  // }
}
