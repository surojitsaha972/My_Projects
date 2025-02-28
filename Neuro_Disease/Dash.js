function Loginpage(){
    window.location.href = "login.html";
}

function changetab(x){
    let txt=document.querySelectorAll("#tab0")
    txt.forEach(txt => {
        txt.addEventListener('click', () =>{
            document.querySelector('.active')?.classList.toggle('active')
            txt.classList.add('active');
        })
    })
}