// Function to open the task form modal
function openTaskForm() {
  document.getElementById("task-modal").style.display = "flex"; // Set to flex when opening
}

// Function to close the task form modal
function closeTaskForm() {
  document.getElementById("task-modal").style.display = "none";
}

// Optional: Close the modal when clicking outside of it
window.onclick = function(event) {
  const modal = document.getElementById("task-modal");
  if (event.target == modal) {
      closeTaskForm();
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("menu-toggle");
  const navbar = document.querySelector(".sidebar");

  menuToggle.addEventListener("change", () => {
    navbar.classList.toggle("active");
  });
});