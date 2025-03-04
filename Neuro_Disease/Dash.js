function Loginpage(){
    window.location.href = "login.html";
}

const links=document.querySelectorAll('.link_tab');
links.forEach(link => {
    link.addEventListener('click', () =>{
        document.querySelector('.active')?.classList.remove('active');
        link.classList.add('active');
    })
})