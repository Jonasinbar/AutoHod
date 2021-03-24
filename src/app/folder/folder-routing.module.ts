import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { FolderPage } from './folder.page';
import { OrderCarComponent } from './OrderCar/orderCar.component';
import { PersonalAreaComponent } from './PersonalArea/PersonalArea.component';

const routes: Routes = [
  {
    path: '',
    component: FolderPage,
    children:[
      {
        path: 'OrderCar',
        component: OrderCarComponent
      },
      {
        path: 'PersonalArea',
        component: PersonalAreaComponent
      },
    ]
  },
  

];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class FolderPageRoutingModule {}
