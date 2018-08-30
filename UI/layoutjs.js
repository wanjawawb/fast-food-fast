/*
WanjawaWB@gmail.com 
script to draw banner top of page using HTML5 canvas
*/

canvas               = document.getElementById('banner')
context              = canvas.getContext('2d')
context.font         = 'bold italic 80px Georgia'
context.textBaseline = 'top'
image                = new Image()
image.src            = 'pfk.png'

image.onload = function()
{
	gradient = context.createLinearGradient(0, 0, 0, 89)
	gradient.addColorStop(1.00, '#faa') //255,170,170
	gradient.addColorStop(0.00, '#f00') //255,0,0 - red
	context.fillStyle = gradient
	context.fillText(  "Fast Food Fast", 0, 0) //hor & ver offsets
	context.strokeText("Fast-Food-Fast", -10, 0) //hor & ver offsets
	context.drawImage(image, 64, 32)
}
