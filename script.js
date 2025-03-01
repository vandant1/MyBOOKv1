// This file will be loaded via the load_js function in app.py

// Import ScrollReveal and Typed.js
// Assuming these are included via CDN or a separate script
// If not, you'll need to include them appropriately.  For example:
// <script src="https://unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js"></script>
// <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>

document.addEventListener("DOMContentLoaded", () => {
    // Initialize ScrollReveal
    const sr = ScrollReveal({
      origin: "bottom",
      distance: "60px",
      duration: 1000,
      delay: 200,
      reset: false,
    })
  
    sr.reveal(".skill-card", { interval: 100 })
    sr.reveal(".project-card", { interval: 200 })
    sr.reveal(".contact-info", { delay: 300 })
    sr.reveal(".about-content", { delay: 300 })
  
    // Initialize Typed.js
    if (document.querySelector(".typing-text")) {
      new Typed(".typing-text", {
        strings: ["Machine Learning Engineer", "AI Developer", "Data Scientist", "Problem Solver"],
        typeSpeed: 80,
        backSpeed: 40,
        backDelay: 1500,
        loop: true,
      })
    }
  
    // Tab functionality
    const tabButtons = document.querySelectorAll(".tab-btn")
    const tabContents = document.querySelectorAll(".tab-content")
  
    tabButtons.forEach((button) => {
      button.addEventListener("click", () => {
        // Remove active class from all buttons and contents
        tabButtons.forEach((btn) => btn.classList.remove("active"))
        tabContents.forEach((content) => content.classList.remove("active"))
  
        // Add active class to clicked button
        button.classList.add("active")
  
        // Show corresponding content
        const tabId = button.getAttribute("data-tab")
        document.getElementById(tabId).classList.add("active")
      })
    })
  
    // Project filter
    const filterButtons = document.querySelectorAll(".filter-btn")
    const projectCards = document.querySelectorAll(".project-card")
  
    filterButtons.forEach((button) => {
      button.addEventListener("click", () => {
        // Remove active class from all buttons
        filterButtons.forEach((btn) => btn.classList.remove("active"))
  
        // Add active class to clicked button
        button.classList.add("active")
  
        const filter = button.getAttribute("data-filter")
  
        projectCards.forEach((card) => {
          if (filter === "all") {
            card.style.display = "flex"
          } else if (card.getAttribute("data-category") === filter) {
            card.style.display = "flex"
          } else {
            card.style.display = "none"
          }
        })
      })
    })
  
    // Back to top button
    const backToTopButton = document.querySelector(".back-to-top")
  
    window.addEventListener("scroll", () => {
      if (window.pageYOffset > 300) {
        backToTopButton.classList.add("visible")
      } else {
        backToTopButton.classList.remove("visible")
      }
  
      // Add scrolled class to navbar
      const navbar = document.querySelector(".navbar")
      if (window.pageYOffset > 50) {
        navbar.classList.add("scrolled")
      } else {
        navbar.classList.remove("scrolled")
      }
    })
  
    // Mobile menu toggle
    const menuToggle = document.querySelector(".menu-toggle")
    const navItems = document.querySelector(".nav-items")
  
    if (menuToggle) {
      menuToggle.addEventListener("click", () => {
        navItems.classList.toggle("active")
        menuToggle.classList.toggle("active")
      })
    }
  
    // Close mobile menu when clicking outside
    document.addEventListener("click", (e) => {
      if (navItems.classList.contains("active") && !navItems.contains(e.target) && !menuToggle.contains(e.target)) {
        navItems.classList.remove("active")
        menuToggle.classList.remove("active")
      }
    })
  
    // Theme switcher
    const themeToggle = document.querySelector(".theme-toggle")
    if (themeToggle) {
      themeToggle.addEventListener("click", () => {
        document.body.classList.toggle("light-mode")
        const isDark = !document.body.classList.contains("light-mode")
        localStorage.setItem("dark-mode", isDark)
      })
  
      // Check for saved theme preference
      const savedTheme = localStorage.getItem("dark-mode")
      if (savedTheme === "false") {
        document.body.classList.add("light-mode")
      }
    }
  
    // Smooth scrolling for navigation
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
        e.preventDefault()
  
        // Close mobile menu if open
        if (navItems.classList.contains("active")) {
          navItems.classList.remove("active")
          menuToggle.classList.remove("active")
        }
  
        const targetId = this.getAttribute("href")
        const targetElement = document.querySelector(targetId)
  
        if (targetElement) {
          window.scrollTo({
            top: targetElement.offsetTop - 80,
            behavior: "smooth",
          })
        }
      })
    })
  
    // Skills progress animation
    const skillBars = document.querySelectorAll(".skill-progress-bar")
  
    const animateSkills = () => {
      skillBars.forEach((bar) => {
        const percentage = bar.getAttribute("data-percentage")
        bar.style.width = percentage
      })
    }
  
    // Trigger skill animation when in viewport
    const skillsSection = document.querySelector("#skills")
    if (skillsSection) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animateSkills()
            observer.unobserve(entry.target)
          }
        })
      })
  
      observer.observe(skillsSection)
    }
  
    // Form submission
    const contactForm = document.querySelector(".contact-form")
    if (contactForm) {
      contactForm.addEventListener("submit", (e) => {
        e.preventDefault()
  
        // Get form data
        const name = document.getElementById("name").value
        const email = document.getElementById("email").value
        const subject = document.getElementById("subject").value
        const message = document.getElementById("message").value
  
        // Validate form
        if (!name || !email || !subject || !message) {
          alert("Please fill in all fields")
          return
        }
  
        // Here you would typically send the form data to a server
        // For now, just show a success message
        alert("Message sent successfully!")
        contactForm.reset()
      })
    }
  })
  
  