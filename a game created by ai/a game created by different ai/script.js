  const box = document.getElementById("box");
  const scoreText = document.getElementById("score");
  let score = 0;

  function moveBox() {
    const x = Math.random() * (window.innerWidth - 60);
    const y = Math.random() * (window.innerHeight - 60);
    box.style.left = x + "px";
    box.style.top = y + "px";
  }

  box.addEventListener("click", () => {
    score++;
    scoreText.textContent = "Puan: " + score;
    moveBox();
  });

  moveBox();
