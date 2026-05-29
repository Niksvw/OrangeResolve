import streamlit as st

from rag_engine import search_similar_incidents
from utils import generate_resolution

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="OrangeResolve",
    page_icon="🟧",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

/* Main App */

.stApp {
    background-color: #FFFFFF;
}

/* Remove Streamlit Padding */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
}

/* Hero Section */

.hero-container {

    padding: 20px 0px 30px 0px;
}

/* Orange Accent */

.orange-line {

    width: 85px;

    height: 6px;

    background: linear-gradient(
        90deg,
        #FF6200,
        #FF8A3D
    );

    border-radius: 50px;

    margin-bottom: 22px;
}

/* Main Heading */

.main-title {

    font-size: 50px;

    font-weight: 800;

    margin-bottom: 8px;

    letter-spacing: -1px;
}

/* Orange Text */

.orange-text {

    color: #111111;
}

.resolve-text {

    color: #FF6200;
}

/* Subtitle */

.sub-title {

    color: #666666;

    font-size: 18px;

    font-weight: 400;

    margin-bottom: 18px;

    max-width: 700px;

    line-height: 1.7;
}

/* Feature Tags */

.feature-container {

    display: flex;

    gap: 12px;

    flex-wrap: wrap;

    margin-top: 18px;
}

.feature-tag {

    background-color: #FFF1E7;

    color: #FF6200;

    padding: 8px 16px;

    border-radius: 30px;

    font-size: 14px;

    font-weight: 600;

    border: 1px solid #FFD4B8;
}

/* Sidebar */

[data-testid="stSidebar"] {

    background-color: #FFF8F3;
}

/* Chat Input */

[data-testid="stChatInput"] {

    border: 2px solid #FF6200;

    border-radius: 14px;
}

/* Response Card */

.ai-box {

    background: white;

    padding: 28px;

    border-radius: 18px;

    border: 1px solid #FFE1CC;

    border-top: 5px solid #FF6200;

    color: #1F1F1F;

    font-size: 17px;

    line-height: 1.9;

    margin-top: 20px;

    box-shadow:
    0px 4px 20px rgba(0,0,0,0.05);
}

/* Section Header */

.section-header {

    color: #111111;

    font-size: 24px;

    font-weight: 700;

    margin-top: 20px;

    margin-bottom: 5px;
}

/* Footer */

.footer {

    text-align: center;

    margin-top: 60px;

    color: #999999;

    font-size: 13px;
}

/* Spinner */

.stSpinner > div {

    border-top-color: #FF6200 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

st.markdown("""
<div class="hero-container">

<div class="orange-line"></div>

<div class="main-title">
<span class="orange-text">Orange</span><span class="resolve-text">Resolve</span>
</div>

<div class="sub-title">
Enterprise-grade incident intelligence platform designed to help DevOps and Platform teams reduce MTTR using semantic search, historical incident analysis, and intelligent resolution recommendations.
</div>

<div class="feature-container">

<div class="feature-tag">Semantic Search</div>

<div class="feature-tag">RAG Architecture</div>

<div class="feature-tag">Groq LLM</div>

<div class="feature-tag">FAISS Vector Search</div>

<div class="feature-tag">Incident Intelligence</div>

</div>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.header("📌 Platform Overview")

    st.write("""
OrangeResolve helps Platform and DevOps teams resolve incidents faster using semantic search and historical incident intelligence.
""")

    st.markdown("---")

    st.write("""
### Core Capabilities

- Intelligent Incident Analysis
- Historical Incident Correlation
- Natural-Language Recommendations
- Faster Root Cause Identification
- Enterprise RAG Architecture
""")

# ---------------------------------------------------
# USER INPUT
# ---------------------------------------------------

query = st.chat_input(
    "Describe your production incident..."
)

# ---------------------------------------------------
# MAIN LOGIC
# ---------------------------------------------------

if query:

    # User Query
    with st.chat_message("user"):

        st.write(query)

    # AI Processing
    with st.spinner(
        "Analyzing historical incidents and generating intelligent recommendation..."
    ):

        results = search_similar_incidents(
            query
        )

        ai_response = generate_resolution(
            query,
            results
        )

    # ---------------------------------------------------
    # RESPONSE SECTION
    # ---------------------------------------------------

    st.markdown("""
<div class="section-header">
🟧 Resolution Recommendation
</div>
""", unsafe_allow_html=True)

    # Format Response
    formatted_response = ai_response.replace(
        "\n",
        "<br>"
    )

    # Response Card
    st.markdown(
        f"""
<div class="ai-box">
{formatted_response}
</div>
""",
        unsafe_allow_html=True
    )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
OrangeResolve • Smart Incident Resolution Platform
</div>
""", unsafe_allow_html=True)
