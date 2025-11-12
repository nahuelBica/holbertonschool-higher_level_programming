fetchMovies();

async function fetchMovies () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  const listMovies = document.querySelector('ul#list_movies');

  try {
    const r = await fetch(url);
    if (!r.ok) {
      throw new Error(r.status);
    }
    const movieData = await r.json();
    movieData.results.forEach(movie => {
        const newMovie = document.createElement('li');
        newMovie.textContent = movie.title;
        listMovies.appendChild(newMovie);
    });
  } catch (e) {
    console.log('Error: ', e);
  }
}
