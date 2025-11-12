document.addEventListener('DOMContentLoaded', () => fetchHello());

async function fetchHello () {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const helloElm = document.querySelector('#hello');
  try {
    const r = await fetch(url);
    if (!r.ok) {
      throw new Error(r.status);
    }
    const data = await r.json();
    helloElm.textContent = data.hello;
  } catch (e) {
    console.log('Error: ', e);
  }
}
