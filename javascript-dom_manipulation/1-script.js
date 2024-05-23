const redHeaderButton = document.getElementById("red_header");
const headerElement = document.querySelector("header");

if (redHeaderButton && headerElement) {
  redHeaderButton.addEventListener("click", () => {
    headerElement.style.color = "#FF0000";
  });
}
