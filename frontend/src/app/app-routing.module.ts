import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { LoginComponent } from './components/login/login.component'
import { SignupComponent } from './components/signup/signup.component'
import { TasksComponent } from './components/tasks/tasks.component'

const routes: Routes = [
  { path: 'accounts/login', component: LoginComponent },
  { path: 'accounts/signup', component: SignupComponent },
  { path: '', component: TasksComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
