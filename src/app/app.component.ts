import { Component } from '@angular/core';
@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  public appPages = [
    { title: 'Inbox', url: '/folder/Inbox', icon: 'mail' },
    { title: 'Login', url: '/folder/login', icon: 'paper-plane' },
    { title: 'Register', url: '/folder/Register', icon: 'heart' },
    { title: 'Archived', url: '/folder/Archived', icon: 'archive' },
    { title: 'Personal Area', url: '/folder/PersonalArea', icon: 'person' },
    { title: 'Order Car', url: '/folder/OrderCar', icon: 'car' },
  ];
  public labels = ['Family', 'Friends', 'Notes', 'Work', 'Travel', 'Reminders'];
  constructor() {}
}
