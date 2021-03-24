import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { Router } from '@angular/router';
// import { Router, ActivatedRoute } from '@angular/router';
// import { FormBuilder, FormGroup, Validators } from '@angular/forms';
// import { first } from 'rxjs/operators';

// import { AccountService, AlertService } from '@app/_services';

@Component({
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.scss']
}
    )
export class LoginComponent implements OnInit {
    @ViewChild('pwd') pwd : ElementRef
    @ViewChild('usr') usr : ElementRef

    constructor(private router: Router){ }


    ngOnInit() {
        
    }

    jonas() {
        var user = this.usr.nativeElement.value
        var password = this.pwd.nativeElement.value
        if(user=="" || password==""){
            alert("please provide all the informations")
        }
        else{
            var jsonOutput: JSON;
            var obj: any = 
            [
            {"userId": user},
            {"password": password},
            ];
            jsonOutput = <JSON>obj;
            console.log(jsonOutput)
            const navigationDetails: string[] = ['folder/PersonalArea'];
            this.router.navigate(navigationDetails,{ queryParams: { username: user , pwd : password} });
        }
        



    }
}