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

// const form=document.getElementById("form");
// const username=document.getElementById("emailuser");
// const password=document.getElementById("password");
// const fname=document.getElementById("fname");
// const lname=document.getElementById("lname");
// const email=document.getElementById("email");
// const repassword=document.getElementById("repass");

// form.addEventListener('submit',(e)=>{
//     let error=[];
//     if (fname){
//         error=getSignupFormErrors(fname.value,lname.value,email.value,password.value,repassword.value);
//     }
//     else{
//         error=getLoginFormErroes(username.value,password.value);
//     }
//     if(error.length>0){
//         e.preventDefault()
//     }
// })

// function getSignupFormErrors(firstname,lastname,email,password,repassword){
//     let error=[];
//     if(firstname==='' || firstname==null){
//         error.push("First Name is required!")
//     }
//     if(lastname==='' || lastname==null){
//         error.push("last Name is required!")
//     }
//     if(email==='' || email==null){
//         error.push("email is required!")
//     }
//     if(password==='' || password==null){
//         error.push("password is required!")
//     }
//     return error;
// }



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
