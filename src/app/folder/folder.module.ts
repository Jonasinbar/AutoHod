import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { FolderPageRoutingModule } from './folder-routing.module';

import { FolderPage } from './folder.page';
import { OrderCarComponent } from './OderCar/orderCar.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './Register/Register.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    FolderPageRoutingModule
  ],
  declarations: [
    FolderPage,
    LoginComponent,
    OrderCarComponent,
    RegisterComponent
  ]
})
export class FolderPageModule {}
