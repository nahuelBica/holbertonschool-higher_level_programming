const button = document.querySelector('#toggle_header');
button.addEventListener('click', function () {
  const header = document.querySelector('header');
  header.classList.toggle('red');
  header.classList.toggle('green');
});
