import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';


// import { Router, ActivatedRoute } from '@angular/router';
// import { FormBuilder, FormGroup, Validators } from '@angular/forms';
// import { first } from 'rxjs/operators';

// import { AccountService, AlertService } from '@app/_services';

@Component({
    templateUrl: './orderCar.component.html',
    styleUrls: ['./orderCar.component.scss']
}
    )
export class OrderCarComponent implements OnInit {

    
    @ViewChild('dates') dates : ElementRef

    constructor(private router: Router, private http: HttpClient){ }


    ngOnInit() {}

    date()
    {
        var dates = this.dates.nativeElement.value
        console.log(dates)
        if(dates=="")
        {
            alert("please choose date")
        }
        else
        {
            var jsonOutput: JSON;
            var obj: any = 
            [
            {"date": dates},
            ];
            jsonOutput = <JSON>obj;
            this.http.post("/keepACar", jsonOutput).subscribe(data => {
                console.log(data) 
            
            }, err => {

            })
            console.log(jsonOutput);

        }
        
    }
}
