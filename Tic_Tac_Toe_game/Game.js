let boxes=document.querySelectorAll(".box");
let resetbut=document.querySelector("#reset_but");
let newbut=document.querySelector(".newbut");
let newcont=document.querySelector(".newcon");
let msg=document.querySelector(".msg");

let turn0=true;
const chpattern=[
    [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]
];

const resetgame=()=>{
    turn0=true;
    enablebox();
    newcont.classList.add("hide");
}

boxes.forEach((box)=>{
    box.addEventListener("click",()=>{
        console.log("Button was clicked.");
        if(turn0==true){
            box.innerText="O";
            turn0=false;
        }
        else{
            box.innerText="X";
            box.style.color="black";
            turn0=true;
        }
        box.disabled=true;
        checkwinner();
    });
});

const showwinner=(winner)=>{
    msg.innerText=`Congratulations, the winner is ${winner}`;
    newcont.classList.remove("hide");
}

const disabledbut=()=>{
    for(let box of boxes){
        box.disabled=true;
    }
};

const enablebox=()=>{
    for(let box of boxes){
        box.disabled=false;
        box.innerText="";
    }
};

const checkwinner=()=>{
    for(pat of chpattern){
        // console.log(pat[0],pat[1],pat[2]);
        // console.log(boxes[pat[0]].innerText,boxes[pat[1]].innerText,boxes[pat[2]].innerText);
        let pos1val=boxes[pat[0]].innerText;
        let pos2val=boxes[pat[1]].innerText;
        let pos3val=boxes[pat[2]].innerText;
        if(pos1val!=""&&pos2val!=""&&pos3val!=""){
            if(pos1val==pos2val&& pos2val==pos3val){
                console.log("winner");
                disabledbut();
                showwinner(pos1val);
            };
        };
    };
};

newbut.addEventListener("click", resetgame);
resetbut.addEventListener("click", resetgame);