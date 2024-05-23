const header = document.querySelector("header");
const toggleHeader = document.getElementById("toggle_header");

function toggleHeaderClass() {
  if (header.classList.contains("red")) {
    header.classList.remove("red");
    header.classList.add("green");
  } else {
    header.classList.remove("green");
    header.classList.add("red");
  }
}

toggleHeader.addEventListener("click", toggleHeaderClass);
