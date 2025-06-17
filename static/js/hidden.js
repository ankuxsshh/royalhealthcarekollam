function toggleSpecialties() {
    const more = document.getElementById("more-specialties");
    const btn = document.getElementById("toggle-specialties");

    if (more.style.display === "none") {
        more.style.display = "block";
        btn.textContent = "Show Less";
    } else {
        more.style.display = "none";
        btn.textContent = "Show More";
    }
}
