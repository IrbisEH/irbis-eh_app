'use strict';
import Noise from './effects/Noise.js';

const menuNoise = new Noise();

let cur_width = window.innerWidth;
let cur_height = window.innerHeight;

menuNoise.Init(cur_width, cur_height);

window.addEventListener("resize", () => {

    menuNoise.wWidth = window.innerWidth;
    menuNoise.wHeight = window.innerHeight;
    menuNoise.Reset();
})