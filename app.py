import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie


# --- LOAD ASSETS ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Lottie animations
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_zrqthn6o.json")

# Profile image
profile_pic = Image.open("Mee.jpg")  # Replace with your actual image path

# Resume PDF
with open("Ayush_Resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- SIDEBAR ---
with st.sidebar:
    st.image(profile_pic, width=200)
    st.title("Ayush Dutta")
    st.write("📞 8100312383")
    st.write("📧 ayush.dutta24-26@bibs.co.in")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/ayush-dutta-9020b6323)")
    st.markdown("[GitHub](https://github.com/Thecoder969)")
    st.download_button(label="📄 Download Resume",
                       data=PDFbyte,
                       file_name="Ayush_Dutta_Resume.pdf",
                       mime="application/pdf")

# --- HEADER ---
st.title("Welcome to My Portfolio! 👋")
st_lottie(lottie_coding, height=300, key="coding")

# --- TABS ---
tabs = st.tabs(["Summary", "Education", "Experience", "Skills", "Projects", "Certifications", "Hobbies"])

with tabs[0]:
    st.subheader("Summary")
    st.write("""
I am Ayush Dutta, a passionate and detail-oriented Business Analytics and Data Science student with a strong foundation in data visualization, analysis, and storytelling. Equipped with hands-on experience in tools like Power BI, Excel, Python, and MySQL, I have worked on real-world projects that derive actionable insights from complex data. I am committed to continuous learning and have earned certifications from reputed institutions like IIT Kanpur, IBM, and BCG. My goal is to help organizations make data-driven decisions that create real business impact.
    """)

with tabs[1]:
    st.subheader("Education")
    st.write("""
    - **PGP + MBA (Business Analytics & Data Science)**, BIBS Kolkata (2024 - Present) — 76%
    - **BBA**, NSHM Knowledge Campus, Kolkata (2020 - 2023) — 70%
    - **CBSE (XII)**, Doon Public School, Roorkee (2020) — 56%
    - **ICSE (X)**, Vivekananda Mission School, Kolkata — 77%
    """)

with tabs[2]:
    st.subheader("Experience")
    st.write("""
    - **Customer Service Executive, Amazon** (June 2023 - Jan 2024)  
      Handled tier-2 customer support remotely, a placement opportunity via NSHM.
    """)

with tabs[3]:
    st.subheader("Skills")
    st.write("""
    - **Languages**: Python, MySQL  
    - **Tools**: Power BI, Tableau, Excel, PowerPoint  
    - **Domains**: Data Analysis, Visualization, Business Analytics
    """)

with tabs[4]:
    st.subheader("Projects")
    st.markdown("""
    - 🔹 **Amazon Sales Dashboard (Power BI)**  
      [Project Link](https://www.linkedin.com/in/ayush-dutta-9020b6323?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)  
      Interactive dashboard with sales trends, top products, regional performance & drilldowns.

    - 🔹 **World Happiness Report (Excel)**  
      [Project Link](https://1drv.ms/x/c/2ee6a32193a742ff/EV99wr2USc5Iu2LrbXG_ju8Bcv2Vpt_dmv_Wn5GV2hywTg)  
      Dashboard analyzing happiness vs. sustainability with Power Query, DAX, and Pivot.
    """)

with tabs[5]:
    st.subheader("Certifications & Achievements")
    st.write("""
    - 📜 Machine Learning - IIT Kanpur  
    - ☁️ AWS - IBM  
    - 💼 BCG Consulting  
    - 🧠 PWC Management Consulting  
    - 🐍 Python - IBM  
    - 🏗️ Siemens Project Management
    """)

with tabs[6]:
    st.subheader("Hobbies & Interests")
    st.write("""
    - 🎧 Music Enthusiast  
    - 📸 Photography  
    - 📊 Dashboard Designing  
    - 🎮 Gaming
    """)

# --- FOOTER ---
st.markdown("---")
st.markdown("Made using Streamlit")

