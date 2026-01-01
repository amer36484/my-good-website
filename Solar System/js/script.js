// Gezegenleri ve güneşi göstermek için
window.addEventListener('load', () => {
  const sun = document.querySelector('.sun');
  sun.classList.add('appear');

  const planets = document.querySelectorAll('.planet');
  planets.forEach((planet, index) => {
    setTimeout(() => {
      planet.classList.add('appear');
    }, 500 + index * 300); // gezegenler sırayla çıkıyor
  });
});

// Süpernova olayı
function supernovaEvent() {
  alert("5 milyar yıl sonra Güneş patlayacak! 🌞💥");

  // Ses çalma
  const audio = new Audio('supernova.mp3');
  audio.play(100)

  const sun = document.querySelector('.sun');
  sun.classList.add('supernova');

  // Gezegenleri fırlatma animasyonu
  const planets = document.querySelectorAll('.planet');
  planets.forEach(planet => {
    const x = (Math.random() - 0.5) * 3000; // -1500px ila +1500px
    const y = (Math.random() - 0.5) * 3000;

    planet.style.transition = 'transform 3s ease-out';
    planet.style.transform = `translate(${x}px, ${y}px)`;
  });
}

// 5 saniye sonra süpernova başlasın
setTimeout(supernovaEvent, 5000);
