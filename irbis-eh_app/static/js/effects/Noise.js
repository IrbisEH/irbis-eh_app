function Noise()
{
    this.amountFrames = 10;

    //black 0xff000000
    //white 0xffffffff
    this.colorNoise = 0xffffffff;
    this.noiseFrequency = 0.6;
    this.timeoutSec = 5;

    this.canvas = null;
    this.ctx = null;
    this.wWidth = null;
    this.wHeight = null;
    this.framesData = [];
    this.idxFrame = 0;
    this.loopTimeout = null;
    this.resizeThrottle = null;

    this.Init();
}

Noise.prototype.Init = function()
{
    let _this = this;

    _this.canvas = document.getElementById("noise");
    _this.ctx = _this.canvas.getContext("2d")

    _this.Setup();
    _this.Reset();
}

Noise.prototype.Setup = function ()
{
    let _this = this;

    // this.idxFrame = 0;
    this.framesData = [];

    _this.wWidth = window.innerWidth;
    _this.wHeight = window.innerHeight;

    _this.canvas.width = _this.wWidth;
    _this.canvas.height = _this.wHeight;

    for (let i = 0; i < _this.amountFrames; i++) {
        _this.CreateNoise();
    }

    _this.Loop();
}

Noise.prototype.CreateNoise = function ()
{
    let _this = this;

    let imageData = _this.ctx.createImageData(_this.wWidth, _this.wHeight);
    let buffer32 = new Uint32Array(imageData.data.buffer);

    for (let i = 0; i < buffer32.length; i++) {
        if (Math.random() < _this.noiseFrequency) {
            buffer32[i] = _this.colorNoise;
        }
    }
    _this.framesData.push(imageData);
}

Noise.prototype.Loop = function ()
{
    let _this = this;

    _this.PaintNoise();

    _this.loopTimeout = window.setTimeout(() => {
        window.requestAnimationFrame(_this.Loop.bind(_this));
    }, _this.timeoutSec);

}

Noise.prototype.PaintNoise = function ()
{
    let _this = this;

    if (_this.idxFrame === _this.amountFrames - 1) {
        _this.idxFrame = 0;
    } else {
        _this.idxFrame++;
    }
    _this.ctx.putImageData(_this.framesData[_this.idxFrame], 0, 0)
}

Noise.prototype.Reset = function () {
    let _this = this;
    _this.framesData = [];
    _this.idxFrame = 0;
    for (let i = 0; i < _this.amountFrames; i++) {
        _this.CreateNoise();
    }
}

export default Noise;