'use strict';
import Noise from './effects/Noise.js';

// let canvas_width = document.getElementsByClassName('noise_wrapper')[0].clientWidth;
// let canvas_height = document.getElementsByClassName('noise_wrapper')[0].clientHeight;

const myNoise = new Noise();

// console.log(canvas_width);
// console.log(canvas_height);
// console.log(myNoise);


// let cur_width = parseInt(window.innerWidth);
// let cur_height = parseInt(window.innerHeight);

let cur_width = window.innerWidth;
let cur_height = window.innerHeight;


// myNoise.Init(cur_width, cur_height);


// window.addEventListener('load', () => {
//     // myNoise.Init(canvas_width, canvas_height);
// })
//
// window.addEventListener("resize", () => {
//
//
//     let canvas_width = document.getElementsByClassName('noise_wrapper')[0].clientWidth;
//     let canvas_height = document.getElementsByClassName('noise_wrapper')[0].clientHeight;
//
//     // myNoise.Reset();
// })