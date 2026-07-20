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
        "description": "Learn how to build, orchestrate and scale AI agents.",
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
        "description": "Work with enterprise data, retrieval systems, embeddings and vector databases.",
        "courses": [
            ("Azure AI Search", "Index and retrieve enterprise content with Azure AI Search.", "2 hrs"),
            ("Vector Databases", "Understand embeddings and vector search for retrieval.", "2 hrs"),
            ("Redis Memory Cache", "Use Redis for fast agent memory and caching.", "1.5 hrs"),
            ("LangChain", "Build retrieval-augmented pipelines using LangChain.", "2.5 hrs"),
            ("Embedding Strategies", "Choose the right embedding model and chunking strategy.", "1.5 hrs"),
        ],
    },

    "llm_promptops": {
        "icon": "💡",
        "name": "LLM & Prompt Ops",
        "color": "#e8781f",
        "bg": "#fef1e6",
        "description": "Learn how to work effectively with leading LLMs and prompt operations.",
        "courses": [
            ("Work with GPT-4 / 4.1 / 5", "Get the most out of OpenAI's latest model family.", "1.5 hrs"),
            ("Claude & Gemini", "Compare and apply Claude and Gemini for common tasks.", "1.5 hrs"),
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
        "description": "Understand how to secure, govern, monitor and responsibly deploy AI.",
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
        "description": "Explore synthetic data, digital twins, open models and sandbox experimentation.",
        "courses": [
            ("Synthetic Data Generation", "Generate realistic synthetic datasets for testing and training.", "2 hrs"),
            ("Digital Twins & Unreal Engine", "Build simulated environments to test AI in the real world.", "3 hrs"),
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


EVENTS = [
    {
        "icon": "📅",
        "title": "Intro to Prompt Engineering for Consultants",
        "date": "22 May 2025",
        "type": "Workshop",
        "color": "#2f6fed",
    },
    {
        "icon": "📗",
        "title": "Building with RAG on Azure AI Search",
        "date": "29 May 2025",
        "type": "Workshop",
        "color": "#2f9e5c",
    },
    {
        "icon": "📘",
        "title": "Multi-Agent Orchestration with LangGraph",
        "date": "5 June 2025",
        "type": "Advanced",
        "color": "#8b5cf6",
    },
    {
        "icon": "🎤",
        "title": "AI Community Showcase",
        "date": "12 June 2025",
        "type": "Community",
        "color": "#e8781f",
    },
]


LABS = [
    {
        "icon": "🔍",
        "title": "RAG Lab",
        "description": "Build a company knowledge assistant using retrieval-augmented generation.",
        "level": "Practitioner",
        "color": "#2f6fed",
        "bg": "#eaf1ff",
    },
    {
        "icon": "🤖",
        "title": "Agent Builder Lab",
        "description": "Create your first AI agent and connect it to tools.",
        "level": "Advanced",
        "color": "#2f9e5c",
        "bg": "#e9f8ee",
    },
    {
        "icon": "🌊",
        "title": "Prompt Flow Lab",
        "description": "Test, evaluate and improve prompts through structured experimentation.",
        "level": "Practitioner",
        "color": "#8b5cf6",
        "bg": "#f2edfe",
    },
    {
        "icon": "🧬",
        "title": "Synthetic Data Lab",
        "description": "Generate realistic data for AI and analytics experimentation.",
        "level": "Innovation",
        "color": "#e8781f",
        "bg": "#fef1e6",
    },
]


ARTICLES = [
    {
        "icon": "🧠",
        "title": "What is Generative AI?",
        "category": "AI Fundamentals",
        "description": "A simple introduction to generative AI, LLMs and how modern AI systems create content.",
        "read_time": "5 min read",
    },
    {
        "icon": "🤖",
        "title": "The Rise of Agentic AI",
        "category": "Agentic AI",
        "description": "How AI agents are evolving from chatbots into systems that can reason, plan and act.",
        "read_time": "8 min read",
    },
    {
        "icon": "🔍",
        "title": "Understanding RAG",
        "category": "RAG & Data",
        "description": "Why retrieval-augmented generation is important for enterprise AI applications.",
        "read_time": "6 min read",
    },
    {
        "icon": "🛡️",
        "title": "Responsible AI in Practice",
        "category": "Governance",
        "description": "The principles and practical guardrails needed to deploy AI responsibly.",
        "read_time": "7 min read",
    },
]


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
    ("🏛️", "Unreal Engine", "https://dev.epicgames.com/documentation/en-us/unreal-engine"),
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
    background-color: #f3f5f9;
}

.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* =========================
   SIDEBAR
========================= */

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
    padding: 4px 0 25px 0;
    font-weight: 800;
    font-size: 16px;
    color: white !important;
}

.sidebar-logo-icon {
    font-size: 24px;
}

.sidebar-section-label {
    color: #858db8 !important;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin: 20px 0 8px 5px;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] button {
    background: transparent !important;
    border: none !important;
    color: #c7cbe6 !important;
    text-align: left !important;
    justify-content: flex-start !important;
    font-weight: 500 !important;
    font-size: 13px !important;
    min-height: 38px !important;
    padding: 8px 12px !important;
    border-radius: 8px !important;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] button:hover {
    background: #202957 !important;
    color: white !important;
}

.sidebar-active button {
    background: #2b3570 !important;
    color: white !important;
}

.quote-box {
    background: #1c2450;
    border-radius: 10px;
    padding: 16px;
    margin-top: 25px;
    font-size: 12px;
    line-height: 1.55;
    color: #b8bde0 !important;
}

.quote-attr {
    margin-top: 10px;
    font-weight: 700;
    color: #7f8ad4 !important;
}

/* =========================
   HEADERS
========================= */

.page-title {
    font-size: 28px;
    font-weight: 800;
    color: #101433;
    line-height: 1.25;
}

.page-subtitle {
    color: #6b7086;
    font-size: 14px;
    margin-top: 5px;
}

.section-title {
    font-size: 18px;
    font-weight: 800;
    color: #12163a;
    margin: 8px 0 14px 0;
}

.page-heading {
    font-size: 26px;
    font-weight: 800;
    color: #12163a;
    margin-bottom: 4px;
}

.page-description {
    color: #6b7086;
    font-size: 14px;
    margin-bottom: 24px;
}

/* =========================
   BUTTONS
========================= */

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

/* =========================
   WHITE CARDS
========================= */

.white-card {
    background: white;
    border-radius: 14px;
    border: 1px solid #e7e9f2;
    padding: 20px;
    height: 100%;
}

/* =========================
   TRACK CARDS
========================= */

.track-card {
    border-radius: 12px;
    padding: 16px;
    min-height: 150px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.track-card-icon {
    font-size: 25px;
    margin-bottom: 10px;
}

.track-card-title {
    font-size: 14px;
    font-weight: 800;
    line-height: 1.3;
}

.track-card-description {
    font-size: 11.5px;
    color: #5c6079;
    line-height: 1.45;
    margin-top: 6px;
}

.track-card-count {
    font-size: 11px;
    font-weight: 700;
    margin-top: 12px;
}

/* =========================
   CAPABILITY JOURNEY
========================= */

.journey-wrapper {
    background: white;
    border-radius: 14px;
    border: 1px solid #e7e9f2;
    padding: 28px 20px 22px 20px;
}

.journey-stage {
    height: 100%;
    text-align: center;
}

.journey-icon {
    width: 70px;
    height: 70px;
    margin: 0 auto 12px auto;
    border-radius: 50%;
    border: 3px solid;
    display: flex;
    align-items: center;
    justify-content: center;
    background: white;
    font-size: 27px;
}

.journey-title {
    font-size: 12px;
    font-weight: 800;
    line-height: 1.3;
    min-height: 32px;
}

.journey-subtitle {
    font-size: 11px;
    color: #6b7086;
    margin: 4px 0 12px 0;
    min-height: 30px;
}

.journey-list {
    text-align: left;
    list-style: none;
    padding: 0;
    margin: 0;
    font-size: 11.5px;
    color: #454868;
}

.journey-list li {
    padding: 6px 2px;
    border-bottom: 1px dashed #eef0f6;
}

.journey-list li::before {
    content: "• ";
}

/* =========================
   COURSE CARDS
========================= */

.course-card {
    background: white;
    border-radius: 12px;
    border: 1px solid #e7e9f2;
    padding: 17px;
    min-height: 180px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.course-number {
    width: 28px;
    height: 28px;
    border-radius: 7px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    font-weight: 800;
    margin-bottom: 10px;
}

.course-title {
    font-weight: 700;
    font-size: 14px;
    color: #12163a;
    line-height: 1.35;
}

.course-description {
    font-size: 12px;
    color: #5c6079;
    line-height: 1.45;
    margin-top: 6px;
}

.course-duration {
    font-size: 11px;
    color: #8b8fa8;
    font-weight: 600;
    margin-top: 12px;
}

/* =========================
   EVENTS
========================= */

.event-card {
    background: white;
    border: 1px solid #e7e9f2;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 12px;
}

.event-card-header {
    display: flex;
    align-items: flex-start;
    gap: 14px;
}

.event-icon {
    width: 42px;
    height: 42px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 19px;
    flex-shrink: 0;
}

.event-title {
    font-weight: 700;
    font-size: 14px;
    color: #16193b;
}

.event-date {
    font-size: 12px;
    color: #6b7086;
    margin-top: 5px;
}

.event-tag {
    display: inline-block;
    margin-top: 10px;
    padding: 4px 9px;
    border-radius: 12px;
    font-size: 10px;
    font-weight: 700;
}

/* =========================
   LABS
========================= */

.lab-card {
    background: white;
    border: 1px solid #e7e9f2;
    border-radius: 14px;
    padding: 20px;
    min-height: 230px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.lab-icon {
    font-size: 30px;
}

.lab-title {
    font-size: 16px;
    font-weight: 800;
    margin-top: 14px;
}

.lab-description {
    font-size: 12.5px;
    color: #5c6079;
    line-height: 1.5;
    margin-top: 7px;
}

.lab-level {
    font-size: 11px;
    font-weight: 700;
    margin-top: 15px;
}

/* =========================
   ARTICLES
========================= */

.article-card {
    background: white;
    border: 1px solid #e7e9f2;
    border-radius: 14px;
    padding: 20px;
    min-height: 220px;
}

.article-icon {
    font-size: 30px;
}

.article-category {
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 14px;
}

.article-title {
    font-size: 16px;
    font-weight: 800;
    color: #12163a;
    margin-top: 6px;
}

.article-description {
    font-size: 12.5px;
    color: #5c6079;
    line-height: 1.5;
    margin-top: 8px;
}

.article-time {
    font-size: 11px;
    color: #8b8fa8;
    font-weight: 600;
    margin-top: 15px;
}

/* =========================
   TOOLS
========================= */

.tool-chip {
    display: block;
    background: white;
    border: 1px solid #e7e9f2;
    border-radius: 9px;
    padding: 10px;
    color: #23264a !important;
    text-decoration: none;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 9px;
}

.tool-chip:hover {
    border-color: #2f6fed;
    background: #eaf1ff;
}

/* =========================
   INFO BANNERS
========================= */

.info-banner {
    background: #eef1fb;
    border-radius: 12px;
    padding: 18px;
    margin-top: 20px;
}

.locked-banner {
    background: #fff8e8;
    border: 1px solid #f1d58a;
    border-radius: 14px;
    padding: 25px;
    text-align: center;
}

/* =========================
   FAQ
========================= */

.faq-card {
    background: white;
    border: 1px solid #e7e9f2;
    border-radius: 12px;
    padding: 4px 18px;
    margin-bottom: 12px;
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

    st.markdown(
        '<div class="sidebar-section-label">Navigation</div>',
        unsafe_allow_html=True,
    )

    sidebar_items = [
        ("🏠", "Home", "home"),
        ("🗺️", "Capability Map", "capability_map"),
        ("🧪", "Sandbox Labs", "labs"),
        ("🗓️", "Workshops & Events", "events"),
        ("📰", "Blog & Articles", "blog"),
        ("📅", "Teams Calendar", "calendar"),
        ("❓", "Help & Support", "help"),
    ]

    for icon, label, page in sidebar_items:

        if st.session_state.page == page:
            st.markdown('<div class="sidebar-active">', unsafe_allow_html=True)

        st.button(
            f"{icon}  {label}",
            key=f"sidebar_{page}",
            use_container_width=True,
            on_click=navigate,
            args=(page,),
        )

        if st.session_state.page == page:
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-section-label">Resources</div>',
        unsafe_allow_html=True,
    )

    st.button(
        "🛠️  Tools & Guides",
        key="sidebar_tools",
        use_container_width=True,
        on_click=navigate,
        args=("tools",),
    )

    st.button(
        "📁  Use Cases",
        key="sidebar_usecases",
        use_container_width=True,
        on_click=navigate,
        args=("usecases",),
    )

    st.markdown(
        """
        <div class="quote-box">
            "We connect AI models to our foundational tools and semantics layers —
            enabling agents to read, reason and act across data and models."

            <div class="quote-attr">
                — OA AI Team
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================================
# HEADER
# ============================================================================

header_left, header_right = st.columns([3, 1])

with header_left:

    st.markdown(
        '<div class="page-title">OA AI Capability Journey</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="page-subtitle">Learn. Build. Apply. Lead.</div>',
        unsafe_allow_html=True,
    )

with header_right:

    with st.popover("ℹ️ How to use this board", use_container_width=True):

        st.markdown("### Getting around the board")

        st.markdown(
            """
            - Use the **sidebar** to move between pages.
            - Explore the **Capability Map** to understand the full AI journey.
            - Use **Sandbox Labs** for hands-on practice.
            - Browse **Workshops & Events** for upcoming learning opportunities.
            - Read **Blog & Articles** for AI insights and updates.
            - The **Teams Calendar** is available to invited users.
            """
        )


st.write("")


# ============================================================================
# PAGE: HOME
# ============================================================================

def render_home():

    st.markdown(
        '<div class="section-title">Choose your learning pathway</div>',
        unsafe_allow_html=True,
    )

    track_cols = st.columns(6)

    for col, (key, track) in zip(track_cols, TRACKS.items()):

        with col:

            st.markdown(
                f"""
                <div class="track-card"
                     style="background:{track['bg']};
                            border:1px solid {track['color']}44;">

                    <div>
                        <div class="track-card-icon">
                            {track['icon']}
                        </div>

                        <div class="track-card-title"
                             style="color:{track['color']};">
                            {track['name']}
                        </div>

                        <div class="track-card-description">
                            {track['description']}
                        </div>
                    </div>

                    <div class="track-card-count"
                         style="color:{track['color']};">
                        {len(track['courses'])} capabilities
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.button(
                "Explore pathway →",
                key=f"home_track_{key}",
                use_container_width=True,
                on_click=navigate,
                args=(key,),
            )


    st.write("")

    # ========================================================================
    # AI CAPABILITY JOURNEY
    # ========================================================================

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
            "fundamentals",
        ),
        (
            "🛠️",
            "PRACTITIONER",
            "Apply & build",
            "#e8781f",
            ["GPT & LLMs", "Claude & Gemini", "Multi-Modal AI", "GitHub Copilot"],
            "llm_promptops",
        ),
        (
            "🏗️",
            "ADVANCED BUILDERS",
            "Design & integrate",
            "#8b5cf6",
            ["Azure AI Search", "Vector Databases", "Redis", "LangChain"],
            "rag_data",
        ),
        (
            "🕸️",
            "AGENTIC AI",
            "Orchestrate & scale",
            "#2f9e5c",
            ["MCP & Tool Abstraction", "Copilot Studio", "Agent Frameworks", "LangGraph"],
            "agentic",
        ),
        (
            "🛡️",
            "ENTERPRISE DEPLOYMENT",
            "Secure & govern",
            "#e0373f",
            ["Security & Guardrails", "Auditing & Monitoring", "Compliance", "Decision Guardrails"],
            "governance",
        ),
        (
            "🚀",
            "INNOVATION LAB",
            "Simulate & explore",
            "#12163a",
            ["Synthetic Data", "Digital Twins", "Open Models", "Simulation"],
            "simulation",
        ),
    ]

    st.markdown(
        '<div class="journey-wrapper">',
        unsafe_allow_html=True,
    )

    journey_cols = st.columns(6)

    for col, (icon, title, subtitle, color, items, track_key) in zip(
        journey_cols,
        stages,
    ):

        with col:

            st.markdown(
                f"""
                <div class="journey-stage">

                    <div class="journey-icon"
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
                        {''.join(f'<li>{item}</li>' for item in items)}
                    </ul>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.button(
                "View pathway →",
                key=f"journey_{track_key}",
                use_container_width=True,
                on_click=navigate,
                args=(track_key,),
            )

    st.markdown(
        '</div>',
        unsafe_allow_html=True,
    )


    st.write("")

    # ========================================================================
    # HOW YOU LEARN
    # ========================================================================

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

    for col, (icon, title, subtitle) in zip(step_cols, steps):

        with col:

            st.markdown(
                f"""
                <div class="white-card"
                     style="text-align:center;
                            min-height:125px;">

                    <div style="font-size:25px;">
                        {icon}
                    </div>

                    <div style="font-weight:800;
                                font-size:12px;
                                color:#12163a;
                                margin-top:8px;">
                        {title}
                    </div>

                    <div style="font-size:11px;
                                color:#6b7086;
                                margin-top:5px;">
                        {subtitle}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


    st.write("")

    # ========================================================================
    # START HERE BANNER
    # ========================================================================

    st.markdown(
        """
        <div class="info-banner">

            <div style="font-size:24px;">
                🌱
            </div>

            <div>

                <div style="font-size:15px;
                            font-weight:800;
                            color:#12163a;">
                    New to AI?
                </div>

                <div style="font-size:12.5px;
                            color:#6b7086;
                            margin-top:4px;">
                    Start with the Fundamentals pathway and build your knowledge
                    step by step before moving into advanced AI capabilities.
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================================
# PAGE: CAPABILITY MAP
# ============================================================================

def render_capability_map():

    st.markdown(
        '<div class="page-heading">🗺️ Capability Map</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-description">
            Explore the full OA AI capability landscape and find the pathway
            that matches your current skills and interests.
        </div>
        """,
        unsafe_allow_html=True,
    )

    for key, track in TRACKS.items():

        col1, col2 = st.columns([4, 1])

        with col1:

            st.markdown(
                f"""
                <div class="white-card">

                    <div style="display:flex;
                                align-items:center;
                                gap:14px;">

                        <div style="font-size:30px;">
                            {track['icon']}
                        </div>

                        <div>

                            <div style="font-size:17px;
                                        font-weight:800;
                                        color:{track['color']};">
                                {track['name']}
                            </div>

                            <div style="font-size:12px;
                                        color:#6b7086;
                                        margin-top:4px;">
                                {track['description']}
                            </div>

                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:

            st.button(
                "Explore →",
                key=f"map_{key}",
                use_container_width=True,
                on_click=navigate,
                args=(key,),
            )

        st.write("")


# ============================================================================
# PAGE: SANDBOX LABS
# ============================================================================

def render_labs():

    st.markdown(
        '<div class="page-heading">🧪 Sandbox Labs</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-description">
            Learn by doing. Use these guided environments to experiment with
            AI tools, models and workflows.
        </div>
        """,
        unsafe_allow_html=True,
    )

    lab_cols = st.columns(2)

    for col, lab in zip(lab_cols * 2, LABS):

        with col:

            st.markdown(
                f"""
                <div class="lab-card"
                     style="background:{lab['bg']};
                            border-color:{lab['color']}44;">

                    <div>

                        <div class="lab-icon">
                            {lab['icon']}
                        </div>

                        <div class="lab-title"
                             style="color:{lab['color']};">
                            {lab['title']}
                        </div>

                        <div class="lab-description">
                            {lab['description']}
                        </div>

                    </div>

                    <div>

                        <div class="lab-level"
                             style="color:{lab['color']};">
                            {lab['level']}
                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.button(
                "Open Lab →",
                key=f"open_lab_{lab['title']}",
                use_container_width=True,
            )

            st.write("")


# ============================================================================
# PAGE: EVENTS
# ============================================================================

def render_events():

    st.markdown(
        '<div class="page-heading">🗓️ Workshops & Events</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-description">
            Join workshops, community sessions and practical learning events
            across the OA AI capability journey.
        </div>
        """,
        unsafe_allow_html=True,
    )

    for event in EVENTS:

        st.markdown(
            f"""
            <div class="event-card">

                <div class="event-card-header">

                    <div class="event-icon"
                         style="background:{event['color']}18;
                                color:{event['color']};">
                        {event['icon']}
                    </div>

                    <div>

                        <div class="event-title">
                            {event['title']}
                        </div>

                        <div class="event-date">
                            📅 {event['date']}
                        </div>

                        <span class="event-tag"
                              style="background:{event['color']}18;
                                     color:{event['color']};">
                            {event['type']}
                        </span>

                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.button(
            "View event details →",
            key=f"event_{event['title']}",
        )

        st.write("")


# ============================================================================
# PAGE: BLOG
# ============================================================================

def render_blog():

    st.markdown(
        '<div class="page-heading">📰 Blog & Articles</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-description">
            Explore practical AI insights, explainers, capability updates and
            stories from the OA AI community.
        </div>
        """,
        unsafe_allow_html=True,
    )

    article_cols = st.columns(2)

    for col, article in zip(article_cols * 2, ARTICLES):

        with col:

            st.markdown(
                f"""
                <div class="article-card">

                    <div class="article-icon">
                        {article['icon']}
                    </div>

                    <div class="article-category"
                         style="color:#2f6fed;">
                        {article['category']}
                    </div>

                    <div class="article-title">
                        {article['title']}
                    </div>

                    <div class="article-description">
                        {article['description']}
                    </div>

                    <div class="article-time">
                        ⏱ {article['read_time']}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.button(
                "Read article →",
                key=f"article_{article['title']}",
                use_container_width=True,
            )

            st.write("")


# ============================================================================
# PAGE: TEAMS CALENDAR
# ============================================================================

def render_calendar():

    st.markdown(
        '<div class="page-heading">📅 Teams Calendar</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-description">
            Access private workshops, invite-only sessions and team events.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="locked-banner">

            <div style="font-size:40px;">
                🔒
            </div>

            <div style="font-size:20px;
                        font-weight:800;
                        color:#12163a;
                        margin-top:10px;">
                Invite-only calendar
            </div>

            <div style="font-size:13px;
                        color:#6b7086;
                        max-width:550px;
                        margin:10px auto;">
                This calendar contains private Microsoft Teams meetings,
                internal workshops and invite-only AI capability sessions.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="white-card" style="text-align:center;">
                <div style="font-size:25px;">👥</div>
                <div style="font-weight:800;margin-top:8px;">
                    Internal workshops
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
            <div class="white-card" style="text-align:center;">
                <div style="font-size:25px;">🎤</div>
                <div style="font-weight:800;margin-top:8px;">
                    Expert sessions
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:

        st.markdown(
            """
            <div class="white-card" style="text-align:center;">
                <div style="font-size:25px;">🚀</div>
                <div style="font-weight:800;margin-top:8px;">
                    Community events
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    st.info(
        "To connect the live Microsoft Teams calendar, add your internal Teams "
        "calendar URL or Microsoft Graph integration here."
    )


# ============================================================================
# PAGE: HELP & SUPPORT
# ============================================================================

def render_help():

    st.markdown(
        '<div class="page-heading">❓ Help & Support</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-description">
            Find answers, report issues and get help navigating the OA AI
            Capability Journey.
        </div>
        """,
        unsafe_allow_html=True,
    )

    faqs = [
        (
            "Where should I start?",
            "If you are new to AI, start with the Fundamentals pathway. "
            "If you already have experience, explore the Capability Map and "
            "choose a pathway that matches your current skills."
        ),
        (
            "How do I access a Sandbox Lab?",
            "Open the Sandbox Labs page from the sidebar and choose the lab "
            "that matches the capability you want to practise."
        ),
        (
            "How do I join a workshop?",
            "Upcoming public workshops are listed on the Workshops & Events "
            "page. Invite-only sessions are available through the Teams Calendar."
        ),
        (
            "How do I suggest a new course?",
            "Use the internal feedback channel or contact the OA AI Capability "
            "Journey team with your suggestion."
        ),
        (
            "Who can I contact for technical support?",
            "Contact the OA AI support team through your internal support channel "
            "or the relevant Microsoft Teams community."
        ),
    ]

    for question, answer in faqs:

        with st.expander(question):

            st.write(answer)

    st.write("")

    st.markdown(
        """
        <div class="info-banner">

            <div style="font-size:25px;">
                💬
            </div>

            <div>

                <div style="font-weight:800;
                            color:#12163a;">
                    Still need help?
                </div>

                <div style="font-size:12px;
                            color:#6b7086;
                            margin-top:4px;">
                    Contact the OA AI team or ask the community for support.
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================================
# PAGE: TOOLS
# ============================================================================

def render_tools():

    st.markdown(
        '<div class="page-heading">🛠️ Tools & Guides</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-description">
            Explore the tools and technologies used across the OA AI ecosystem.
        </div>
        """,
        unsafe_allow_html=True,
    )

    tool_cols = st.columns(3)

    for col, (icon, name, url) in zip(tool_cols * 4, TOOLS):

        with col:

            st.markdown(
                f"""
                <a class="tool-chip"
                   href="{url}"
                   target="_blank"
                   rel="noopener noreferrer">

                    {icon} {name}
                    <span style="float:right;">↗</span>

                </a>
                """,
                unsafe_allow_html=True,
            )


# ============================================================================
# PAGE: USE CASES
# ============================================================================

def render_use_cases():

    st.markdown(
        '<div class="page-heading">📁 AI Use Cases</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-description">
            Explore examples of how AI capabilities can be applied across
            consulting, operations, data and technology.
        </div>
        """,
        unsafe_allow_html=True,
    )

    use_cases = [
        ("🔍", "Knowledge Assistant", "Search and reason across internal documents."),
        ("🤖", "AI Agent", "Automate multi-step tasks using tools and data."),
        ("📊", "Data Analysis", "Use AI to accelerate analysis and insight generation."),
        ("📝", "Document Intelligence", "Extract, summarise and classify enterprise documents."),
        ("⚙️", "Process Automation", "Combine AI with workflows to improve productivity."),
        ("🧪", "Synthetic Data", "Generate realistic data for testing and experimentation."),
    ]

    cols = st.columns(3)

    for col, (icon, title, description) in zip(cols * 2, use_cases):

        with col:

            st.markdown(
                f"""
                <div class="white-card"
                     style="min-height:170px;">

                    <div style="font-size:28px;">
                        {icon}
                    </div>

                    <div style="font-size:15px;
                                font-weight:800;
                                color:#12163a;
                                margin-top:12px;">
                        {title}
                    </div>

                    <div style="font-size:12px;
                                color:#6b7086;
                                line-height:1.5;
                                margin-top:7px;">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.write("")


# ============================================================================
# PAGE: TRACK DETAIL
# ============================================================================

def render_track_page(track_key):

    track = TRACKS[track_key]

    st.button(
        "← Back to Capability Map",
        key=f"back_{track_key}",
        on_click=navigate,
        args=("capability_map",),
    )

    st.markdown(
        f"""
        <div style="background:{track['bg']};
                    border-radius:14px;
                    padding:25px;
                    margin:15px 0 25px 0;">

            <div style="display:flex;
                        align-items:center;
                        gap:16px;">

                <div style="font-size:38px;">
                    {track['icon']}
                </div>

                <div>

                    <div style="font-size:25px;
                                font-weight:800;
                                color:{track['color']};">
                        {track['name']}
                    </div>

                    <div style="font-size:13px;
                                color:{track['color']};
                                margin-top:5px;">
                        {track['description']}
                    </div>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Capabilities in this pathway</div>',
        unsafe_allow_html=True,
    )

    course_cols = st.columns(4)

    for i, (title, description, duration) in enumerate(track["courses"]):

        with course_cols[i % 4]:

            st.markdown(
                f"""
                <div class="course-card">

                    <div>

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

                    </div>

                    <div class="course-duration">
                        ⏱ {duration}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.button(
                "Start capability →",
                key=f"course_{track_key}_{i}",
                use_container_width=True,
            )

            st.write("")


# ============================================================================
# ROUTER
# ============================================================================

if st.session_state.page == "home":

    render_home()

elif st.session_state.page == "capability_map":

    render_capability_map()

elif st.session_state.page == "labs":

    render_labs()

elif st.session_state.page == "events":

    render_events()

elif st.session_state.page == "blog":

    render_blog()

elif st.session_state.page == "calendar":

    render_calendar()

elif st.session_state.page == "help":

    render_help()

elif st.session_state.page == "tools":

    render_tools()

elif st.session_state.page == "usecases":

    render_use_cases()

elif st.session_state.page in TRACKS:

    render_track_page(st.session_state.page)

else:

    render_home()