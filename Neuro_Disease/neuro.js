// ----- Login Page -----

var a=document.getElementById("login");
var b=document.getElementById("register");

function login(){
    a.style.left="5px";
    b.style.right="-500px";
    a.style.opacity=1;
    b.style.opacity=0;
}

function register(){
    a.style.left="-510px";
    b.style.right="5px";
    a.style.opacity=0;
    b.style.opacity=1;
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


// const links=document.querySelectorAll('.alphaorder ul li');
// links.forEach(link =>{
//     link.addEventListener('click', function(){
//         document.querySelectorAll('.alphaorder ul li, .alpha').forEach(el => el.classList.remove('active'));
//         this.classList.add('active');
//         let targetid=this.querySelector('a').getAttribute('data-target');
//         let targetel=document.getElementById(targetid);
//         if(targetel){
//             targetel.classList.add('active');
//         }
//     })
// })