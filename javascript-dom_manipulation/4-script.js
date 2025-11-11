const button = document.querySelector('#add_item');
button.addEventListener('click', function () {
  const list = document.querySelector('ul.my_list');
  const liElm = document.createElement('li');
  liElm.innerText = 'Item';
  list.appendChild(liElm);
});
