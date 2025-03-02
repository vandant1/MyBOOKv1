import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import base64
from pathlib import Path
import os

# Page Configuration
st.set_page_config(
    page_title="MyBOOK",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('style.css')

# Load JavaScript from external file
def load_js():
    with open('script.js') as f:
        js_content = f.read()
        
    js_with_libraries = """
    <script src="https://unpkg.com/scrollreveal@4.0.9/dist/scrollreveal.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
    <script>
    """ + js_content + """
    </script>
    """
    components.html(js_with_libraries, height=0)

# Function to check if image exists
def image_exists(image_path):
    return os.path.isfile(image_path)

def render_lottie(url, height=350):
    lottie_html = f"""
    <script src="https://unpkg.com/@dotlottie/player-component@2.7.12/dist/dotlottie-player.mjs" type="module"></script>
    <dotlottie-player src="{url}" background="transparent" speed="1" style="width: 100%; height: {height}px" loop autoplay></dotlottie-player>
    """
    components.html(lottie_html, height=height)

# Navigation
def create_nav():
    st.markdown(
        """
        <nav class="navbar">
            <div class="logo">
                <span class="logo-text">Portfolio</span>
                <span class="logo-dot"></span>
            </div>
            <div class="menu-toggle">
                <span></span>
                <span></span>
                <span></span>
            </div>
            <div class="nav-items">
                <a href="#home" class="nav-link">Home</a>
                <a href="#about" class="nav-link">About</a>
                <a href="#skills" class="nav-link">Skills</a>
                <a href="#projects" class="nav-link">Projects</a>
                <a href="#contact" class="nav-link">Contact</a>
                <button class="theme-toggle">
                    <i class="fas fa-moon"></i>
                    <i class="fas fa-sun"></i>
                </button>
            </div>
        </nav>
        """,
        unsafe_allow_html=True
    )

# Hero Section
def hero_section():
    st.markdown('<div id="home"></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(
            """
            <div class="hero-content">
                <div class="hero-badge">Welcome to my Portfolio</div>
                <h1>Hello, I'm<br>a <span class="typing-text">Machine Learning Engineer!</span></h1>
                <p class="hero-text">I am a passionate Machine Learning & AI Developer focused on creating scalable solutions that drive innovation. With hands-on experience in deep learning, computer vision, NLP, and predictive analytics, I turn raw data into actionable insights.</p>
                <div class="hero-buttons">
                    <a href="#contact" class="btn primary-btn">
                        <span>Get in Touch</span>
                        <i class="fas fa-arrow-right"></i>
                    </a>
                    <a href="#projects" class="btn secondary-btn">
                        <span>View Projects</span>
                        <i class="fas fa-eye"></i>
                    </a>
                </div>
                <div class="hero-stats">
                    <div class="stat-item">
                        <span class="stat-number">10+</span>
                        <span class="stat-label">Projects</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-number">0.5+</span>
                        <span class="stat-label">Years Experience</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-number">5+</span>
                        <span class="stat-label">Technologies</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        render_lottie("https://lottie.host/e3061e9c-1d25-4378-a237-d0410520e91e/vNtYDa3wzV.lottie", height=400)

# Personal Details Section
# Update your personal_details_section function with this code
def personal_details_section():
    st.markdown('<div id="about" class="section-anchor"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        # Image handling with base64 encoding
        def img_to_base64(image_path):
            try:
                with open(image_path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode()
                return f"data:image/png;base64,{encoded_string}"
            except Exception as e:
                st.error(f"Error loading image: {str(e)}")
                return ""
        
        # Use relative path and check both extensions
        image_path = None
        if image_exists("images/Vandan ABB1.png"):
            image_path = "images/Vandan ABB1.png"
        elif image_exists("images/Vandan ABB1.jpg"):
            image_path = "images/Vandan ABB1.jpg"
        
        profile_img = img_to_base64(image_path) if image_path else ""
        
        st.markdown(
            f"""
            <div class="profile-card">
                <div class="profile-img-container">
                    <img src="{profile_img}" alt="Profile" class="profile-img">
                    <div class="profile-overlay"></div>
                </div>
                <div class="profile-social">
                    <!-- Keep social links unchanged -->
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="about-content">
                <h2>My Journey</h2>
                <p class="about-text">
                    I'm a passionate Machine Learning Engineer with hands-on experience in deep learning, data science, and software development.
                    My goal is to build intelligent solutions that solve real-world problems efficiently.
                </p>
                <div class="about-tabs">
                    <div class="tab-buttons">
                        <button class="tab-btn active" data-tab="experience">Experience</button>
                        <button class="tab-btn" data-tab="education">Education</button>
                        <button class="tab-btn" data-tab="interests">Interests</button>
                    </div>
                    <div class="tab-content active" id="experience">
                        <div class="timeline">
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <div class="timeline-date">2024 - 2025</div>
                                <div class="timeline-content">
                                    <h3>Internship at ABB India Ltd.</h3>
                                    <p>Working on cutting-edge Inventory Management solutions for real-world problems.</p>
                                </div>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <div class="timeline-date">2023 - 2024</div>
                                <div class="timeline-content">
                                    <h3>Projects of Personal Interest</h3>
                                    <p>Analyzed large datasets and built predictive models for business insights.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="tab-content" id="education">
                        <div class="timeline">
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <div class="timeline-date">2022 - 2026</div>
                                <div class="timeline-content">
                                    <h3>B.E. in Electronics and Telecommunication</h3>
                                    <p>Focused on Electronic Circuits, Power devices, control systems, machine learning, artificial intelligence, and data structures.</p>
                                </div>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <div class="timeline-date">2018 - 2019</div>
                                <div class="timeline-content">
                                    <h3>High School</h3>
                                    <p>Specialized in Mathematics and Computer Science.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="tab-content" id="interests">
                        <div class="interests-grid">
                            <div class="interest-item">
                                <i class="fas fa-robot"></i>
                                <span>Artificial Intelligence</span>
                            </div>
                            <div class="interest-item">
                                <i class="fas fa-brain"></i>
                                <span>Deep Learning</span>
                            </div>
                            <div class="interest-item">
                                <i class="fas fa-chart-line"></i>
                                <span>Data Visualization</span>
                            </div>
                            <div class="interest-item">
                                <i class="fas fa-code"></i>
                                <span>Programming</span>
                            </div>
                            <div class="interest-item">
                                <i class="fas fa-book"></i>
                                <span>Reading</span>
                            </div>
                            <div class="interest-item">
                                <i class="fas fa-hiking"></i>
                                <span>Hiking</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="about-cta">
                    <a href="#" class="btn primary-btn download-cv">
                        <i class="fas fa-download"></i>
                        <span>Download CV</span>
                    </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Skills Section
def skills_section():
    st.markdown('<div id="skills" class="section-anchor"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">My Expertise</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="section-subtitle">Skills & Technologies</div>
        <p class="section-description">
            I specialize in machine learning and data science, with expertise in various programming languages and frameworks.
            My technical skills enable me to build robust and scalable solutions for complex problems.
        </p>
        """,
        unsafe_allow_html=True
    )
    
    # Technical Skills with progress bars - Fixed with inline styles for immediate display
    st.markdown(
        """
        <div class="skills-container">
            <div class="skills-category">
                <h3 class="skills-category-title">Technical Skills</h3>
                <div class="skill-progress">
                    <div class="skill-info">
                        <span class="skill-name">Python</span>
                        <span class="skill-percentage">95%</span>
                    </div>
                    <div class="skill-progress-bg">
                        <div class="skill-progress-bar" data-percentage="95%" style="width: 95%"></div>
                    </div>
                </div>
                <div class="skill-progress">
                    <div class="skill-info">
                        <span class="skill-name">Machine Learning</span>
                        <span class="skill-percentage">90%</span>
                    </div>
                    <div class="skill-progress-bg">
                        <div class="skill-progress-bar" data-percentage="90%" style="width: 90%"></div>
                    </div>
                </div>
                <div class="skill-progress">
                    <div class="skill-info">
                        <span class="skill-name">Deep Learning</span>
                        <span class="skill-percentage">85%</span>
                    </div>
                    <div class="skill-progress-bg">
                        <div class="skill-progress-bar" data-percentage="85%" style="width: 85%"></div>
                    </div>
                </div>
                <div class="skill-progress">
                    <div class="skill-info">
                        <span class="skill-name">Data Analysis</span>
                        <span class="skill-percentage">92%</span>
                    </div>
                    <div class="skill-progress-bg">
                        <div class="skill-progress-bar" data-percentage="92%" style="width: 92%"></div>
                    </div>
                </div>
                <div class="skill-progress">
                    <div class="skill-info">
                        <span class="skill-name">Web Development</span>
                        <span class="skill-percentage">80%</span>
                    </div>
                    <div class="skill-progress-bg">
                        <div class="skill-progress-bar" data-percentage="80%" style="width: 80%"></div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Skill cards
    st.markdown('<div class="skills-grid">', unsafe_allow_html=True)
    
    skills_data = [
        {
            "icon": "brain",
            "title": "Machine Learning",
            "description": "Building predictive models and algorithms that learn from data."
        },
        {
            "icon": "network-wired",  # Changed from chart-network which might not exist in Font Awesome
            "title": "Deep Learning",
            "description": "Creating neural networks for complex pattern recognition tasks."
        },
        {
            "icon": "database",
            "title": "Data Engineering",
            "description": "Designing and implementing efficient database solutions and data pipelines."
        },
        {
            "icon": "chart-line",
            "title": "Data Science",
            "description": "Extracting insights from data through statistical analysis and visualization."
        },
        {
            "icon": "code",
            "title": "Web Development",
            "description": "Building scalable web applications with modern technologies."
        },
        {
            "icon": "github",
            "title": "Version Control",
            "description": "Proficient in Git and GitHub for version control and collaboration."
        },
        {
            "icon": "cloud",
            "title": "Cloud Computing",
            "description": "Deploying and managing applications on cloud platforms."
        },
        {
            "icon": "robot",
            "title": "AI Applications",
            "description": "Developing practical AI solutions for real-world problems."
        }
    ]
    
    for skill in skills_data:
        st.markdown(
            f"""
            <div class="skill-card">
                <div class="skill-icon-container">
                    <i class="fas fa-{skill['icon']} skill-icon"></i>
                </div>
                <h3>{skill['title']}</h3>
                <p>{skill['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Technologies
    st.markdown(
        """
        <div class="tech-stack">
            <h3 class="tech-stack-title">Technologies I Work With</h3>
            <div class="tech-icons">
                <div class="tech-icon">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python">
                    <span>Python</span>
                </div>
                <div class="tech-icon">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" alt="TensorFlow">
                    <span>TensorFlow</span>
                </div>
                <div class="tech-icon">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg" alt="PyTorch">
                    <span>PyTorch</span>
                </div>
                <div class="tech-icon">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" alt="Pandas">
                    <span>Pandas</span>
                </div>
                <div class="tech-icon">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" alt="NumPy">
                    <span>NumPy</span>
                </div>
                <div class="tech-icon">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript">
                    <span>JavaScript</span>
                </div>
                <div class="tech-icon">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML5">
                    <span>HTML5</span>
                </div>
                <div class="tech-icon">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS3">
                    <span>CSS3</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def projects_section():
    st.markdown('<div id="projects" class="section-anchor"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Featured Projects</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="section-subtitle">Innovative Solutions Showcase</div>
        <p class="section-description">
            Explore my cutting-edge projects that demonstrate expertise in AI/ML development, 
            data engineering, and full-stack solutions. Each project includes technical details 
            and live demonstrations.
        </p>
        
        <div class="project-filters">
            <button class="filter-btn active" data-filter="all">All</button>
            <button class="filter-btn" data-filter="ml">AI/ML</button>
            <button class="filter-btn" data-filter="data">Data Science</button>
            <button class="filter-btn" data-filter="web">Web Dev</button>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    projects_data = [
        {    
            "title": "Disease Breakout Diagnosis",
            "description": "AI-powered epidemiological prediction system using Streamlit, pandas and numpy",
            "image": "images/disease_diagnosis.png",
            "github": "https://github.com/vandant1/Disease-Breakout-Diagnosis",
            "web": "https://disease-diagnosis.streamlit.app/",
            "category": "ml",
            "tech": ["Python", "Numpy", "Streamlit", "Pandas"]
        },
        {
            "title": "Smart Inventory Manager",
            "description": "Enterprise-grade inventory system with real-time analytics dashboard",
            "image": "images/inventory_system.png",
            "github": "https://github.com/vandant1/ABBMSM",
            "web": "https://inventory-tracker.streamlit.app/",
            "category": "web",
            "tech": ["Flask", "HTML & CSS", "MySQL", "Aiven clouds"]
        },
        {
            "title": "Data Visualization Suite",
            "description": "Interactive data analysis toolkit with automated cleaning pipelines",
            "image": "images/data_visualization.png",
            "github": "https://github.com/vandant1/Data-Cleaning-Tool",
            "web": "https://data-visualization.streamlit.app/",
            "category": "data",
            "tech": ["Python", "Plotly", "Pandas", "Spark"]
        }
    ]
    
    for project in projects_data:
        # Enhanced image handling with caching
        @st.cache_data
        def load_image_base64(image_path):
            try:
                if image_exists(image_path):
                    with open(image_path, "rb") as img_file:
                        return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
                return "https://via.placeholder.com/800x450.png?text=Image+Not+Found&theme=dark"
            except Exception as e:
                st.error(f"Image load error: {str(e)}")
                return ""
        
        image_base64 = load_image_base64(project["image"])
        
        st.markdown(
            f"""
            <div class="project-card" data-category="{project['category']}">
                <div class="project-image-container">
                    <img src="{image_base64}" alt="{project['title']}" class="project-image">
                    <div class="project-overlay">
                        <div class="project-links">
                            <a href="{project['github']}" target="_blank" class="project-link" aria-label="GitHub Repository">
                                <i class="fab fa-github"></i>
                            </a>
                            <a href="{project['web']}" target="_blank" class="project-link" aria-label="Live Demo">
                                <i class="fas fa-external-link-alt"></i>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="project-content">
                    <h3 class="project-title">{project['title']}</h3>
                    <p class="project-description">{project['description']}</p>
                    <div class="project-tech">
                        {"".join([f'<span class="tech-pill">{tech}</span>' for tech in project["tech"]])}
                    </div>
                    <div class="project-actions">
                        <a href="{project['github']}" target="_blank" class="project-btn code-btn">
                            <i class="fas fa-code"></i>
                            <span>View Source</span>
                        </a>
                        <a href="{project['web']}" target="_blank" class="project-btn demo-btn">
                            <i class="fas fa-rocket"></i>
                            <span>Live Demo</span>
                        </a>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Project statistics
    st.markdown(
        """
        <div class="project-stats">
            <div class="stat-card">
                <div class="stat-icon">
                    <i class="fas fa-code-branch"></i>
                </div>
                <div class="stat-number">10+</div>
                <div class="stat-title">Projects Completed</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">
                    <i class="fas fa-users"></i>
                </div>
                <div class="stat-number">5+</div>
                <div class="stat-title">Happy Clients</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">
                    <i class="fas fa-clock"></i>
                </div>
                <div class="stat-number">1000+</div>
                <div class="stat-title">Hours Coded</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">
                    <i class="fas fa-coffee"></i>
                </div>
                <div class="stat-number">500+</div>
                <div class="stat-title">Cups of Coffee</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Contact Section
def contact_section():
    st.markdown('<div id="contact" class="section-anchor"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Get In Touch</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="section-subtitle">Contact Me</div>
        <p class="section-description">
            Feel free to reach out for collaborations, job opportunities, or just a friendly chat.
            I'm always open to discussing new projects and ideas.
        </p>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(
            """
            <div class="contact-info">
                <div class="contact-card">
                    <div class="contact-card-icon">
                        <i class="fas fa-map-marker-alt"></i>
                    </div>
                    <div class="contact-card-content">
                        <h3>Location</h3>
                        <p>Nashik,Maharashtra,India</p>
                    </div>
                </div>
                <div class="contact-card">
                    <div class="contact-card-icon">
                        <i class="fas fa-envelope"></i>
                    </div>
                    <div class="contact-card-content">
                        <h3>Email</h3>
                        <p>taradevandan@gmail.com</p>
                    </div>
                </div>
                <div class="contact-card">
                    <div class="contact-card-icon">
                        <i class="fas fa-phone"></i>
                    </div>
                    <div class="contact-card-content">
                        <h3>Phone</h3>
                        <p>+91 9529747095</p>
                    </div>
                </div>
                <div class="social-links-container">
                    <h3>Connect With Me</h3>
                    <div class="social-links">
                        <a href="https://github.com/vandant1" target="_blank" class="social-icon">
                            <i class="fab fa-github"></i>
                        </a>
                        <a href="https://www.linkedin.com/in/mr-vandan/" target="_blank" class="social-icon">
                            <i class="fab fa-linkedin"></i>
                        </a>
                        <a href="mailto:taradevandan@gmail.com" class="social-icon">
                            <i class="fas fa-envelope"></i>
                        </a>
                        <a href="#" class="social-icon">
                            <i class="fab fa-twitter"></i>
                        </a>
                        <a href="#" class="social-icon">
                            <i class="fab fa-instagram"></i>
                        </a>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="contact-form-container">
                <form class="contact-form" id="contact-form">
                    <h3>Send Me a Message</h3>
                    <p>I'll get back to you as soon as possible.</p>
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" id="name" placeholder="Your Name" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" id="email" placeholder="Your Email" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label for="subject">Subject</label>
                        <input type="text" id="subject" placeholder="Subject" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label for="message">Message</label>
                        <textarea id="message" rows="5" placeholder="Your Message" class="form-control" required></textarea>
                    </div>
                    <button type="submit" class="btn primary-btn submit-btn">
                        <span>Send Message</span>
                        <i class="fas fa-paper-plane"></i>
                    </button>
                </form>
            </div>
            """,
            unsafe_allow_html=True
        )

# Footer Section
def footer_section():
    st.markdown(
        """
        <footer class="footer">
            <div class="footer-content">
                <div class="footer-logo">
                    <span class="logo-text">Portfolio</span>
                    <span class="logo-dot"></span>
                </div>
                <p class="footer-text">Building intelligent solutions for a smarter future.</p>
                <div class="footer-social">
                    <a href="https://github.com/vandant1" target="_blank" class="footer-social-icon">
                        <i class="fab fa-github"></i>
                    </a>
                    <a href="https://www.linkedin.com/in/mr-vandan/" target="_blank" class="footer-social-icon">
                        <i class="fab fa-linkedin"></i>
                    </a>
                    <a href="mailto:taradevandan@gmail.com" class="footer-social-icon">
                        <i class="fas fa-envelope"></i>
                    </a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 My Portfolio. All rights reserved.</p>
                <div class="footer-links">
                    <a href="#home">Home</a>
                    <a href="#about">About</a>
                    <a href="#skills">Skills</a>
                    <a href="#projects">Projects</a>
                    <a href="#contact">Contact</a>
                </div>
            </div>
        </footer>
        """,
        unsafe_allow_html=True
    )

# Back to top button
def back_to_top_button():
    st.markdown(
        """
        <a href="#home" class="back-to-top">
            <i class="fas fa-arrow-up"></i>
        </a>
        """,
        unsafe_allow_html=True
    )

def main():
    create_nav()
    hero_section()
    personal_details_section()
    skills_section()
    projects_section()
    contact_section()
    footer_section()
    back_to_top_button()
    load_js()

if __name__ == "__main__":
    main()

