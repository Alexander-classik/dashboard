document.addEventListener('DOMContentLoaded', () => {
  
  // Обработка кликов по заголовкам секций для сворачивания/разворачивания
  document.querySelectorAll('.collapsible-section .section-header').forEach(header => {
    header.addEventListener('click', () => {
      const section = header.parentElement;
      section.classList.toggle('collapsed');
      
      // Можно обновить иконку стрелки
      const icon = header.querySelector('.toggle-icon');
      if (icon) {
        if (section.classList.contains('collapsed')) {
          icon.textContent = '►'; // стрелка вправо
        } else {
          icon.textContent = '▼'; // стрелка вниз
        }
      }
      
    });
    
    // Изначально установить стрелки в правильное положение
    const section = header.parentElement;
    const icon = header.querySelector('.toggle-icon');
    if (icon) {
      if (section.classList.contains('collapsed')) {
        icon.textContent = '►';
      } else {
        icon.textContent = '▼';
      }
    }
    
  });

  
// Обновление времени каждую секунду
function updateClock() {
const clock = document.getElementById('clock');
if (clock) {
const now = new Date();
clock.textContent = now.toLocaleString();
}
setTimeout(updateClock,1000);
}
updateClock();

// Получение IP-адреса с сервера
fetch('/get_ip')
.then(response => response.json())
.then(data => {
const ipDiv = document.getElementById('ip-address');
if (ipDiv) { ipDiv.textContent = 'IP: ' + data.ip; }
})
.catch(error => { console.error('Ошибка при получении IP:', error); });
});
  
// Функция для запуска виртуальной машины (пример)
function launchVM(vm_id) {
alert('Запуск виртуальной машины: ' + vm_id);
}

// Анимация градиента у секций
const sections = document.querySelectorAll('.animated-border');

sections.forEach(section => {
let offset =0;

function animate() {
offset= (offset +1)%1400;
// Обновляем CSS переменную --gradient-offset
section.style.setProperty('--gradient-offset', `${offset}px`);
requestAnimationFrame(animate);
}

animate();
});