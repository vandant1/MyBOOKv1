import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import base64
from pathlib import Path

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

# Custom Components
def render_lottie(url):
    animation = f'<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script><lottie-player src="{url}" background="transparent" speed="1" loop autoplay></lottie-player>'
    components.html(animation, height=300)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Navigation
def create_nav():
    st.markdown(
        """
        <nav class="navbar">
            <div class="logo">Portfolio</div>
            <div class="nav-items">
                <a href="#home" class="nav-link">Home</a>
                <a href="#skills" class="nav-link">Skills</a>
                <a href="#projects" class="nav-link">Projects</a>
                <a href="#contact" class="nav-link">Contact</a>
            </div>
        </nav>
        """,
        unsafe_allow_html=True
    )

# Hero Section
def hero_section():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(
            """
            <div class="hero-content">
                <h1>Hello, I'm<br>a Machine Learning Engineer!</h1>
                <p class="hero-text">I build scalable web applications and bring ideas to life through Data.</p>
                <div class="hero-buttons">
                    <a href="#contact" class="btn primary-btn">Get in Touch</a>
                    <a href="#projects" class="btn secondary-btn">View Projects</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        render_lottie("https://assets2.lottiefiles.com/packages/lf20_iorpbol0.json")

# Skills Section
def skills_section():
    st.markdown('<div class="section-title" id="skills">Skill-Set</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    skills_data = [
        {
            "icon": "github",
            "title": "Version Control",
            "description": "Proficient in Git and GitHub for version control and collaboration."
        },
        {
            "icon": "code",
            "title": "ML Models Development",
            "description": "Building scalable applications with modern technologies."
        },
        {
            "icon": "database",
            "title": "Database Design",
            "description": "Designing and implementing efficient database solutions."
        }
    ]
    
    for idx, skill in enumerate(skills_data):
        with [col1, col2, col3][idx]:
            st.markdown(
                f"""
                <div class="skill-card">
                    <i class="fas fa-{skill['icon']} skill-icon"></i>
                    <h3>{skill['title']}</h3>
                    <p>{skill['description']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# Projects Section
def projects_section():
    st.markdown('<div class="section-title" id="projects">Featured Projects</div>', unsafe_allow_html=True)
    
    projects_data = [
        {
            "title": "Trackitall",
            "description": "The Smart Inventory Management System, for the maintainenance store of 'Vaccum Interrupter' for ABB India Ltd",
            "image": "C:\\Users\\Hp\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-12-02 150657.png",
            "github": "https://github.com/vandant1/ABBMSM.git",
            "Recap": "https://github.com/vandant1/ABBMSM"
        },
        # Add more projects here
    ]
    
    for project in projects_data:
        with st.container():
            st.markdown(
                f"""
                <div class="project-card">
                    <img src="{project['image']}" alt="{project['title']}" class="project-image">
                    <div class="project-content">
                        <h3>{project['title']}</h3>
                        <p>{project['description']}</p>
                        <div class="project-links">
                            <a href="{project['github']}" target="_blank" class="btn github-btn">
                                <i class="fab fa-github"></i> View Code
                            </a>
                            <a href="{project['Recap']}" target="_blank" class="btn demo-btn">
                                <i class="fas fa-external-link-alt"></i> Live Demo
                            </a>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

# Contact Section
def contact_section():
    st.markdown('<div class="section-title" id="contact">Connect with me</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(
            """
            <div class="contact-info">
                <h3>Let's work together</h3>
                <p>Feel free to reach out for collaborations or just a friendly hello</p>
                <div class="social-links">
                    <a href="https://github.com/vandant1" target="_blank" class="social-icon">
                        <i class="fab fa-github"></i>
                    </a>
                    <a href="https://www.linkedin.com/in/mr-vandan/" target="_blank" class="social-icon">
                        <i class="fab fa-linkedin"></i>
                    </a>
                    <a href="taradevandan@gmail.com" class="social-icon">
                        <i class="fas fa-envelope"></i>
                    </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        with st.form("contact_form"):
            st.text_input("Name")
            st.text_input("Email")
            st.text_area("Message")
            st.form_submit_button("Send Message")

def main():
    create_nav()
    hero_section()
    skills_section()
    projects_section()
    contact_section()

if __name__ == "__main__":
    main()

