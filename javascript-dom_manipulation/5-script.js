const header = document.querySelector("header");
const updateHeader = document.getElementById("update_header");

function updateHeaderText() {
  header.textContent = "New Header!!!";
}

updateHeader.addEventListener("click", updateHeaderText);
