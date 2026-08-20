// function add(a,b){
// return a+b
// }
// console.log(add(10,20))


// console.log("hello bindu")

// let studentname="bindu"
// let age="20"
// let course="python"

// console.log(studentname)
// console.log(age)
// console.log(course)

// let age=20;
// console.log(age)
// age=21;
// console.log(age)

// const college="rit"
// college="rit college"


// let name="bindu"
// let age=20;
// let isstudent=true;
// let salary=null;
// let address=undefined;

// console.log(typeof name)
// console.log(typeof age)
// console.log(typeof isstudent)
// console.log(typeof salary)
// console.log(typeof address)



// let a=5;
// let b=2;

// console.log(a+b);
// console.log(a%b);
// console.log(a*b);
// console.log(a-b);
// console.log(a>b);
// console.log(a<b);
// console.log(a>=b);
// console.log(a<=b);
// console.log(a==b);
// console.log(a===b);



// let age=20;

// console.log(age>20);
// console.log(age<20);
// console.log(age==20);
// console.log(age===20);
// console.log(age!=20);


let age=20;

if(age>=18){
    console.log("eligible to vote")
}else{
    console.log("not eligible to vote")
}


let marks=85;
if (marks >= 90) {
    console.log("Grade: A+");
}
else if(marks >= 80) {
    console.log("Grade: A");
}
else if(marks >= 70){
    console.log("Grade: B+");
}
else if(marks >= 60){
    console.log("Grade: B");
}
else if(marks >= 50){
    console.log("Grade: C");
}
else{
    console.log("Grade: F");
}


let title=document.getElementById("title")
let button=document.getElementById("btn")

button.addEventListener("click",function(){
    title.innerText="button was clicked"
});

document.querySelector("#btn")
document.addEventListener("click",function(){
    alert("clicked")
})