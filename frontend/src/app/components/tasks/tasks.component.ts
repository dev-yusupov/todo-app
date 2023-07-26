import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css']
})
export class TasksComponent implements OnInit {

  tasks: any;

  constructor(
    private http: HttpClient,
    private authService: AuthService,
  ) { }

  ngOnInit(): void {
    this.http.get('http://127.0.0.1:8000/tasks/api/v1/').subscribe(response => {
      console.log(this.authService.isLoggedIn())
    })
  }

}
