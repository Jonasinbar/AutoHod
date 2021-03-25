import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { Router } from '@angular/router';
// import { Router, ActivatedRoute } from '@angular/router';
// import { FormBuilder, FormGroup, Validators } from '@angular/forms';
// import { first } from 'rxjs/operators';

// import { AccountService, AlertService } from '@app/_services';

@Component({
    templateUrl: './Register.component.html',
    styleUrls: ['./Register.component.scss']
}
    )
export class RegisterComponent implements OnInit {
    @ViewChild('username') username : ElementRef
    @ViewChild('personal_id') personal_id : ElementRef
    @ViewChild('team') team : ElementRef
    @ViewChild('license_type') license_type : ElementRef
    @ViewChild('phone_number') phone_number : ElementRef
    @ViewChild('pwd') pwd : ElementRef

    constructor(private router: Router){ }


    ngOnInit() {
        
    }
    Register() {
        
        var username = this.username.nativeElement.value
        var personal_id = this.personal_id.nativeElement.value
        var team = this.team.nativeElement.value
        var license_type = this.license_type.nativeElement.value
        var phone_number = this.phone_number.nativeElement.value
        var pwd = this.pwd.nativeElement.value
        

        if(username=="" || personal_id=="" || team=="" || license_type=="" || phone_number=="" || pwd==""){
            alert("please provide all the informations")
        }
        else{
            var jsonOutput: JSON;
            var obj: any = 
            [
            {"username": username},
            {"personal_id": personal_id},
            {"team": team},
            {"license_type": license_type},
            {"phone_number": phone_number},
            {"pwd": pwd},
            ];
            jsonOutput = <JSON>obj;
            console.log(jsonOutput)
            const navigationDetails: string[] = ['folder/PersonalArea'];
            this.router.navigate(navigationDetails,{ queryParams: { username: username , personal_id : personal_id ,team: team , license_type : license_type ,phone_number: phone_number , pwd : pwd} });
        }
    }
}