const redHeaderButton = document.getElementById("red_header");
const headerElement = document.querySelector("div");

if (redHeaderButton && headerElement) {
  redHeaderButton.addEventListener("click", () => {
    headerElement.classList.add("red");
  });
}
