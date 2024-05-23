const listMovies = document.getElementById("list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => response.json())
  .then((data) => {
    data.results.forEach((movie) => {
      const listItem = document.createElement("li");
      listItem.textContent = movie.title;
      listMovies.appendChild(listItem);
    });
  })
  .catch((error) => {
    console.error("Error:", error);
  });
