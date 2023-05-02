'use strict';
import Noise from './effects/Noise.js';

let menuObj = document.getElementById("menu");

menuObj.style.height = window.innerHeight + "px";
menuObj.style.width = window.innerWidth + "px";

let canvas_width = document.getElementsByClassName('noise_wrapper')[0].clientWidth;
let canvas_height = document.getElementsByClassName('noise_wrapper')[0].clientHeight;

const myNoise = new Noise();

window.addEventListener('load', () => {
    myNoise.Init(canvas_width, canvas_height);
})

window.addEventListener("resize", () => {
    menuObj.style.height = window.innerHeight + "px";
    menuObj.style.width = window.innerWidth + "px";

    let canvas_width = document.getElementsByClassName('noise_wrapper')[0].clientWidth;
    let canvas_height = document.getElementsByClassName('noise_wrapper')[0].clientHeight;

    myNoise.Reset();
})