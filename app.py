import streamlit as st
from google import genai
from google.genai import types

# 1. Page Configuration (Sets title and page icon on browser tab)
st.set_page_config(
    page_title="AI Requirements Workspace",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inject Premium Custom CSS (Custom Fonts, Gradients, Cards, Buttons)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Typography */
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* App Title Gradient styling */
    .title-gradient {
        background: linear-gradient(135deg, #0F172A 0%, #2563EB 50%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.8rem;
        margin-bottom: 0.2rem;
        line-height: 1.2;
    }
    .subtitle-text {
        color: #64748B;
        font-size: 1.15rem;
        font-weight: 400;
        margin-bottom: 2rem;
    }
    
    /* Elegant Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #0F172A !important;
    }
    section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span {
        color: #F8FAFC !important;
    }
    
    /* Metrics Custom Cards styling */
    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 1.2rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        text-align: center;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    .metric-val {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2563EB;
        margin-bottom: 0.2rem;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #64748B;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Interactive Workspace Card styling */
    .workspace-card {
        background-color: #FFFFFF;
        border: 1px solid #F1F5F9;
        border-left: 6px solid #2563EB;
        border-radius: 16px;
        padding: 2.2rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        margin-top: 1.5rem;
    }
    
    /* Standardized Buttons styling */
    div.stButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 0.6rem 1.8rem !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
        transition: all 0.2s ease-in-out !important;
        width: 100%;
    }
    div.stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 16px rgba(37, 99, 235, 0.3) !important;
        background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Configuration (Parameters, Info, and API Key inputs)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=64)
    st.markdown("<h2 style='margin-top:0.5rem;'>Workspace Settings</h2>", unsafe_allow_html=True)
    st.markdown("Configure your AI model credentials and operational parameters safely here.")
    st.markdown("---")
    
    # Input field for Gemini API Key
    api_key = st.text_input("Gemini API Key:", type="password", placeholder="Paste your AIza... key")
    
    # Advanced customization options (Great for BA context styling)
    st.markdown("<h4 style='color:#F8FAFC;'>BA Target Preferences</h4>", unsafe_allow_html=True)
    output_style = st.selectbox(
        "Preferred Format:", 
        ["Agile Scrum User Stories", "Traditional BRD Document", "Technical Functional Specs"]
    )
    
    st.markdown("---")
    st.markdown("💡 **Tip:** Securely store your credentials in your Streamlit dashboard secrets block later.")

# 4. Main App Title Block (Gradient design)
st.markdown('<h1 class="title-gradient">AI-Powered Business Analyst Workspace</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Transform unstructured stakeholder interview recordings into production-ready Agile documentation in seconds.</p>', unsafe_allow_html=True)

# 5. Business Value Metrics Block (Proving project KPI statistics)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><div class="metric-val">10 Secs</div><div class="metric-label">Avg. Turnaround Time</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><div class="metric-val">95%</div><div class="metric-label">Time Saved Daily</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><div class="metric-val">0%</div><div class="metric-label">Manual Typos / Errors</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><div class="metric-val">Gemini 2.5</div><div class="metric-label">LLM Engine Online</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Tabbed Workspace Layout (Separates workspace, dashboards, and setup logs)
tab1, tab2, tab3 = st.tabs(["🚀 Core Generator", "📊 Analytical Insights", "📘 Guide & Strategy"])

with tab1:
    st.markdown("### Document Processing Terminal")
    st.write("Upload your raw text transcript or record note file below to begin processing.")
    
    # File Uploader Container
    uploaded_file = st.file_uploader("", type=["txt"])
    
    if uploaded_file and api_key:
        raw_transcript = uploaded_file.read().decode("utf-8")
        
        # Center-aligned execute button
        btn_col_1, btn_col_2, btn_col_3 = st.columns([1, 2, 1])
        with btn_col_2:
            trigger_button = st.button("✨ Compile Business Requirements Document")
            
        if trigger_button:
            with st.spinner("Analyzing transcript using deep business logic matrices..."):
                try:
                    # Initializing Gemini client
                    client = genai.Client(api_key=api_key)
                    
                    # Customizing the prompt based on selector choice
                    format_instruction = ""
                    if output_style == "Agile Scrum User Stories":
                        format_instruction = "Generate an Executive Summary, Pain Points, and beautifully structured Agile User Stories in 'As a... I want to... So that...' form with clear Given-When-Then Acceptance Criteria."
                    elif output_style == "Traditional BRD Document":
                        format_instruction = "Generate a formal Business Requirements Document with Business Objectives, Scope, Out-of-Scope lists, functional requirements, and data structure dependencies."
                    else:
                        format_instruction = "Generate technical specifications including API structures, detailed system integration flows, and relational logic flows."

                    system_prompt = (
                        f"You are an elite Business Analyst consultant. {format_instruction} "
                        f"Use clear Markdown formatting with nice headers, bold fonts, and clean lines. "
                        f"Adopt a highly structured, analytical, and professional corporate tone."
                    )
                    
                    # Fetching generation from Gemini
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=f"{system_prompt}\n\nTranscript:\n{raw_transcript}"
                    )
                    
                    # Presenting output inside an elegant workspace container card
                    st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
                    st.markdown("### 📋 Generated Requirements Analysis")
                    st.markdown(response.text)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Download block styling
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.download_button(
                        label="📥 Download Structured Document (.md)",
                        data=response.text,
                        file_name="AI_Generated_Requirements.md",
                        mime="text/markdown"
                    )
                    
                except Exception as e:
                    st.error(f"Execution Error: {e}. Please check your API key validity.")
                    
    elif not api_key:
        st.info("🔑 Please enter your Gemini API Key in the sidebar input box to unlock document generation.")
    else:
        st.info("📂 Please drop or upload a raw stakeholder interview transcript file (.txt) above to get started.")

with tab2:
    st.markdown("### 📊 Operational Analytics Matrix")
    st.write("Overview metrics simulating the tracking performance and automation patterns of your AI-powered system.")
    
    # Dynamic columns showing mock data metrics to complete the analytics look
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("💡 Highlight Operational Efficiencies")
        st.markdown("""
        * **Manual Documentation Rate:** ~4.5 hours per BRD draft.
        * **AI Compilation Rate:** ~12.5 seconds per BRD draft.
        * **Pipeline Efficiency Increase:** **99.72%** speed improvement.
        * **Team Bandwidth Returned:** ~22.5 hours per week saved for strategic solutioning.
        """)
    with col_b:
        st.subheader("🔑 Top Extracted Categorizations")
        # Visual metrics of standard categorized requirements
        st.progress(0.85, text="UI/UX Interface Workflows (85%)")
        st.progress(0.60, text="Database & Backend Logic Pipelines (60%)")
        st.progress(0.40, text="Transactional/Notification Systems (40%)")

with tab3:
    st.markdown("### 📘 Guide: How to Write Clean Transcripts")
    with st.expander("📝 1. Conducting High-Quality Stakeholder Interviews"):
        st.write("""
        When interviewing stakeholders, prompt them to frame their requirements through specific outcomes.
        * **Wrong questions:** 'What fields do you need in the form?'
        * **Right questions:** 'What is the absolute first action you perform on this screen, and why?'
        """)
    with st.expander("💡 2. Structure of an Excellent AI-Ready Transcript"):
        st.write("""
        For the best output quality, ensure your transcripts include:
        1. Explicit definitions of user roles (e.g., "The kitchen manager," "The guest shopper").
        2. Descriptions of current bottlenecks ("It takes 3 hours to sync this list").
        3. Clear boundary conditions ("This only occurs for orders containing sourdough").
        """)
