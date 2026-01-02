
    let targetNumber = Math.floor(Math.random() * 100) + 1;
    let attempts = 0;
    let lives = 7;

    function checkGuess() {
        const input = document.getElementById('guessInput');
        const message = document.getElementById('message');
        const guess = parseInt(input.value);

        if (isNaN(guess) || guess < 1 || guess > 100) {
            message.textContent = "Lütfen 1-100 arası bir sayı gir!";
            return;
        }

        attempts++;
        document.getElementById('attempts').textContent = attempts;

        if (guess === targetNumber) {
            message.innerHTML = "🎉 TEBRİKLER! <br> Doğru tahmin!";
            message.style.color = "#4ee44e";
            disableGame();
        } else {
            lives--;
            document.getElementById('lives').textContent = lives;
            
            if (lives === 0) {
                message.innerHTML = "💥 OYUN BİTTİ! <br> Sayı: " + targetNumber;
                message.style.color = "#ff4d6d";
                disableGame();
            } else {
                message.textContent = guess > targetNumber ? "Daha KÜÇÜK bir sayı!" : "Daha BÜYÜK bir sayı!";
                message.style.color = "#f9ed69";
            }
        }
        input.value = "";
        input.focus();
    }

    function disableGame() {
        document.querySelector('button').disabled = true;
        document.getElementById('guessInput').disabled = true;
    }
