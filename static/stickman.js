const canvas = document.getElementById('myCanvas');
const context = canvas.getContext('2d');
context.beginPath();
context.fillStyle = "bisque"; // #ffe4c4
context.fill();

var head = {
  draw : function() {
    context.beginPath();
    context.fillStyle = "bisque"; // #ffe4c4
    context.arc(200, 50, 30, 0, Math.PI * 2, true); // draw circle for head
    context.arc(200, 450, 50, 0, Math.PI * 2, true);
    // (x,y) center, radius, start angle, end angle, anticlockwise
    context.fill();
  }
};

var right_eye = {
  draw : function() {
    context.beginPath();
    context.fillStyle = "green"; // color
    context.arc(210, 45, 3, 0, Math.PI * 2, true); // draw right eye
    context.fill();
  }
};

var left_eye = {
  draw : function() {
    context.beginPath();
    context.fillStyle = "green"; // color
    context.arc(190, 45, 3, 0, Math.PI * 2, true); // draw left eye
    context.fill();
  }
};

var body = {
  draw : function() {
    context.beginPath();
    context.moveTo(200, 80);
    context.lineTo(200, 180);
    context.strokeStyle = "navy";
    context.stroke();
  }
};

var left_arm = {
    draw : function() {
        context.beginPath();
        context.strokeStyle = "#0000ff"; // blue
        context.moveTo(200, 80);
        context.lineTo(150, 130);
        context.stroke();
      }
};

var right_arm = {
    draw : function() {
        context.beginPath();
        context.strokeStyle = "#0000ff"; // blue
        context.moveTo(200, 80);
        context.lineTo(250, 130);
        context.stroke();
      }
};

var left_leg = {
    draw : function() {
        context.beginPath();
        context.strokeStyle = "orange";
        context.moveTo(200, 180);
        context.lineTo(150, 280);
        context.stroke();
      }
};

var right_leg = {
  draw : function() {
    context.beginPath();
    context.strokeStyle = "orange";
    context.moveTo(200, 180);
    context.lineTo(250, 280);
    context.stroke();
  }
};

var smile = {
    draw : function() {
      context.beginPath();
      context.strokeStyle = "red"; // color
      context.lineWidth = 3;
      context.arc(200, 50, 20, 0, Math.PI, false); // draw semicircle for smiling
      context.stroke();
   }
};
