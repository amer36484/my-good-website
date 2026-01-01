const canvas = document.getElementById("playground");
const ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
let balls = [];
class Ball {
  constructor(x, y, radius, color) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.color = color;
    this.dx = (Math.random() - 0.5) * 6;
    this.dy = Math.random() * 3 + 2;
    this.gravity = 0.3;
    this.friction = 0.8;
  }
  draw() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = this.color;
    ctx.fill();
    ctx.closePath();
  }
  update() {
    if (this.y + this.radius + this.dy > canvas.height) {
      this.dy = -this.dy * this.friction;
    } else {
      this.dy += this.gravity;
    }
    if (
      this.x + this.radius + this.dx > canvas.width ||
      this.x - this.radius + this.dx < 0
      ) {
      this.dx = -this.dx;
    }
    this.x += this.dx;
    this.y += this.dy;
    this.draw();
  }
}
function randomColor() {
  return `hsl(${Math.random() * 360}, 70%, 50%)`;
}
function addBall(x, y) {
  const radius = Math.random() * 30 + 15;
  balls.push(new Ball(x, y, radius, randomColor()));
}
canvas.addEventListener("click", (e) => {
  addBall(e.clientX, e.clientY);
});
function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  balls.forEach((ball) => ball.update());
  requestAnimationFrame(animate);
}
animate();