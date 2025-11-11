fetchChar();

async function fetchChar () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  const charElm = document.querySelector('#character');

  try {
    const r = await fetch(url);
    if (!r.ok) {
      throw new Error(r.status);
    }
    const charData = await r.json();
    charElm.textContent = charData.name;
  } catch (e) {
    console.log('Error: ', e);
  }
}
