'use strict';
// import Noise from './effects/Noise.js';


// console.log(window.)




let canvas_width = document.getElementsByClassName('noise_wrapper')[0].clientWidth;
let canvas_height = document.getElementsByClassName('noise_wrapper')[0].clientHeight;

console.log(canvas_width)
console.log(canvas_height)
// const myNoise = new Noise();

window.addEventListener('load', () => {
    // myNoise.Init(canvas_width, canvas_height);
})

window.addEventListener("resize", () => {


    let canvas_width = document.getElementsByClassName('noise_wrapper')[0].clientWidth;
    let canvas_height = document.getElementsByClassName('noise_wrapper')[0].clientHeight;

    // myNoise.Reset();
})