const modeSwitch = document.getElementById('modeSwitch');

modeSwitch.addEventListener('change', () => {
  document.body.classList.toggle('light-mode');
});