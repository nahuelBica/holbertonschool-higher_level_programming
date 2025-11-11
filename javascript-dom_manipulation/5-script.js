const button = document.querySelector('#update_header');
button.addEventListener('click', function () {
  const header = document.querySelector('header');
  header.innerText = 'New Header!!!';
});
