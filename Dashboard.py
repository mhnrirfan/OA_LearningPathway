import streamlit as st

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="OA AI Capability Journey",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================================
# DATA
# ============================================================================

TRACKS = {
    "fundamentals": {
        "icon": "🏆",
        "name": "Fundamentals",
        "color": "#2f6fed",
        "bg": "#eaf1ff",
        "description": "Build a strong foundation in AI, LLMs, prompting, data and responsible AI.",
        "courses": [
            ("AI & LLM Fundamentals", "Understand how large language models work and their core capabilities.", "1.5 hrs"),
            ("Prompt Engineering", "Learn to write clear, effective prompts for consistent AI outputs.", "2 hrs"),
            ("Responsible AI", "Core principles for safe, fair and transparent AI use.", "1 hr"),
            ("Governance Basics", "Understand the policies and guardrails that govern AI use at OA.", "1 hr"),
            ("AI Landscape Overview", "A tour of today's leading models, vendors and tools.", "1.5 hrs"),
            ("Data Literacy for AI", "Learn how data quality and structure impact AI outcomes.", "1.5 hrs"),
            ("Understanding Neural Networks", "A plain-English look at how neural networks learn.", "2 hrs"),
            ("AI Ethics & Bias", "Recognise and mitigate bias in AI-driven decisions.", "1.5 hrs"),
        ],
    },

    "agentic": {
        "icon": "🕸️",
        "name": "Agentic AI",
        "color": "#2f9e5c",
        "bg": "#e9f8ee",
        "description": "Build, orchestrate and scale AI agents that can reason and act.",
        "courses": [
            ("MCP & Tool Abstraction", "Connect models to tools and data using the Model Context Protocol.", "2 hrs"),
            ("Copilot Studio", "Build and deploy custom copilots without writing code.", "2.5 hrs"),
            ("Agent Frameworks", "Compare popular frameworks for building autonomous agents.", "2 hrs"),
            ("LangGraph", "Design stateful, multi-step agent workflows with LangGraph.", "3 hrs"),
            ("Multi-Agent Systems", "Orchestrate teams of agents that collaborate on tasks.", "3 hrs"),
            ("Autonomous Task Orchestration", "Manage long-running, autonomous agent workflows safely.", "2.5 hrs"),
        ],
    },

    "rag_data": {
        "icon": "💠",
        "name": "RAG & Data",
        "color": "#8b5cf6",
        "bg": "#f2edfe",
        "description": "Work with enterprise data, retrieval, embeddings and AI memory.",
        "courses": [
            ("Azure AI Search", "Index and retrieve enterprise content with Azure AI Search.", "2 hrs"),
            ("Vector Databases", "Understand embeddings and vector search for retrieval.", "2 hrs"),
            ("Redis (Memory Cache)", "Use Redis for fast agent memory and caching.", "1.5 hrs"),
            ("LangChain", "Build retrieval-augmented pipelines using LangChain.", "2.5 hrs"),
            ("Embedding Strategies", "Choose the right embedding model and chunking strategy.", "1.5 hrs"),
        ],
    },

    "llm_promptops": {
        "icon": "💡",
        "name": "LLM & Prompt Ops",
        "color": "#e8781f",
        "bg": "#fef1e6",
        "description": "Master models, prompts, multimodal AI and AI-assisted development.",
        "courses": [
            ("Work with GPT-4/4.1/5", "Get the most out of OpenAI's latest model family.", "1.5 hrs"),
            ("Claude 3.x & Gemini", "Compare and apply Claude and Gemini for common tasks.", "1.5 hrs"),
            ("Multi-Modal AI", "Work with text, image and audio inputs together.", "2 hrs"),
            ("GitHub Copilot", "Accelerate coding with AI pair programming.", "1.5 hrs"),
            ("Prompt Flow", "Build, test and evaluate prompt pipelines visually.", "2 hrs"),
            ("Prompt Versioning & Evaluation", "Track prompt changes and measure output quality over time.", "1.5 hrs"),
        ],
    },

    "governance": {
        "icon": "🛡️",
        "name": "Governance & Responsible AI",
        "color": "#e0373f",
        "bg": "#fdecec",
        "description": "Deploy AI safely with governance, monitoring, security and compliance.",
        "courses": [
            ("Security & Guardrails", "Put technical guardrails around AI systems in production.", "2 hrs"),
            ("Auditing & Monitoring", "Track AI decisions and outputs for accountability.", "1.5 hrs"),
            ("Compliance", "Navigate regulatory requirements for enterprise AI.", "1.5 hrs"),
            ("Decision Guardrails", "Design approval and escalation paths for high-stakes AI decisions.", "1 hr"),
        ],
    },

    "simulation": {
        "icon": "🚀",
        "name": "Simulation & Innovation",
        "color": "#12163a",
        "bg": "#eceef5",
        "description": "Explore emerging AI capabilities through simulation and experimentation.",
        "courses": [
            ("Synthetic Data Generation", "Generate realistic synthetic datasets for testing and training.", "2 hrs"),
            ("Digital Twins (Unreal Engine)", "Build simulated environments to test AI in the real world.", "3 hrs"),
            ("Mistral & Llama", "Explore open-weight model families and when to use them.", "1.5 hrs"),
            ("Simulation & Sandbox", "Safely trial new AI capabilities in a sandboxed environment.", "2 hrs"),
        ],
    },
}


STAGE_TO_TRACK = {
    "FOUNDATION": "fundamentals",
    "PRACTITIONER": "llm_promptops",
    "ADVANCED BUILDERS": "rag_data",
    "AGENTIC AI": "agentic",
    "ENTERPRISE DEPLOYMENT": "governance",
    "INNOVATION LAB": "simulation",
}


TOOLS = [
    ("🔷", "Azure AI Search", "https://learn.microsoft.com/en-us/azure/search/"),
    ("🟥", "Redis", "https://redis.io/docs/latest/"),
    ("⛓️", "LangChain", "https://python.langchain.com/docs/introduction/"),
    ("🔗", "LangGraph", "https://langchain-ai.github.io/langgraph/"),
    ("🧩", "Copilot Studio", "https://learn.microsoft.com/en-us/microsoft-copilot-studio/"),
    ("🐙", "GitHub Copilot", "https://docs.github.com/en/copilot"),
    ("🌐", "OpenAI", "https://platform.openai.com/docs"),
    ("✨", "Claude", "https://docs.claude.com/"),
    ("💎", "Gemini", "https://ai.google.dev/gemini-api/docs"),
    ("🦙", "Llama", "https://www.llama.com/docs/overview/"),
    ("🌪️", "Mistral", "https://docs.mistral.ai/"),
    ("🎨", "DALL-E", "https://platform.openai.com/docs/guides/images"),
    ("🔊", "Whisper", "https://platform.openai.com/docs/guides/speech-to-text"),
    ("🏛️", "Unreal Engine", "https://dev.epicgames.com/documentation/en-us/unreal-engine"),
    ("🌊", "Prompt Flow", "https://microsoft.github.io/promptflow/"),
    ("🦜", "LangSmith", "https://docs.smith.langchain.com/"),
]


# ============================================================================
# SESSION STATE
# ============================================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "feedback_sent" not in st.session_state:
    st.session_state.feedback_sent = False


def navigate(page):
    st.session_state.page = page


# ============================================================================
# CSS
# ============================================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

* {
    box-sizing: border-box;
}

.main {
    background: #f3f5f9;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {
    background: #131a3a;
}

section[data-testid="stSidebar"] * {
    color: #d7dbf0;
}

.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 4px 0 24px 0;
    font-weight: 800;
    font-size: 16px;
    color: white !important;
}

.sidebar-logo-icon {
    font-size: 25px;
}

.sidebar-section {
    font-size: 10px;
    font-weight: 800;
    color: #737cae !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin: 22px 0 8px 4px;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] button {
    width: 100%;
    background: transparent;
    color: #c7cbe6;
    border: none;
    text-align: left;
    font-size: 13px;
    font-weight: 500;
    padding: 9px 12px;
    min-height: 38px;
    border-radius: 8px;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] button:hover {
    background: #242d5d;
    color: white;
}

.sidebar-quote {
    background: #1c2450;
    border-radius: 10px;
    padding: 15px;
    margin-top: 22px;
    font-size: 12px;
    line-height: 1.55;
    color: #b8bde0 !important;
}

.sidebar-quote-author {
    margin-top: 10px;
    font-weight: 700;
    color: #7f8ad4 !important;
}

/* ================= HEADERS ================= */

.page-title {
    font-size: 29px;
    font-weight: 800;
    color: #101433;
    line-height: 1.3;
}

.page-subtitle {
    color: #6b7086;
    font-size: 14px;
    margin-top: 4px;
}

.page-header {
    margin-bottom: 28px;
}

.section-title {
    font-size: 18px;
    font-weight: 800;
    color: #12163a;
    margin: 22px 0 13px 0;
}

.page-section-title {
    font-size: 23px;
    font-weight: 800;
    color: #12163a;
    margin-bottom: 5px;
}

.page-section-subtitle {
    color: #6b7086;
    font-size: 13px;
    margin-bottom: 24px;
}

/* ================= BUTTONS ================= */

div[data-testid="stButton"] > button {
    border-radius: 8px;
    font-weight: 600;
    font-size: 13px;
    border: 1px solid #d7dae3;
    background: white;
    color: #2c3050;
    min-height: 40px;
}

div[data-testid="stButton"] > button:hover {
    border-color: #2f6fed;
    color: #2f6fed;
}

/* ================= CARDS ================= */

.white-card {
    background: white;
    border-radius: 14px;
    border: 1px solid #e7e9f2;
    padding: 20px;
}

.info-card {
    background: white;
    border-radius: 14px;
    border: 1px solid #e7e9f2;
    padding: 22px;
    min-height: 150px;
}

.card-title {
    font-size: 15px;
    font-weight: 800;
    color: #12163a;
    margin-bottom: 7px;
}

.card-description {
    font-size: 12.5px;
    color: #6b7086;
    line-height: 1.5;
}

/* ================= PATHWAYS ================= */

.pathway-card {
    border-radius: 13px;
    padding: 17px;
    min-height: 150px;
    border: 1px solid;
}

.pathway-icon {
    font-size: 25px;
    margin-bottom: 12px;
}

.pathway-title {
    font-size: 14px;
    font-weight: 800;
    line-height: 1.3;
}

.pathway-count {
    font-size: 11px;
    margin-top: 8px;
    color: #6b7086;
}

/* ================= JOURNEY ================= */

.journey-container {
    background: white;
    border-radius: 15px;
    border: 1px solid #e7e9f2;
    padding: 24px 18px;
}

.journey-card {
    min-height: 270px;
    text-align: center;
}

.journey-circle {
    width: 68px;
    height: 68px;
    border-radius: 50%;
    border: 3px solid;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 12px auto;
    background: white;
    font-size: 25px;
}

.journey-title {
    font-size: 11.5px;
    font-weight: 800;
    line-height: 1.3;
    min-height: 30px;
}

.journey-subtitle {
    color: #6b7086;
    font-size: 11px;
    margin: 5px 0 10px 0;
}

.journey-list {
    text-align: left;
    list-style: none;
    padding: 0;
    margin: 0;
}

.journey-list li {
    font-size: 11.5px;
    color: #454868;
    padding: 5px 0;
    border-bottom: 1px dashed #eef0f6;
}

.journey-list li::before {
    content: "• ";
}

/* ================= HOW YOU LEARN ================= */

.step-card {
    background: white;
    border-radius: 12px;
    border: 1px solid #e7e9f2;
    padding: 18px 10px;
    min-height: 125px;
    text-align: center;
}

.step-icon {
    font-size: 23px;
    margin-bottom: 8px;
}

.step-title {
    font-weight: 800;
    font-size: 12px;
    color: #12163a;
}

.step-description {
    color: #6b7086;
    font-size: 11px;
    margin-top: 5px;
    line-height: 1.4;
}

/* ================= TRACK PAGE ================= */

.track-hero {
    border-radius: 15px;
    padding: 26px;
    display: flex;
    align-items: center;
    gap: 17px;
    margin-bottom: 25px;
}

.track-hero-icon {
    width: 60px;
    height: 60px;
    border-radius: 15px;
    background: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
}

.track-hero-title {
    font-size: 25px;
    font-weight: 800;
    margin: 0;
}

.track-hero-description {
    font-size: 13px;
    margin-top: 5px;
    opacity: 0.8;
}

.course-card {
    background: white;
    border-radius: 12px;
    border: 1px solid #e7e9f2;
    padding: 17px;
    min-height: 190px;
}

.course-number {
    width: 28px;
    height: 28px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    font-weight: 800;
    margin-bottom: 10px;
}

.course-title {
    font-weight: 800;
    font-size: 14px;
    color: #12163a;
    line-height: 1.35;
}

.course-description {
    color: #5c6079;
    font-size: 12px;
    line-height: 1.45;
    margin-top: 6px;
}

.course-duration {
    color: #8b8fa8;
    font-size: 11px;
    font-weight: 700;
    margin-top: 14px;
}

/* ================= EVENT CARDS ================= */

.event-card {
    background: white;
    border: 1px solid #e7e9f2;
    border-radius: 13px;
    padding: 20px;
    min-height: 205px;
}

.event-date {
    color: #2f6fed;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.event-title {
    font-size: 15px;
    font-weight: 800;
    color: #12163a;
    line-height: 1.35;
}

.event-description {
    font-size: 12px;
    color: #6b7086;
    line-height: 1.5;
    margin-top: 8px;
}

/* ================= LAB CARDS ================= */

.lab-card {
    background: white;
    border-radius: 14px;
    border: 1px solid #e7e9f2;
    padding: 22px;
    min-height: 215px;
}

.lab-icon {
    font-size: 28px;
    margin-bottom: 15px;
}

.lab-title {
    font-size: 16px;
    font-weight: 800;
    color: #12163a;
}

.lab-description {
    color: #6b7086;
    font-size: 12.5px;
    line-height: 1.5;
    margin-top: 8px;
}

/* ================= BLOG ================= */

.article-card {
    background: white;
    border: 1px solid #e7e9f2;
    border-radius: 14px;
    padding: 21px;
    min-height: 235px;
}

.article-tag {
    display: inline-block;
    background: #eaf1ff;
    color: #2f6fed;
    border-radius: 20px;
    padding: 4px 9px;
    font-size: 10px;
    font-weight: 800;
    margin-bottom: 13px;
}

.article-title {
    font-size: 16px;
    font-weight: 800;
    color: #12163a;
    line-height: 1.35;
}

.article-description {
    font-size: 12px;
    color: #6b7086;
    line-height: 1.5;
    margin-top: 8px;
}

/* ================= TOOLS ================= */

a.tool-chip {
    display: flex;
    align-items: center;
    gap: 7px;
    background: #f7f8fb;
    border: 1px solid #edeef4;
    border-radius: 8px;
    padding: 9px;
    font-size: 11.5px;
    font-weight: 600;
    color: #23264a !important;
    margin-bottom: 8px;
    text-decoration: none;
}

a.tool-chip:hover {
    border-color: #2f6fed;
    background: #eaf1ff;
}

/* ================= FOOTER ================= */

.footer-banner {
    background: #eef1fb;
    border-radius: 12px;
    padding: 17px 20px;
    display: flex;
    align-items: center;
    gap: 14px;
    margin-top: 25px;
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-logo">
            <span class="sidebar-logo-icon">🔷</span>
            <span>OA AI Capability Journey</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sidebar-section">Navigate</div>', unsafe_allow_html=True)

    sidebar_items = [
        ("🏠", "Home", "home"),
        ("🗺️", "Capability Map", "capability_map"),
        ("🎯", "Learning Pathways", "pathways"),
        ("🧪", "Sandbox Labs", "labs"),
        ("🗓️", "Workshops & Events", "events"),
        ("📰", "Blog & Articles", "blog"),
        ("📅", "Teams Calendar", "calendar"),
    ]

    for icon, label, page in sidebar_items:
        if st.button(
            f"{icon}  {label}",
            key=f"sidebar_{page}",
            use_container_width=True,
        ):
            st.session_state.page = page
            st.rerun()

    st.markdown('<div class="sidebar-section">Support</div>', unsafe_allow_html=True)

    support_items = [
        ("❓", "Help & Support", "help"),
        ("💬", "Community", "community"),
        ("📝", "Feedback", "feedback"),
    ]

    for icon, label, page in support_items:
        if st.button(
            f"{icon}  {label}",
            key=f"sidebar_{page}",
            use_container_width=True,
        ):
            st.session_state.page = page
            st.rerun()

    st.markdown(
        """
        <div class="sidebar-quote">
            "We connect AI models to our foundational tools and semantics layers —
            enabling agents to read, reason and act across data and models."

            <div class="sidebar-quote-author">
                — OA AI Team
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================================
# SHARED HEADER
# ============================================================================

def render_header(title, subtitle):

    st.markdown(
        f"""
        <div class="page-header">
            <div class="page-title">{title}</div>
            <div class="page-subtitle">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def back_home():

    if st.button("← Back to Home", key=f"back_{st.session_state.page}"):
        st.session_state.page = "home"
        st.rerun()


# ============================================================================
# HOME PAGE
# ============================================================================

def render_home():

    render_header(
        "OA AI Capability Journey",
        "Learn. Build. Apply. Lead.",
    )

    # ------------------------------------------------------------------------
    # PATHWAYS
    # ------------------------------------------------------------------------

    st.markdown(
        '<div class="section-title">Choose your learning pathway</div>',
        unsafe_allow_html=True,
    )

    pathway_cols = st.columns(6)

    for col, (key, track) in zip(pathway_cols, TRACKS.items()):

        with col:

            st.markdown(
                f"""
                <div class="pathway-card"
                     style="background:{track['bg']};
                            border-color:{track['color']}55;">

                    <div class="pathway-icon">
                        {track['icon']}
                    </div>

                    <div class="pathway-title"
                         style="color:{track['color']};">
                        {track['name']}
                    </div>

                    <div class="pathway-count">
                        {len(track['courses'])} capabilities
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(
                "Explore pathway →",
                key=f"home_pathway_{key}",
                use_container_width=True,
            ):
                st.session_state.page = key
                st.rerun()

    # ------------------------------------------------------------------------
    # JOURNEY
    # ------------------------------------------------------------------------

    st.markdown(
        '<div class="section-title">Your AI Capability Journey</div>',
        unsafe_allow_html=True,
    )

    stages = [
        (
            "🌱",
            "FOUNDATION",
            "Build your basics",
            "#2f6fed",
            ["AI & LLM Fundamentals", "Prompt Engineering", "Responsible AI", "Governance Basics"],
        ),
        (
            "🛠️",
            "PRACTITIONER",
            "Apply & build",
            "#e8781f",
            ["Work with GPT-4/4.1/5", "Claude 3.x & Gemini", "Multi-Modal AI", "GitHub Copilot"],
        ),
        (
            "🧩",
            "ADVANCED BUILDERS",
            "Design & integrate",
            "#8b5cf6",
            ["Azure AI Search", "Vector Databases", "Redis (Memory Cache)", "LangChain"],
        ),
        (
            "🕸️",
            "AGENTIC AI",
            "Orchestrate & scale",
            "#2f9e5c",
            ["MCP & Tool Abstraction", "Copilot Studio", "Agent Frameworks", "LangGraph"],
        ),
        (
            "🛡️",
            "ENTERPRISE DEPLOYMENT",
            "Secure & govern",
            "#e0373f",
            ["Security & Guardrails", "Auditing & Monitoring", "Compliance", "Decision Guardrails"],
        ),
        (
            "🚀",
            "INNOVATION LAB",
            "Simulate & explore",
            "#12163a",
            ["Synthetic Data Generation", "Digital Twins", "Mistral & Llama", "Simulation & Sandbox"],
        ),
    ]

    st.markdown(
        '<div class="journey-container">',
        unsafe_allow_html=True,
    )

    journey_cols = st.columns(6)

    for col, (icon, title, subtitle, color, items) in zip(journey_cols, stages):

        with col:

            st.markdown(
                f"""
                <div class="journey-card">

                    <div class="journey-circle"
                         style="border-color:{color};
                                color:{color};">

                        {icon}

                    </div>

                    <div class="journey-title"
                         style="color:{color};">

                        {title}

                    </div>

                    <div class="journey-subtitle">
                        {subtitle}
                    </div>

                    <ul class="journey-list">

                        {''.join(f"<li>{item}</li>" for item in items)}

                    </ul>

                </div>
                """,
                unsafe_allow_html=True,
            )

            track_key = STAGE_TO_TRACK[title]

            if st.button(
                "View pathway →",
                key=f"journey_{track_key}",
                use_container_width=True,
            ):
                st.session_state.page = track_key
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------------
    # HOW YOU LEARN
    # ------------------------------------------------------------------------

    st.markdown(
        '<div class="section-title">How you learn</div>',
        unsafe_allow_html=True,
    )

    steps = [
        ("📖", "1. LEARN", "Self-paced content"),
        ("👥", "2. WORKSHOP", "Instructor-led learning"),
        ("🧪", "3. SANDBOX", "Guided hands-on practice"),
        ("⚙️", "4. BUILD", "Mini project or use case"),
        ("📊", "5. SHOWCASE", "Demo to the community"),
    ]

    step_cols = st.columns(5)

    for col, (icon, title, description) in zip(step_cols, steps):

        with col:

            st.markdown(
                f"""
                <div class="step-card">

                    <div class="step-icon">
                        {icon}
                    </div>

                    <div class="step-title">
                        {title}
                    </div>

                    <div class="step-description">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

    # ------------------------------------------------------------------------
    # TOOLS
    # ------------------------------------------------------------------------

    st.markdown(
        '<div class="section-title">Tools We Work With</div>',
        unsafe_allow_html=True,
    )

    tool_cols = st.columns(4)

    for i, (icon, name, url) in enumerate(TOOLS):

        with tool_cols[i % 4]:

            st.markdown(
                f"""
                <a class="tool-chip"
                   href="{url}"
                   target="_blank">

                    {icon} {name}
                    <span style="margin-left:auto;">↗</span>

                </a>
                """,
                unsafe_allow_html=True,
            )

    # ------------------------------------------------------------------------
    # FOOTER
    # ------------------------------------------------------------------------

    st.markdown(
        """
        <div class="footer-banner">

            <div style="font-size:25px;">
                🌱
            </div>

            <div>

                <strong>
                    New to AI?
                </strong>

                <div style="color:#6b7086; font-size:12px; margin-top:3px;">
                    Start with the Fundamentals pathway and build your capabilities step by step.
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================================
# CAPABILITY MAP
# ============================================================================

def render_capability_map():

    render_header(
        "Capability Map",
        "Explore the full AI capability landscape across OA.",
    )

    st.markdown(
        """
        <div class="white-card">

            <div class="card-title">
                How the capability map works
            </div>

            <div class="card-description">
                The map is organised into six capability areas. You can explore
                each area individually and follow the progression from foundational
                knowledge to advanced AI implementation and innovation.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Capability areas</div>',
        unsafe_allow_html=True,
    )

    cols = st.columns(3)

    for i, (key, track) in enumerate(TRACKS.items()):

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="info-card"
                     style="border-top:4px solid {track['color']};">

                    <div style="font-size:28px;">
                        {track['icon']}
                    </div>

                    <div class="card-title"
                         style="margin-top:10px;">

                        {track['name']}

                    </div>

                    <div class="card-description">

                        {track['description']}

                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(
                "Explore capabilities →",
                key=f"map_{key}",
                use_container_width=True,
            ):
                st.session_state.page = key
                st.rerun()


# ============================================================================
# LEARNING PATHWAYS
# ============================================================================

def render_pathways():

    render_header(
        "Learning Pathways",
        "Choose the pathway that best matches your current AI goals.",
    )

    cols = st.columns(3)

    for i, (key, track) in enumerate(TRACKS.items()):

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="info-card"
                     style="border-top:4px solid {track['color']};">

                    <div style="font-size:28px;">
                        {track['icon']}
                    </div>

                    <div class="card-title">
                        {track['name']}
                    </div>

                    <div class="card-description">
                        {track['description']}
                    </div>

                    <div style="font-size:11px; color:#8b8fa8; margin-top:12px;">
                        {len(track['courses'])} capabilities
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(
                "View pathway →",
                key=f"pathway_{key}",
                use_container_width=True,
            ):
                st.session_state.page = key
                st.rerun()


# ============================================================================
# SANDBOX LABS
# ============================================================================

def render_labs():

    render_header(
        "Sandbox Labs",
        "Practise AI capabilities through guided, hands-on experimentation.",
    )

    labs = [
        ("🧠", "RAG Lab", "Build a company knowledge assistant using enterprise content and retrieval.", "Beginner → Intermediate"),
        ("🤖", "Agent Builder Lab", "Create your first AI agent and connect it to tools and workflows.", "Intermediate"),
        ("🧪", "Prompt Evaluation Lab", "Test, evaluate and improve prompts using structured experiments.", "Beginner → Intermediate"),
        ("📊", "Synthetic Data Lab", "Generate realistic synthetic data for AI and analytics use cases.", "Intermediate"),
        ("🕸️", "Multi-Agent Lab", "Experiment with multiple agents collaborating on a complex task.", "Advanced"),
        ("🛡️", "Responsible AI Lab", "Explore guardrails, monitoring and safe AI deployment patterns.", "Intermediate"),
    ]

    cols = st.columns(3)

    for i, (icon, title, description, level) in enumerate(labs):

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="lab-card">

                    <div class="lab-icon">
                        {icon}
                    </div>

                    <div class="lab-title">
                        {title}
                    </div>

                    <div class="lab-description">
                        {description}
                    </div>

                    <div style="font-size:11px; color:#8b8fa8; margin-top:14px;">
                        {level}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.button(
                "Open lab →",
                key=f"lab_{i}",
                use_container_width=True,
            )


# ============================================================================
# EVENTS
# ============================================================================

def render_events():

    render_header(
        "Workshops & Events",
        "Learn together through workshops, talks, demos and community sessions.",
    )

    events = [
        ("22 May 2025", "Intro to Prompt Engineering for Consultants", "Learn how to create better prompts for day-to-day consulting work.", "Beginner"),
        ("29 May 2025", "Building with RAG on Azure AI Search", "Build a retrieval-augmented knowledge assistant using enterprise content.", "Practitioner"),
        ("5 June 2025", "Multi-Agent Orchestration with LangGraph", "Explore how multiple AI agents can collaborate to complete complex tasks.", "Advanced"),
        ("12 June 2025", "Responsible AI in Practice", "Understand how to apply governance and responsible AI principles to real projects.", "All levels"),
        ("19 June 2025", "AI Showcase: What Are Teams Building?", "See practical AI use cases being developed across OA.", "Community"),
        ("26 June 2025", "AI Tools Open Clinic", "Bring your AI questions and get practical support from the AI community.", "Open session"),
    ]

    cols = st.columns(3)

    for i, (date, title, description, level) in enumerate(events):

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="event-card">

                    <div class="event-date">
                        {date}
                    </div>

                    <div class="event-title">
                        {title}
                    </div>

                    <div class="event-description">
                        {description}
                    </div>

                    <div style="font-size:11px; color:#8b8fa8; margin-top:14px;">
                        {level}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.button(
                "View event →",
                key=f"event_{i}",
                use_container_width=True,
            )


# ============================================================================
# BLOG & ARTICLES
# ============================================================================

def render_blog():

    render_header(
        "Blog & Articles",
        "Stay up to date with AI thinking, practical guidance and OA insights.",
    )

    articles = [
        ("AI Fundamentals", "What Actually Happens When You Ask an LLM a Question?", "A simple explanation of tokens, context windows, inference and model outputs."),
        ("Practical AI", "From Prompt to Production: What Changes?", "Why production AI systems require more than a good prompt."),
        ("Agentic AI", "What Makes an AI Agent Different from a Chatbot?", "Understand the difference between conversational AI and systems that can reason and act."),
        ("Responsible AI", "Why AI Governance Matters", "The practical role of governance, guardrails and monitoring in enterprise AI."),
        ("Data & RAG", "Why Enterprise AI Needs Better Data", "How data quality, retrieval and context influence AI outcomes."),
        ("Innovation", "The Future of AI at OA", "Exploring emerging capabilities, tools and opportunities for innovation."),
    ]

    cols = st.columns(3)

    for i, (tag, title, description) in enumerate(articles):

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="article-card">

                    <div class="article-tag">
                        {tag}
                    </div>

                    <div class="article-title">
                        {title}
                    </div>

                    <div class="article-description">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.button(
                "Read article →",
                key=f"article_{i}",
                use_container_width=True,
            )


# ============================================================================
# TEAMS CALENDAR
# ============================================================================

def render_calendar():

    render_header(
        "Teams Calendar",
        "Access AI workshops, events and invite-only sessions.",
    )

    st.markdown(
        """
        <div class="white-card">

            <div style="font-size:38px;">
                🔒
            </div>

            <div class="card-title" style="margin-top:12px;">
                Invite-only calendar
            </div>

            <div class="card-description">
                This calendar is restricted to invited participants and approved
                OA AI community members. Once connected, this page can display
                the relevant Microsoft Teams calendar and event invitations.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button("Request calendar access →", use_container_width=False):

        st.success(
            "Your access request has been recorded. The AI team can review your request."
        )


# ============================================================================
# HELP & SUPPORT
# ============================================================================

def render_help():

    render_header(
        "Help & Support",
        "Find answers, guidance and support for your AI learning journey.",
    )

    faqs = [
        (
            "Where should I start?",
            "If you are new to AI, begin with the Fundamentals pathway. It covers AI, LLMs, prompt engineering, responsible AI and governance."
        ),
        (
            "How do I choose a pathway?",
            "Choose the pathway that best matches what you are currently trying to learn or build. You can move between pathways at any time."
        ),
        (
            "What are Sandbox Labs?",
            "Sandbox Labs provide safe environments where you can practise AI concepts and experiment with tools without affecting production systems."
        ),
        (
            "How do I attend a workshop?",
            "Visit Workshops & Events to see upcoming sessions. Calendar invitations for restricted sessions will be sent through Microsoft Teams."
        ),
        (
            "Where can I get help with a technical problem?",
            "Use the Community channel or contact the AI team through your internal support route."
        ),
    ]

    for question, answer in faqs:

        with st.expander(question):

            st.write(answer)

    st.markdown(
        '<div class="section-title">Need more help?</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="white-card">

            <div class="card-title">
                Contact the OA AI Team
            </div>

            <div class="card-description">
                For questions about the capability journey, learning pathways,
                workshops or access to sandbox environments, contact the OA AI Team
                through your internal communication channels.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================================
# COMMUNITY
# ============================================================================

def render_community():

    render_header(
        "AI Community",
        "Connect with colleagues, share ideas and learn from what others are building.",
    )

    cols = st.columns(3)

    community_cards = [
        ("💬", "Ask the Community", "Ask questions and get support from colleagues working with AI."),
        ("🏆", "Share Your Build", "Showcase an AI experiment, use case or project."),
        ("🤝", "Find Collaborators", "Connect with people interested in similar AI capabilities."),
    ]

    for col, (icon, title, description) in zip(cols, community_cards):

        with col:

            st.markdown(
                f"""
                <div class="info-card">

                    <div style="font-size:28px;">
                        {icon}
                    </div>

                    <div class="card-title" style="margin-top:10px;">
                        {title}
                    </div>

                    <div class="card-description">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


# ============================================================================
# FEEDBACK
# ============================================================================

def render_feedback():

    render_header(
        "Feedback",
        "Help us improve the OA AI Capability Journey.",
    )

    feedback = st.text_area(
        "What would make this platform more useful?",
        height=180,
        placeholder="Share your feedback, ideas or suggestions...",
    )

    if st.button("Submit feedback"):

        if feedback.strip():

            st.session_state.feedback_sent = True

            st.success(
                "Thanks — your feedback has been recorded for this session."
            )

        else:

            st.warning(
                "Please enter some feedback before submitting."
            )


# ============================================================================
# TRACK DETAIL PAGE
# ============================================================================

def render_track_page(key):

    track = TRACKS[key]

    back_home()

    st.markdown(
        f"""
        <div class="track-hero"
             style="background:{track['bg']};">

            <div class="track-hero-icon">
                {track['icon']}
            </div>

            <div>

                <div class="track-hero-title"
                     style="color:{track['color']};">

                    {track['name']}

                </div>

                <div class="track-hero-description"
                     style="color:{track['color']};">

                    {track['description']}

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="page-section-title">
            Capabilities in this pathway
        </div>

        <div class="page-section-subtitle">
            Explore the learning content available in the {track['name']} pathway.
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(4)

    for i, (title, description, duration) in enumerate(track["courses"]):

        with cols[i % 4]:

            st.markdown(
                f"""
                <div class="course-card">

                    <div class="course-number"
                         style="background:{track['color']}1a;
                                color:{track['color']};">

                        {i + 1:02d}

                    </div>

                    <div class="course-title">
                        {title}
                    </div>

                    <div class="course-description">
                        {description}
                    </div>

                    <div class="course-duration">
                        ⏱ {duration}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.button(
                "Start course →",
                key=f"course_{key}_{i}",
                use_container_width=True,
            )


# ============================================================================
# ROUTER
# ============================================================================

page = st.session_state.page

if page == "home":

    render_home()

elif page == "capability_map":

    render_capability_map()

elif page == "pathways":

    render_pathways()

elif page == "labs":

    render_labs()

elif page == "events":

    render_events()

elif page == "blog":

    render_blog()

elif page == "calendar":

    render_calendar()

elif page == "help":

    render_help()

elif page == "community":

    render_community()

elif page == "feedback":

    render_feedback()

elif page in TRACKS:

    render_track_page(page)