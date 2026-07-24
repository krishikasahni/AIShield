const status = document.getElementById("status");
const scanned = document.getElementById("scanned");
const spam = document.getElementById("spam");
const toggleButton = document.getElementById("toggle");

toggleButton.addEventListener("click", () => {
    if (status.textContent === "Active") {
        status.textContent = "Disabled";
        toggleButton.textContent = "Enable Protection";
    } else {
        status.textContent = "Active";
        toggleButton.textContent = "Disable Protection";
    }
});