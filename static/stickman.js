const canvas = document.getElementById('myCanvas');
const context = canvas.getContext('2d');
context.beginPath();
context.fillStyle = "bisque"; // #ffe4c4
context.arc(200, 50, 30, 0, Math.PI * 2, true); // draw circle for head
// (x,y) center, radius, start angle, end angle, anticlockwise
context.fill();

context.beginPath();
context.strokeStyle = "red"; // color
context.lineWidth = 3;
context.arc(200, 50, 20, 0, Math.PI, false); // draw semicircle for smiling
context.stroke();

// eyes
context.beginPath();
context.fillStyle = "green"; // color
context.arc(190, 45, 3, 0, Math.PI * 2, true); // draw left eye
context.fill();
context.arc(210, 45, 3, 0, Math.PI * 2, true); // draw right eye
context.fill();

// body
context.beginPath();
context.moveTo(200, 80);
context.lineTo(200, 180);
context.strokeStyle = "navy";
context.stroke();

// arms
context.beginPath();
context.strokeStyle = "#0000ff"; // blue
context.moveTo(200, 80);
context.lineTo(150, 130);
context.moveTo(200, 80);
context.lineTo(250, 130);
context.stroke();

// legs
context.beginPath();
context.strokeStyle = "orange";
context.moveTo(200, 180);
context.lineTo(150, 280);
context.moveTo(200, 180);
context.lineTo(250, 280);
context.stroke();
