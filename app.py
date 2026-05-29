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
    background-color: white;
}

/* Main Title */

.main-title {
    color: #FF6200;
    font-size: 50px;
    font-weight: bold;
    margin-bottom: 5px;
}

/* Subtitle */

.sub-title {
    color: #555555;
    font-size: 20px;
    margin-bottom: 30px;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background-color: #FFF4EC;
}

/* AI Response Box */

.ai-box {

    background-color: #FFF3E8;

    padding: 25px;

    border-radius: 14px;

    border-left: 7px solid #FF6200;

    color: black;

    font-size: 17px;

    line-height: 1.8;

    margin-top: 15px;
}

/* Chat Input */

[data-testid="stChatInput"] {

    border: 2px solid #FF6200;

    border-radius: 12px;
}

/* Footer */

.footer {

    text-align: center;

    margin-top: 50px;

    color: gray;

    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    """
    <div class="main-title">
    🟧 OrangeResolve
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
    Smart Incident Resolution Platform
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.header("📌 About")

    st.write("""
OrangeResolve helps platform and DevOps teams reduce MTTR using semantic incident intelligence and historical incident analysis.

✅ Semantic Search

✅ RAG Architecture

✅ Intelligent Recommendations

✅ Historical Incident Intelligence

✅ Faster Root Cause Analysis
""")

# ---------------------------------------------------
# USER INPUT
# ---------------------------------------------------

query = st.chat_input(
    "Describe your incident..."
)

# ---------------------------------------------------
# MAIN LOGIC
# ---------------------------------------------------

if query:

    # User Message
    with st.chat_message("user"):

        st.write(query)

    # AI Processing
    with st.spinner(
        "Analyzing historical incidents and generating recommendation..."
    ):

        results = search_similar_incidents(
            query
        )

        ai_response = generate_resolution(
            query,
            results
        )

    # ---------------------------------------------------
    # AI RESPONSE
    # ---------------------------------------------------

    st.subheader(
        "🟧 Resolution Recommendation"
    )

    # Format Response
    formatted_response = ai_response.replace(
        "\n",
        "<br>"
    )

    # Display Response
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

st.markdown(
    """
<div class="footer">
OrangeResolve • Smart Incident Resolution Platform
</div>
""",
    unsafe_allow_html=True
)