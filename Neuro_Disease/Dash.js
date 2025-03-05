function Loginpage(){
    window.location.href = "login.html";
}

const links=document.querySelectorAll('.link_tab');
const tabs=document.querySelectorAll('.alpha');
links.forEach(link => {
    link.addEventListener('click', () => {
        link.document.querySelector('.active')?.classList.remove('active');
        link.classList.add('active');
        // tabs.document.querySelector('.active')?.classList.remove('active');
        // tabs.classList.add('active');
    })
})