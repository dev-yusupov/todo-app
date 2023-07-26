import { Inject, Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpErrorResponse
} from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';
import { authUrl } from '../environments';
import { Router } from '@angular/router';
 
import { TokenManagerService } from '../services/token-manager.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor(
    private tokenService: TokenManagerService,
    @Inject(authUrl) private apiUrl: string,
    private router: Router,
  ) {}

  intercept(
    request: HttpRequest<any>, 
    next: HttpHandler
    ): Observable<HttpEvent<any>> {
      debugger
      const localToken = localStorage.getItem('token');
      
      if (localToken) {
        const cloned = request.clone({
          headers: request.headers.set("Authorization", 
          "JWT" + localToken)
        });

        return next.handle(cloned).pipe(
          catchError((err: HttpErrorResponse) => {
            if (err.status == 401) {
              localStorage.removeItem('token');
              localStorage.removeItem('refresh');
              this.router.navigate(['accounts/login'])
            }

            return throwError(err)
          })
        )
      }
      else {
        return next.handle(request)
      }
  }
}
