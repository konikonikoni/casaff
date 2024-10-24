var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;

    // Toggle display between "none" and "block" if screen width is above 1600px,
    // and between "none" and "flex" if it's below 1600px
    if (window.innerWidth > 1600) {
      if (panel.style.display === "block") {
        panel.style.display = "none";
      } else {
        panel.style.display = "block";
      }
    } else {
      if (panel.style.display === "flex") {
        panel.style.display = "none";
      } else {
        panel.style.display = "flex";
      }
    }
  });
}
