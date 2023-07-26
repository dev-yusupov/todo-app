import { Component, OnInit } from '@angular/core';
import { FormGroup, Validators, FormControl, FormBuilder } from '@angular/forms'
import { AuthService } from '../../services/auth.service';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  public formGroup!: FormGroup;

  constructor(
    private http: HttpClient,
    private formBuilder: FormBuilder,
    private router: Router,
    ) { }

  controlsConfig = {}

  ngOnInit(): void {

    this.formGroup = this.formBuilder.group({
      email: ['', Validators.required],
      password: ['', Validators.required],
    });
    
  }
  response: any;

  submit(): void {
    this.http.post(`http://127.0.0.1:8000/accounts/api/v1/login/`, this.formGroup.getRawValue(), {
      withCredentials: true,
    }).subscribe((response) => {
      this.router.navigate(['/']);
      this.response = response;
      var token = this.response.access;
      var refresh = this.response.refresh;
      localStorage.setItem('token', token);
      localStorage.setItem('refresh', refresh);
    });
  }
}

