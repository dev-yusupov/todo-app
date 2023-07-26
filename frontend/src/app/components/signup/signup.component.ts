import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, FormControl } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit{
  public formGroup!: FormGroup;

  constructor(
    private router: Router,
    private http: HttpClient,
    private formBuilder: FormBuilder,
  ) { }

  ngOnInit(): void {
    this.formGroup = this.formBuilder.group({
      username: '',
      email: '',
      password1: '',
      password2: ''
    })
  }

  submit() {
    this.http.post(`http://127.0.0.1:8000/accounts/api/v1/registration/`, this.formGroup.getRawValue(), {
      withCredentials: true 
    }).subscribe((response) => {
      this.router.navigate(['accounts/login']);
      
    });
    console.log(this.formGroup.getRawValue())
  }
}
