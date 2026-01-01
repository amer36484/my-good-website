const hour = document.querySelector(".hour");
const minute = document.querySelector(".minute");
const second = document.querySelector(".second");

function setDate() {
  const now = new Date();

  const s = now.getSeconds();
  const m = now.getMinutes();
  const h = now.getHours() % 12;

  // 1 saniye = 6°, 1 dakika = 6°, 1 saat = 30°
  const secondDeg = s * 6;
  const minuteDeg = m * 6 + s * 0.1;                  // dakika kolu saniyeye göre akıcı
  const hourDeg   = h * 30 + m * 0.5 + s * (0.5/60);  // akrep dakika+saniyeye göre akıcı

  second.style.transform = `rotate(${secondDeg}deg)`;
  minute.style.transform = `rotate(${minuteDeg}deg)`;
  hour.style.transform   = `rotate(${hourDeg}deg)`;
}

setInterval(setDate, 1000);
setDate();
