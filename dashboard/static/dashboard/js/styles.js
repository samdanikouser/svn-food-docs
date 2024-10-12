// Get all elements with the class 'dropdown-btn'
let dropdown = document.getElementsByClassName("dropdown-btn");

for (let i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function () {
        // Toggle between hiding and showing the dropdown content
        let dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === "block") {
            dropdownContent.style.display = "none";
        } else {
            dropdownContent.style.display = "block";
        }
    });
}
