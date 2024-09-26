let slideIndex = 0;
showSlides(); // Initialize the slideshow

function showSlides() {
    const slides = document.getElementsByClassName("slide");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; // Hide all slides
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1} // Loop back to first slide
    slides[slideIndex - 1].style.display = "block"; // Show the current slide

    // Trigger confetti effect
    showConfetti();

    setTimeout(showSlides, 2500); // Change slide every 5 seconds
}

function plusSlides(n) {
    const slides = document.getElementsByClassName("slide");
    slideIndex += n;
    if (slideIndex > slides.length) {slideIndex = 1} // Loop back to first slide
    if (slideIndex < 1) {slideIndex = slides.length} // Loop back to last slide
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; // Hide all slides
    }
    slides[slideIndex - 1].style.display = "block"; // Show the current slide

    // Trigger confetti effect
    showConfetti();
}

function showConfetti() {
    console.log("Confetti triggered"); // Debugging line
    confetti({
        particleCount: 100,
        spread: 500,
        origin: { y: 0.6 }, // Start the confetti from the top
        gravity: 0.5, // Makes confetti fall slower
        scalar: 1.2,
        colors: ['#a2c2e0', '#f4c2c2', '#c2a2e0'] // Optional: Customize colors
    });
}


