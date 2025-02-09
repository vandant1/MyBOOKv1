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

def render_lottie(url):
    lottie_html = f"""
    <script src="https://unpkg.com/@dotlottie/player-component@2.7.12/dist/dotlottie-player.mjs" type="module"></script>
    <dotlottie-player src="{url}" background="transparent" speed="1" style="width: 300px; height: 300px" loop autoplay></dotlottie-player>
    """
    components.html(lottie_html, height=350)

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
                <p class="hero-text">I am a passionate Machine Learning & AI Developer focused on creating scalable solutions that drive innovation. With expertise in deep learning, computer vision, NLP, and predictive analytics, I turn raw data into actionable insights. I work across industries like healthcare, fintech, and industrial automation to solve real-world challenges with precision and creativity.</p>
                <div class="hero-buttons">
                    <a href="#contact" class="btn primary-btn">Get in Touch</a>
                    <a href="#projects" class="btn secondary-btn">View Projects</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        render_lottie("https://lottie.host/e3061e9c-1d25-4378-a237-d0410520e91e/vNtYDa3wzV.lottie")


# Skills Section
def skills_section():
    st.markdown('<div class="section-title" id="skills">Skill-Set</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    skills_data = [
        {
            "icon": "github",
            "title": "Version Control",
            "description": "Proficient in Git and GitHub for version control and collaboration."
        },
        {
            "icon": "code",
            "title": "Web Development",
            "description": "Building scalable applications with modern technologies."
        },
        {
            "icon": "database",
            "title": "Database Design",
            "description": "Designing and implementing efficient database solutions."
        },
        {
            "icon": "brain",
            "title": "AI/ML",
            "description":"Developing the robust and high accuracy Machine learning Models."
        },
        {
            "icon": "chart-line",
            "title": "Data Science",
            "description": "Feature Engineering in Datasets and extracting insights from data."

        }
    ]
    
    for idx, skill in enumerate(skills_data):
        with [col1, col2, col3, col4, col5][idx]:
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
        {    "title": "Disease Breakout Diagnosis",
            "description": "Predicting Disease Outbreaks Using Machine Learning!",
            "image": "C:\\2k25\\MyBooKv1\\images\\Screenshot 2025-02-09 131757.png",
            "github": "https://github.com/vandant1/Disease-Breakout-Diagnosis",
            "Web": "https://disease-diagnosis-at-finger-tip.streamlit.app/"
        },

        {
            "title": "Trackitall",
            "description": "The Smart Inventory Management System, for the maintenance store of 'Vacuum Interrupter' for ABB India Ltd",
            "image": "C:\\2k25\\MyBooKv1\\images\\TrackItAll Home page.png",
            "github": "https://github.com/vandant1/ABBMSM.git",
            "Web": "https://github.com/vandant1/ABBMSM"
        },

        {
            "title": "Data-Cleaning and Visualization",
            "description": "Data Cleaning and Visualization Tool 📊 A Streamlit-based app for uploading CSV files, cleaning data, and creating visualizations. Features include real-time previews, scatter plots, and histograms. Built with Pandas, Seaborn, and Matplotlib, its perfect for quick insights and interactive data exploration.",
            "image": "C:\\2k25\\MyBooKv1\\images\\Screenshot 2025-02-09 153504.png",
            "github": "https://github.com/vandant1/Data-Cleaning-and-visualization-tool",
            "Web": "https://data-cleaning-and-visualization-tool.streamlit.app/"
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
                            <a href="{project['Web']}" target="_blank" class="btn demo-btn">
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

# Personal Details Section
def personal_details_section():
    st.markdown('<div class="section-title" id="about">About Me</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://github.com/vandant1/MyBOOKv1/blob/main/images/Vandan%20ABB1.jpg", width=250, use_container_width=True)


    with col2:
        st.markdown(
            """
            <div class="about-content">
                <h2>Vandan Tarade</h2>
                <p class="about-text">
                    I'm a passionate Machine Learning Engineer with expertise in deep learning, data science, and software development.
                    My goal is to build intelligent solutions that solve real-world problems efficiently.
                </p>
                <ul class="about-list">
                    <li><strong>📍 Location:</strong> Maharashtra, India</li>
                    <li><strong>🎓 Education:</strong> B.E in Electronics and Telecommunication</li>
                    <li><strong>💼 Experience:</strong> AI & ML Internship at TechSaksham</li>
                    <li><strong>📧 Email:</strong> taradevandan@gmail.com</li>
                    <li><strong>🔗 LinkedIn:</strong> <a href="https://www.linkedin.com/in/mr-vandan/" target="_blank">LinkedIn Profile</a></li>
                    <li><strong>🌐 Portfolio:</strong> <a href="https://mybook.streamlit.app/" target="_blank">My Portfolio</a></li>
                </ul>
            </div>
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

if __name__ == "__main__":
    main()

