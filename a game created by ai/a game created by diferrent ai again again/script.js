const secretNumber = Math.floor(Math.random() * 100) + 1;
let attemptsLeft = 8;
let guessCount = 0;

const messageEl = document.getElementById('message');
const guessInput = document.getElementById('guessInput');
const guessBtn = document.getElementById('guessBtn');
const attemptsEl = document.getElementById('attemptsLeft');
const countEl = document.getElementById('guessCount');
const restartBtn = document.getElementById('restart');

function updateStats() {
  attemptsEl.textContent = attemptsLeft;
  countEl.textContent = guessCount;
}

function disableGame() {
  guessInput.disabled = true;
  guessBtn.disabled = true;
  restartBtn.style.display = 'block';
}

guessBtn.addEventListener('click', () => {
  const guess = Number(guessInput.value);
  
  if (isNaN(guess) || guess < 1 || guess > 100) {
    messageEl.textContent = "1 ile 100 arasında bir sayı gir lütfen! 😅";
    messageEl.style.color = "#ffd93d";
    return;
  }

  guessCount++;
  updateStats();

  if (guess === secretNumber) {
    messageEl.textContent = `Tebrikler! 🎉 ${guessCount}. tahminde buldun!`;
    messageEl.style.color = "#4cd137";
    disableGame();
  } 
  else if (guess < secretNumber) {
    messageEl.textContent = "Daha YÜKSEK bir sayı düşün ↑";
    messageEl.style.color = "#ff9f43";
    attemptsLeft--;
  } 
  else {
    messageEl.textContent = "Daha DÜŞÜK bir sayı düşün ↓";
    messageEl.style.color = "#ff9f43";
    attemptsLeft--;
  }

  if (attemptsLeft <= 0 && guess !== secretNumber) {
    messageEl.textContent = `Maalesef bitti! 😔 Doğru sayı: ${secretNumber}`;
    messageEl.style.color = "#ff4757";
    disableGame();
  }

  guessInput.value = '';
  guessInput.focus();
});

restartBtn.addEventListener('click', () => {
  location.reload();
});

// Enter tuşu ile de tahmin yapılabilsin
guessInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    guessBtn.click();
  }
});
