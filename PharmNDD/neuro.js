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
    var username=document.getElementById("emailuser").value;
    var password=document.getElementById("password").value;
    
    if(username=="" || password==""){
        alert("All Fields are required for signin!")
    }
    else{
        confirm("Login Successfully.")
    }
}

function regform(){
    var name=document.getElementById("fname").value;
    var phone=document.getElementById("number").value;
    var email=document.getElementById("email").value;
    var password=document.getElementById("pass").value;
    var repassword=document.getElementById("repass").value;

    if(name=="" || phone=="" || email=="" || password=="" || repassword==""){
        alert("All Fields are required for registration!");
    }
    else if(phone.length>10 || phone.length<10){
        alert("No. should be of 10 digits ! Enter valid contact number!");
    }
    else if(isNaN(phone)){
        alert("Only numbers are allowed ! Enter valid contact number!");
    }
    else if(password!=repassword){
        alert("Password are not matched!");
    }
    else{
        confirm("Registered Successfully.");
    }
}

function enablelogbtn(){
    var check=document.getElementById("login-check");
    var btn=document.getElementById("logbtn");
    if(check.checked){
        btn.removeAttribute("disabled");
    }
    else{
        btn.disabled="true";
    }
}

function enableregbtn(){
    var check=document.getElementById("register-check");
    var btn=document.getElementById("regbtn");
    if(check.checked){
        btn.removeAttribute("disabled");
    }
    else{
        btn.disabled="true";
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


// ----- Home Page ------

function check(){
    window.location.href="Dashboard.html";
}