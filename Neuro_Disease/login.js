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