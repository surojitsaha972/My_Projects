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