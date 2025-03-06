// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });
  
  // Form submission handling
  document.getElementById('contact-form').addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Thank you for reaching out! I will get back to you soon.');
    this.reset();
  });

// adding modern tech feature to hero section
  const textArray = ["Python & Django Developer", "Full-Stack Web Enthusiast", "ML Enthusiast"];
  let textIndex = 0;
  let charIndex = 0;
  const typingSpeed = 100;
  const erasingSpeed = 50;
  const delayBetweenTexts = 1500;
  const typedTextElement = document.getElementById("typed-text");

  function typeText() {
      if (charIndex < textArray[textIndex].length) {
          typedTextElement.textContent += textArray[textIndex].charAt(charIndex);
          charIndex++;
          setTimeout(typeText, typingSpeed);
      } else {
          setTimeout(eraseText, delayBetweenTexts);
      }
  }

  function eraseText() {
      if (charIndex > 0) {
          typedTextElement.textContent = textArray[textIndex].substring(0, charIndex - 1);
          charIndex--;
          setTimeout(eraseText, erasingSpeed);
      } else {
          textIndex = (textIndex + 1) % textArray.length;
          setTimeout(typeText, typingSpeed);
      }
  }

  document.addEventListener("DOMContentLoaded", () => {
      setTimeout(typeText, typingSpeed);
  });

  function toggleMenu() {
    document.querySelector(".nav-links").classList.toggle("show");
}

// Add sticky navbar effect on scroll
window.addEventListener("scroll", function () {
    const navbar = document.querySelector(".navbar");
    if (window.scrollY > 50) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});