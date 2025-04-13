// ----- Login Page -----

var a=document.getElementById("login");
var b=document.getElementById("register");

function login(){
    a.style.left="5px";
    b.style.right="-510px";
    a.style.opacity=1;
    b.style.opacity=0;
}

function register(){
    a.style.left="-510px";
    b.style.right="5px";
    a.style.opacity=0;
    b.style.opacity=1;
}

function loginform(){

    // const form=document.getElementById("form");
    var username=document.getElementById("emailuser").value;
    var password=document.getElementById("password").value;
    
    if(username=="" || password==""){
        alert("All Fields are required!")
    }
    else{
        confirm("Login Successfully.")
    }
}

function regform(){
    var fstname=document.getElementById("fname").value;
    var lstname=document.getElementById("lname").value;
    var email=document.getElementById("email").value;
    var password=document.getElementById("password").value;
    var repassword=document.getElementById("repass").value;
    if(fstname=="" || lstname=="" || email=="" || password=="" || repassword==""){
        alert("All Fields are required!")
    }
    else if(password!=repassword){
        alert("Password are not matched!")
    }
    else{
        confirm("Registered Successfully.")
    }
}



// ----- Dashboard Page ------

function Loginpage(){
    window.location.href = "login.html";
}


const links=document.querySelectorAll('.alphaorder ul li');
links.forEach(link =>{
    link.addEventListener('click', function(){
        document.querySelectorAll('.alphaorder ul li, .alpha').forEach(el => el.classList.remove('active'));
        this.classList.add('active');
        let targetid=this.querySelector('a').getAttribute('data-target');
        let targetel=document.getElementById(targetid);
        if(targetel){
            targetel.classList.add('active');
        }
    })
})


// ----- Disease Details ------


function ald_page(){
    window.location.href = "Adrenoleukodystrophy.html";
}

function ad_page(){
    window.location.href = "Alzheimer's Disease.html";
}

function brain_page(){
    window.location.href = "brainstroke.html";
}

function alex_page(){
    window.location.href = "AlexanderDisease.html";
}

function als_page(){
    window.location.href = "AmyotrophicLateralSclerosis.html";
}
