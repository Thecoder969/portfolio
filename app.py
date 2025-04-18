import streamlit as st
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="Ayush Dutta | Portfolio", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.image("Mee.jpg", width=200)  # Update with your image file name
    st.markdown("## Ayush Dutta")
    st.markdown("**📞** 8100312383")
    st.markdown("**📧** ayush.dutta24-26@bibs.co.in")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/ayush-dutta-9020b6323)")
    st.markdown("[💻 GitHub](https://github.com/Thecoder969)")
    st.download_button("📄 Download Resume", data=open("Ayush_Resume.pdf", "rb"), file_name="Ayush_Resume.pdf")

# --- Custom CSS ---
st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    h2 { color: #4CAF50; }
    .tab-content { animation: fadein 1.5s ease-in; }
    @keyframes fadein {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0px); }
    }
    </style>
""", unsafe_allow_html=True)

# --- Tabs ---
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["🏁 Summary", "🎓 Education", "💼 Experience", "🛠 Skills", "📊 Projects", "📜 Certifications", "🎯 Extras"])

# --- Summary ---
with tab1:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    st.subheader("Career Summary")
    st.write("""
        Enthusiastic and analytical Business Analytics & Data Science student with hands-on experience in data visualization, Excel modeling,
        Power BI dashboards, and business consulting case studies. Passionate about turning data into actionable insights and driving decision-making
        processes through analytics.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Education ---
with tab2:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    st.subheader("Education")
    st.write("""
    - **PGP + MBA in Business Analytics & Data Science**, Bengal Institute of Business Studies, 08/2024 - Present (76%)
    - **BBA**, NSHM Knowledge Campus, Kolkata, 05/2020 - 06/2023 (70%)
    - **CBSE**, Doon Public School, Roorkee, 04/2018 - 04/2020 (56%)
    - **ICSE**, Vivekananda Mission School, Kolkata, 04/2018 (77%)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Experience ---
with tab3:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    st.subheader("Experience")
    st.write("""
    - **Customer Support Executive (Tier 2)**, Amazon (06/2023 – 01/2024)
        - Delivered efficient customer service as part of the Tier 2 team.
        - Managed escalations and provided solutions in a WFH environment.
        - Selected through campus placement at NSHM.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Skills ---
with tab4:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    st.subheader("Skills")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Programming:** Python, MySQL")
        st.markdown("**Tools:** Excel, Power BI, Tableau")
    with col2:
        st.markdown("**Concepts:** Data Analysis, Business Analytics, Visualization")
        st.markdown("**Soft Skills:** Communication, Teamwork, Critical Thinking")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Projects ---
with tab5:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    st.subheader("Projects")
    st.markdown("""
    - **Amazon Sales Dashboard in Power BI**
        - Visualized key sales metrics, top-performing products, regional trends
        - [🔗 View Project](https://1drv.ms/u/c/2ee6a32193a742ff/EcDPcF9TvLpFj5QRmLH8nWgB_p3m4mSzm252aiGIhvoOXg)

    - **World Happiness Excel Dashboard**
        - Used Power Query, Pivot, and DAX to analyze sustainability and happiness
        - [🔗 View Project](https://1drv.ms/x/c/2ee6a32193a742ff/EV99wr2USc5Iu2LrbXG_ju8Bcv2Vpt_dmv_Wn5GV2hywTg)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Certifications ---
with tab6:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    st.subheader("Certifications & Achievements")
    st.write("""
    - **Machine Learning** – IIT Kanpur  
    - **AWS Cloud** – IBM  
    - **Python for Data Science** – IBM  
    - **Consulting** – BCG, PWC  
    - **Project Management** – Siemens  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Extras ---
with tab7:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    st.subheader("Hobbies & Personal Info")
    st.write("""
    - 💡 Creative Design
    - 🎵 Music Enthusiast
    - 📸 Photography
    - 🎮 Gaming
    - 🌱 Learning New Tech
    """)
    st.markdown('</div>', unsafe_allow_html=True)
