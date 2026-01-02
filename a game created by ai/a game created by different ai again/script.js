const game = document.getElementById('game');
const scoreEl = document.getElementById('score');
const timeEl = document.getElementById('time');
const startBtn = document.getElementById('start');

let score = 0;
let time = 30;
let timerId = null;
let spawnId = null;

function randomPos(max) {
  return Math.floor(Math.random() * max);
}

function spawnTarget() {
  const t = document.createElement('div');
  t.className = 'target';
  t.style.left = randomPos(game.clientWidth - 28) + 'px';
  t.style.top = randomPos(game.clientHeight - 28) + 'px';
  t.onclick = () => {
    score++;
    scoreEl.textContent = score;
    t.remove();
  };
  game.appendChild(t);
  setTimeout(() => t.remove(), 900);
}

function startGame() {
  score = 0;
  time = 30;
  scoreEl.textContent = score;
  timeEl.textContent = time;
  game.innerHTML = '';

  clearInterval(timerId);
  clearInterval(spawnId);

  timerId = setInterval(() => {
    time--;
    timeEl.textContent = time;
    if (time <= 0) endGame();
  }, 1000);

  spawnId = setInterval(spawnTarget, 450);
}

function endGame() {
  clearInterval(timerId);
  clearInterval(spawnId);
  alert('Oyun bitti! Puanın: ' + score);
}

startBtn.onclick = startGame;
