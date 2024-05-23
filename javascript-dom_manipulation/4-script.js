const addItem = document.getElementById("add_item");
const myList = document.querySelector(".my_list");

function addListItem() {
  const newItem = document.createElement("li");
  newItem.textContent = "Item";

  myList.appendChild(newItem);
}

addItem.addEventListener("click", addListItem);
