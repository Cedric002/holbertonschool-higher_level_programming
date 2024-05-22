const redHeaderButton = document.getElementById("red_header");
const headerElement = document.querySelector("h1");

if (redHeaderButton && headerElement) {
  redHeaderButton.addEventListener("click", () => {
    headerElement.style.color = "#FF0000";
  });
}
