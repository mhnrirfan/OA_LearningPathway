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
        "courses": [
            ("Synthetic Data Generation", "Generate realistic synthetic datasets for testing and training.", "2 hrs"),
            ("Digital Twins (Unreal Engine)", "Build simulated environments to test AI in the real world.", "3 hrs"),
            ("Mistral & LLAMA", "Explore open-weight model families and when to use them.", "1.5 hrs"),
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


TOOL_LINKS = {
    "Azure AI Search": ("🔷", "https://learn.microsoft.com/en-us/azure/search/"),
    "Redis": ("🟥", "https://redis.io/docs/latest/"),
    "LangChain": ("⛓️", "https://python.langchain.com/docs/introduction/"),
    "LangGraph": ("🔗", "https://langchain-ai.github.io/langgraph/"),
    "Copilot Studio": ("🧩", "https://learn.microsoft.com/en-us/microsoft-copilot-studio/"),
    "MS Foundry": ("Ⓜ️", "https://learn.microsoft.com/en-us/azure/ai-foundry/"),
    "GitHub Copilot": ("🐙", "https://docs.github.com/en/copilot"),
    "Celonis API": ("🌀", "https://docs.celonis.com/"),
    "OpenAI": ("🌐", "https://platform.openai.com/docs"),
    "Claude": ("✨", "https://docs.claude.com/"),
    "Gemini": ("💎", "https://ai.google.dev/gemini-api/docs"),
    "Llama": ("🦙", "https://www.llama.com/docs/overview/"),
    "Mistral": ("🌪️", "https://docs.mistral.ai/"),
    "DALL-E": ("🎨", "https://platform.openai.com/docs/guides/images"),
    "Midjourney": ("🌆", "https://docs.midjourney.com/"),
    "Whisper": ("🔊", "https://platform.openai.com/docs/guides/speech-to-text"),
    "Unreal Engine": ("🏛️", "https://dev.epicgames.com/documentation/en-us/unreal-engine"),
    "Prompt Flow": ("🌊", "https://microsoft.github.io/promptflow/"),
    "LangSmith": ("🦜", "https://docs.smith.langchain.com/"),
    "W&B": ("⚖️", "https://docs.wandb.ai/"),
}


# ============================================================================
# SESSION STATE
# ============================================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "feedback_sent" not in st.session_state:
    st.session_state.feedback_sent = False


def go_home():
    st.session_state.page = "home"


def go_page(page):
    st.session_state.page = page


# ============================================================================
# GLOBAL CSS
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
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

p, div, span, li, a {
    overflow-wrap: break-word;
    word-break: break-word;
}


/* ============================================================================
SIDEBAR
============================================================================ */

section[data-testid="stSidebar"] {
    background-color: #131a3a;
}

section[data-testid="stSidebar"] * {
    color: #d7dbf0 !important;
}

.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 4px 0 22px 0;
    font-weight: 800;
    font-size: 16px;
    color: white !important;
    line-height: 1.3;
}

.sidebar-logo .logo-icon {
    font-size: 24px;
    flex-shrink: 0;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] > button {
    width: 100%;
    border: none !important;
    background: transparent !important;
    color: #c7cbe6 !important;
    text-align: left !important;
    justify-content: flex-start !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    padding: 9px 12px !important;
    min-height: 40px !important;
    border-radius: 8px !important;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover {
    background-color: #202956 !important;
    color: white !important;
}

.nav-active {
    display: flex;
    align-items: center;
    gap: 10px;
    background-color: #2b3570;
    color: white !important;
    padding: 10px 12px;
    border-radius: 8px;
    margin-bottom: 4px;
    font-size: 13.5px;
    font-weight: 700;
}

.quote-box {
    background-color: #1c2450;
    border-radius: 10px;
    padding: 16px;
    margin-top: 24px;
    font-size: 12px;
    line-height: 1.55;
    color: #b8bde0;
}

.quote-attr {
    margin-top: 10px;
    font-weight: 700;
    color: #7f8ad4 !important;
}


/* ============================================================================
HEADER
============================================================================ */

.page-title {
    font-size: 28px;
    font-weight: 800;
    color: #101433;
    margin: 0;
    line-height: 1.35;
}

.page-subtitle {
    color: #6b7086;
    font-size: 14px;
    margin-top: 4px;
    line-height: 1.5;
}

div[data-testid="stButton"] > button {
    border-radius: 8px;
    font-weight: 600;
    font-size: 13px;
    border: 1px solid #d7dae3;
    background-color: white;
    color: #2c3050;
    padding: 8px 12px;
    white-space: normal;
    line-height: 1.3;
    min-height: 40px;
}

div[data-testid="stButton"] > button:hover {
    border-color: #2f6fed;
    color: #2f6fed;
}

div[data-testid="stPopover"] > button {
    border-radius: 8px;
    font-weight: 600;
    font-size: 13px;
    border: 1px solid #d7dae3;
    background-color: white;
    color: #2c3050;
    padding: 8px 12px;
    min-height: 40px;
}


/* ============================================================================
SECTIONS
============================================================================ */

.section-title {
    font-size: 18px;
    font-weight: 800;
    color: #12163a;
    margin: 8px 0 14px 0;
    line-height: 1.3;
}

.section-title-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 8px 0 14px 0;
}


/* ============================================================================
PATHWAY CARDS
============================================================================ */

.pathway-card {
    min-height: 112px;
    height: 112px;
    border-radius: 12px;
    padding: 15px;
    border: 1px solid;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.pathway-icon {
    font-size: 22px;
    line-height: 1;
}

.pathway-title {
    font-size: 13px;
    font-weight: 800;
    line-height: 1.25;
}

.pathway-meta {
    font-size: 11px;
    color: #6b7086;
}


/* ============================================================================
JOURNEY
============================================================================ */

.journey-wrap {
    background: white;
    border-radius: 14px;
    padding: 28px 22px 20px 22px;
    border: 1px solid #e7e9f2;
    margin-bottom: 26px;
}

.journey-stage {
    min-height: 265px;
    height: 265px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.journey-circle {
    width: 68px;
    height: 68px;
    border-radius: 50%;
    border: 3px solid;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 23px;
    margin-bottom: 10px;
    background: white;
}

.journey-stage-title {
    text-align: center;
    font-weight: 800;
    font-size: 12px;
    line-height: 1.3;
    min-height: 34px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.journey-stage-sub {
    text-align: center;
    font-size: 11px;
    color: #6b7086;
    min-height: 28px;
    margin-top: 3px;
}

.journey-list {
    list-style: none;
    padding: 0;
    margin: 6px 0 0 0;
    width: 100%;
    font-size: 11.5px;
    color: #33364f;
    line-height: 1.35;
}

.journey-list li {
    padding: 5px 2px;
    border-bottom: 1px dashed #eef0f6;
}

.journey-list li:before {
    content: "•  ";
}


/* ============================================================================
HOW YOU LEARN
============================================================================ */

.step-card {
    background: white;
    border-radius: 12px;
    border: 1px solid #e7e9f2;
    padding: 16px 12px;
    text-align: center;
    min-height: 120px;
    height: 120px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.step-icon {
    font-size: 21px;
    margin-bottom: 7px;
}

.step-title {
    font-weight: 700;
    font-size: 12px;
    color: #12163a;
    line-height: 1.3;
}

.step-sub {
    font-size: 11px;
    color: #6b7086;
    margin-top: 4px;
    line-height: 1.35;
}


/* ============================================================================
GENERAL CARDS
============================================================================ */

.white-card {
    background: white;
    border-radius: 14px;
    border: 1px solid #e7e9f2;
    padding: 20px;
}

.course-card {
    background: white;
    border-radius: 12px;
    border: 1px solid #e7e9f2;
    padding: 16px;
    min-height: 180px;
    height: 180px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.course-number {
    width: 26px;
    height: 26px;
    border-radius: 7px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    font-weight: 800;
    margin-bottom: 8px;
}

.course-title {
    font-weight: 700;
    font-size: 14px;
    color: #12163a;
    margin-bottom: 5px;
    line-height: 1.35;
}

.course-desc {
    font-size: 12px;
    color: #5c6079;
    line-height: 1.45;
}

.course-meta {
    font-size: 11px;
    color: #8b8fa8;
    font-weight: 600;
}


/* ============================================================================
TRACK HERO
============================================================================ */

.track-hero {
    border-radius: 14px;
    padding: 24px;
    margin: 18px 0 22px 0;
    display: flex;
    align-items: center;
    gap: 16px;
}

.track-hero-icon {
    width: 56px;
    height: 56px;
    border-radius: 14px;
    background: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    flex-shrink: 0;
}

.track-hero-title {
    font-size: 24px;
    font-weight: 800;
    margin: 0;
    line-height: 1.2;
}

.track-hero-sub {
    font-size: 13px;
    margin-top: 4px;
    opacity: 0.85;
}


/* ============================================================================
LABS
============================================================================ */

.lab-card {
    border-radius: 12px;
    padding: 20px;
    min-height: 215px;
    height: 215px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.lab-title {
    font-weight: 800;
    font-size: 16px;
    margin-bottom: 7px;
}

.lab-desc {
    font-size: 12px;
    color: #454868;
    line-height: 1.5;
}


/* ============================================================================
TOOLS
============================================================================ */

a.tool-chip {
    display: flex;
    align-items: center;
    gap: 7px;
    background: #f7f8fb;
    border: 1px solid #edeef4;
    border-radius: 8px;
    padding: 8px 9px;
    font-size: 11.5px;
    font-weight: 600;
    color: #23264a !important;
    margin-bottom: 8px;
    line-height: 1.25;
    text-decoration: none;
}

a.tool-chip:hover {
    border-color: #2f6fed;
    background: #eaf1ff;
    color: #2f6fed !important;
}

.tool-arrow {
    margin-left: auto;
    opacity: 0.45;
}


/* ============================================================================
EVENTS / ARTICLES
============================================================================ */

.event-card {
    background: white;
    border: 1px solid #e7e9f2;
    border-radius: 12px;
    padding: 18px;
    min-height: 150px;
    height: 150px;
}

.article-card {
    background: white;
    border: 1px solid #e7e9f2;
    border-radius: 12px;
    padding: 20px;
    min-height: 230px;
    height: 230px;
}


/* ============================================================================
FOOTER
============================================================================ */

.footer-banner {
    background: #eef1fb;
    border-radius: 12px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 14px;
    margin-top: 26px;
}


/* ============================================================================
BACK BUTTON
============================================================================ */

.back-marker + div[data-testid="stButton"] button {
    border: none;
    background: transparent;
    color: #2f6fed;
    font-weight: 700;
    padding: 4px 0;
    min-height: unset;
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
            <span class="logo-icon">🔷</span>
            <span>OA AI Capability Journey</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    nav_items = [
        ("🏠", "Home", "home"),
        ("🗺️", "Capability Map", "capability_map"),
        ("🧪", "Sandbox Labs", "labs"),
        ("🗓️", "Workshops & Events", "events"),
        ("📰", "Blog & Articles", "blog"),
        ("📅", "Teams Calendar", "calendar"),
        ("❓", "Help & Support", "help"),
    ]

    for icon, label, page_key in nav_items:

        if st.session_state.page == page_key:

            st.markdown(
                f"""
                <div class="nav-active">
                    <span>{icon}</span>
                    <span>{label}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        else:

            st.button(
                f"{icon}  {label}",
                key=f"nav_{page_key}",
                use_container_width=True,
                on_click=go_page,
                args=(page_key,),
            )

    st.markdown(
        """
        <div class="quote-box">
            "We connect AI models to our foundational tools and semantics layers —
            enabling agents to read, reason and act across data and models."

            <div class="quote-attr">— OA AI Team</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================================
# SHARED HEADER
# ============================================================================

h1, h2 = st.columns([3, 2])

with h1:

    st.markdown(
        '<div class="page-title">OA AI Capability Journey</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="page-subtitle">Learn. Build. Apply. Lead.</div>',
        unsafe_allow_html=True,
    )


with h2:

    b1, b2, b3 = st.columns(3)

    with b1:

        with st.popover("ℹ️ How to use this board", use_container_width=True):

            st.markdown("**Getting around the board**")

            st.markdown(
                """
                - Use the sidebar to explore different areas.
                - Use the **Capability Map** to explore AI capabilities.
                - Follow the journey from Foundation to Innovation.
                - Use **Sandbox Labs** for hands-on practice.
                - Check **Workshops & Events** for upcoming sessions.
                - Use **Tools & Guides** to access official documentation.
                """
            )


    with b2:

        with st.popover("📄 AI Capability Guide", use_container_width=True):

            st.markdown("**AI Capability Guide**")

            st.markdown(
                """
                This board maps six pathways, from AI fundamentals through to
                agentic systems, RAG & data, governance and simulation.

                Start at **Fundamentals** if you're new to AI, or jump directly
                to the pathway that matches what you're building.
                """
            )


    with b3:

        with st.popover("💬 Share feedback", use_container_width=True):

            st.markdown("**Tell us what's working — or not**")

            fb = st.text_area(
                "Your feedback",
                label_visibility="collapsed",
                placeholder="What would make this board more useful?",
                key="fb_text",
            )

            if st.button("Submit feedback", key="fb_submit"):

                st.session_state.feedback_sent = True

            if st.session_state.feedback_sent:

                st.success(
                    "Thanks — your feedback has been noted for this session."
                )


st.write("")


# ============================================================================
# TRACK DETAIL PAGE
# ============================================================================

def render_track_page(key):

    track = TRACKS[key]

    st.markdown(
        '<div class="back-marker"></div>',
        unsafe_allow_html=True,
    )

    st.button(
        "← Back to Capability Map",
        key="back_to_map",
        on_click=go_page,
        args=("capability_map",),
    )

    st.markdown(
        f"""
        <div class="track-hero" style="background:{track['bg']};">

            <div class="track-hero-icon">
                {track['icon']}
            </div>

            <div>

                <p class="track-hero-title" style="color:{track['color']};">
                    {track['name']} Track
                </p>

                <p class="track-hero-sub" style="color:{track['color']};">
                    {len(track['courses'])} capabilities in this pathway
                </p>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(4)

    for i, (title, desc, duration) in enumerate(track["courses"]):

        with cols[i % 4]:

            st.markdown(
                f"""
                <div class="course-card">

                    <div>

                        <div
                            class="course-number"
                            style="
                                background:{track['color']}1a;
                                color:{track['color']};
                            "
                        >
                            {i + 1:02d}
                        </div>

                        <div class="course-title">
                            {title}
                        </div>

                        <div class="course-desc">
                            {desc}
                        </div>

                    </div>

                    <div class="course-meta">
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
# HOME PAGE
# ============================================================================

def render_home():

    main_col, right_col = st.columns(
        [3, 1],
        gap="large",
    )


    # ------------------------------------------------------------------------
    # MAIN CONTENT
    # ------------------------------------------------------------------------

    with main_col:

        # ---------------- PATHWAYS ----------------

        st.markdown(
            '<div class="section-title">Choose your learning pathway</div>',
            unsafe_allow_html=True,
        )

        pathway_cols = st.columns(3)

        for i, (key, track) in enumerate(TRACKS.items()):

            with pathway_cols[i % 3]:

                st.markdown(
                    f"""
                    <div
                        class="pathway-card"
                        style="
                            background:{track['bg']};
                            border-color:{track['color']}44;
                        "
                    >

                        <div class="pathway-icon">
                            {track['icon']}
                        </div>

                        <div
                            class="pathway-title"
                            style="color:{track['color']};"
                        >
                            {track['name']}
                        </div>

                        <div class="pathway-meta">
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
                    on_click=go_page,
                    args=(key,),
                )


        st.write("")


        # ---------------- JOURNEY ----------------

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
                [
                    "AI & LLM Fundamentals",
                    "Prompt Engineering",
                    "Responsible AI",
                    "Governance Basics",
                ],
            ),

            (
                "🛠️",
                "PRACTITIONER",
                "Apply & build",
                "#e8781f",
                [
                    "Work with GPT-4/4.1/5",
                    "Claude 3.x & Gemini",
                    "Multi-Modal AI",
                    "GitHub Copilot",
                ],
            ),

            (
                "</>",
                "ADVANCED BUILDERS",
                "Design & integrate",
                "#8b5cf6",
                [
                    "Azure AI Search",
                    "Vector Databases",
                    "Redis (Memory Cache)",
                    "LangChain",
                ],
            ),

            (
                "🕸️",
                "AGENTIC AI",
                "Orchestrate & scale",
                "#2f9e5c",
                [
                    "MCP & Tool Abstraction",
                    "Copilot Studio",
                    "Agent Frameworks",
                    "LangGraph",
                ],
            ),

            (
                "🛡️",
                "ENTERPRISE DEPLOYMENT",
                "Secure & govern",
                "#e0373f",
                [
                    "Security & Guardrails",
                    "Auditing & Monitoring",
                    "Compliance",
                    "Decision Guardrails",
                ],
            ),

            (
                "🚀",
                "INNOVATION LAB",
                "Simulate & explore",
                "#12163a",
                [
                    "Synthetic Data Generation",
                    "Digital Twins",
                    "Mistral & LLAMA",
                    "Simulation & Sandbox",
                ],
            ),

        ]

        st.markdown(
            '<div class="journey-wrap">',
            unsafe_allow_html=True,
        )

        journey_cols = st.columns(6)

        for col, (icon, title, subtitle, color, items) in zip(
            journey_cols,
            stages,
        ):

            with col:

                st.markdown(
                    f"""
                    <div class="journey-stage">

                        <div
                            class="journey-circle"
                            style="
                                border-color:{color};
                                color:{color};
                            "
                        >
                            {icon}
                        </div>

                        <div
                            class="journey-stage-title"
                            style="color:{color};"
                        >
                            {title}
                        </div>

                        <div class="journey-stage-sub">
                            {subtitle}
                        </div>

                        <ul class="journey-list">

                            {''.join(
                                f'<li>{item}</li>'
                                for item in items
                            )}

                        </ul>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                track_key = STAGE_TO_TRACK[title]

                st.button(
                    "View pathway →",
                    key=f"stage_{track_key}",
                    use_container_width=True,
                    on_click=go_page,
                    args=(track_key,),
                )

        st.markdown(
            '</div>',
            unsafe_allow_html=True,
        )


        # ---------------- HOW YOU LEARN ----------------

        st.markdown(
            '<div class="section-title">How you learn</div>',
            unsafe_allow_html=True,
        )

        steps = [

            (
                "📖",
                "1. LEARN",
                "Self-paced content",
            ),

            (
                "👥",
                "2. WORKSHOP",
                "Instructor-led session",
            ),

            (
                "🧪",
                "3. SANDBOX LAB",
                "Guided hands-on practice",
            ),

            (
                "⚙️",
                "4. BUILD",
                "Mini project or use case",
            ),

            (
                "📊",
                "5. SHOWCASE",
                "Demo to the community",
            ),

        ]

        step_cols = st.columns(5)

        for col, (icon, title, subtitle) in zip(
            step_cols,
            steps,
        ):

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

                        <div class="step-sub">
                            {subtitle}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )


        # ---------------- FOOTER CTA ----------------

        st.markdown(
            """
            <div class="footer-banner">

                <div style="font-size:22px;">
                    🌱
                </div>

                <div>

                    <div
                        style="
                            font-weight:800;
                            color:#12163a;
                        "
                    >
                        New to AI? Start with Fundamentals.
                    </div>

                    <div
                        style="
                            color:#6b7086;
                            font-size:12.5px;
                            margin-top:3px;
                        "
                    >
                        Build your foundation before progressing into
                        advanced AI capabilities.
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    # ------------------------------------------------------------------------
    # RIGHT SIDEBAR CONTENT
    # ------------------------------------------------------------------------

    with right_col:

        st.markdown(
            '<div class="section-title" style="font-size:15px;">Tools We Work With</div>',
            unsafe_allow_html=True,
        )

        tool_cols = st.columns(2)

        for i, (name, (icon, url)) in enumerate(
            TOOL_LINKS.items()
        ):

            with tool_cols[i % 2]:

                st.markdown(
                    f"""
                    <a
                        class="tool-chip"
                        href="{url}"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        {icon}
                        {name}
                        <span class="tool-arrow">↗</span>
                    </a>
                    """,
                    unsafe_allow_html=True,
                )


        st.write("")


        st.markdown(
            '<div class="section-title" style="font-size:15px;">Quick Links</div>',
            unsafe_allow_html=True,
        )

        quick_links = [

            ("🧪", "Sandbox Labs", "labs"),
            ("🗓️", "Workshops & Events", "events"),
            ("📰", "Blog & Articles", "blog"),
            ("❓", "Help & Support", "help"),

        ]

        for icon, label, page_key in quick_links:

            st.button(
                f"{icon}  {label}",
                key=f"quick_{page_key}",
                use_container_width=True,
                on_click=go_page,
                args=(page_key,),
            )


# ============================================================================
# CAPABILITY MAP PAGE
# ============================================================================

def render_capability_map():

    st.markdown(
        '<div class="page-title">AI Capability Map</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-subtitle">
            Explore the full AI capability landscape and find the pathway
            that matches your role and development goals.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    for key, track in TRACKS.items():

        st.markdown(
            f"""
            <div
                class="white-card"
                style="
                    border-left:5px solid {track['color']};
                    margin-bottom:12px;
                "
            >

                <div
                    style="
                        display:flex;
                        align-items:center;
                        gap:14px;
                    "
                >

                    <div style="font-size:30px;">
                        {track['icon']}
                    </div>

                    <div>

                        <div
                            style="
                                font-size:18px;
                                font-weight:800;
                                color:{track['color']};
                            "
                        >
                            {track['name']}
                        </div>

                        <div
                            style="
                                font-size:12px;
                                color:#6b7086;
                            "
                        >
                            {len(track['courses'])} capabilities
                        </div>

                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        course_cols = st.columns(4)

        for i, (title, desc, duration) in enumerate(
            track["courses"]
        ):

            with course_cols[i % 4]:

                st.markdown(
                    f"""
                    <div class="course-card">

                        <div>

                            <div class="course-title">
                                {title}
                            </div>

                            <div class="course-desc">
                                {desc}
                            </div>

                        </div>

                        <div class="course-meta">
                            ⏱ {duration}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        st.write("")


# ============================================================================
# SANDBOX LABS PAGE
# ============================================================================

def render_labs():

    st.markdown(
        '<div class="page-title">Sandbox Labs</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-subtitle">
            Experiment safely, build prototypes and practise AI capabilities
            through hands-on exercises.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    labs = [

        (
            "🧠",
            "RAG Lab",
            "Build a company knowledge assistant using documents and enterprise search.",
            "Intermediate",
            "2–4 hours",
            "#eaf1ff",
            "#2f6fed",
        ),

        (
            "🤖",
            "Agent Builder Lab",
            "Create your first AI agent and connect it to tools and business processes.",
            "Intermediate",
            "2–4 hours",
            "#e9f8ee",
            "#2f9e5c",
        ),

        (
            "🌊",
            "Prompt Flow Lab",
            "Test, evaluate and improve prompts using structured experimentation.",
            "Practitioner",
            "2–3 hours",
            "#f2edfe",
            "#8b5cf6",
        ),

        (
            "📊",
            "Synthetic Data Lab",
            "Generate realistic synthetic datasets for testing AI and analytics use cases.",
            "Advanced",
            "3–4 hours",
            "#fef1e6",
            "#e8781f",
        ),

        (
            "🕸️",
            "Multi-Agent Lab",
            "Build a workflow where multiple agents collaborate to complete a task.",
            "Advanced",
            "4–6 hours",
            "#e9f8ee",
            "#2f9e5c",
        ),

        (
            "🛡️",
            "Responsible AI Lab",
            "Explore guardrails, monitoring and safe AI deployment scenarios.",
            "All levels",
            "2 hours",
            "#fdecec",
            "#e0373f",
        ),

    ]

    lab_cols = st.columns(3)

    for i, (
        icon,
        title,
        desc,
        level,
        duration,
        bg,
        color,
    ) in enumerate(labs):

        with lab_cols[i % 3]:

            st.markdown(
                f"""
                <div
                    class="lab-card"
                    style="background:{bg}; margin-bottom:14px;"
                >

                    <div>

                        <div
                            style="
                                font-size:28px;
                                margin-bottom:10px;
                            "
                        >
                            {icon}
                        </div>

                        <div
                            class="lab-title"
                            style="color:{color};"
                        >
                            {title}
                        </div>

                        <div class="lab-desc">
                            {desc}
                        </div>

                    </div>

                    <div
                        style="
                            font-size:11px;
                            color:#6b7086;
                        "
                    >
                        <b>{level}</b>
                        &nbsp; · &nbsp;
                        {duration}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.button(
                "Start Lab →",
                key=f"lab_{i}",
                use_container_width=True,
            )


# ============================================================================
# WORKSHOPS & EVENTS PAGE
# ============================================================================

def render_events():

    st.markdown(
        '<div class="page-title">Workshops & Events</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-subtitle">
            Learn from experts, build together and discover what is happening
            across the OA AI community.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    events = [

        (
            "📅",
            "Intro to Prompt Engineering for Consultants",
            "Learn how to write effective prompts for analysis, research and consulting workflows.",
            "22 May 2025",
            "Beginner",
            "#eaf1ff",
            "#2f6fed",
        ),

        (
            "📗",
            "Building with RAG on Azure AI Search",
            "Build a knowledge assistant using enterprise documents and retrieval-augmented generation.",
            "29 May 2025",
            "Practitioner",
            "#e9f8ee",
            "#2f9e5c",
        ),

        (
            "📘",
            "Multi-Agent Orchestration with LangGraph",
            "Explore how multiple agents can collaborate on complex business processes.",
            "5 June 2025",
            "Advanced",
            "#f2edfe",
            "#8b5cf6",
        ),

        (
            "🛡️",
            "Responsible AI in Practice",
            "Understand how to design safe, governed and trustworthy AI solutions.",
            "12 June 2025",
            "All levels",
            "#fdecec",
            "#e0373f",
        ),

    ]

    for i, (
        icon,
        title,
        desc,
        date,
        level,
        bg,
        color,
    ) in enumerate(events):

        st.markdown(
            f"""
            <div
                class="event-card"
                style="margin-bottom:10px;"
            >

                <div
                    style="
                        display:flex;
                        align-items:flex-start;
                        gap:16px;
                    "
                >

                    <div
                        style="
                            background:{bg};
                            color:{color};
                            border-radius:10px;
                            padding:12px;
                            font-size:22px;
                        "
                    >
                        {icon}
                    </div>

                    <div style="flex:1;">

                        <div
                            style="
                                font-size:16px;
                                font-weight:800;
                                color:#12163a;
                            "
                        >
                            {title}
                        </div>

                        <div
                            style="
                                font-size:13px;
                                color:#6b7086;
                                margin-top:5px;
                            "
                        >
                            {desc}
                        </div>

                        <div
                            style="
                                margin-top:10px;
                                font-size:11px;
                                color:{color};
                                font-weight:700;
                            "
                        >
                            {level}
                        </div>

                    </div>

                    <div
                        style="
                            font-size:12px;
                            color:#6b7086;
                            white-space:nowrap;
                        "
                    >
                        {date}
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.button(
            "View event details →",
            key=f"event_{i}",
        )


# ============================================================================
# BLOG PAGE
# ============================================================================

def render_blog():

    st.markdown(
        '<div class="page-title">Blog & Articles</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-subtitle">
            Ideas, insights and practical guidance from the OA AI community.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    articles = [

        (
            "🧠",
            "What is Agentic AI?",
            "Understand how AI agents differ from traditional chatbots and automation.",
            "AI Fundamentals",
            "8 min read",
            "#eaf1ff",
            "#2f6fed",
        ),

        (
            "🔍",
            "Why Retrieval-Augmented Generation Matters",
            "How RAG helps enterprise AI systems work with trusted organisational knowledge.",
            "RAG & Data",
            "10 min read",
            "#f2edfe",
            "#8b5cf6",
        ),

        (
            "🛡️",
            "Building Responsible AI Systems",
            "The practical principles behind safe, governed and trustworthy AI.",
            "Responsible AI",
            "7 min read",
            "#fdecec",
            "#e0373f",
        ),

        (
            "🚀",
            "From AI Experiment to Enterprise Capability",
            "What it takes to move from a prototype to a production AI solution.",
            "Enterprise AI",
            "12 min read",
            "#e9f8ee",
            "#2f9e5c",
        ),

    ]

    article_cols = st.columns(2)

    for i, (
        icon,
        title,
        desc,
        category,
        duration,
        bg,
        color,
    ) in enumerate(articles):

        with article_cols[i % 2]:

            st.markdown(
                f"""
                <div
                    class="article-card"
                    style="margin-bottom:14px;"
                >

                    <div
                        style="
                            background:{bg};
                            border-radius:10px;
                            padding:18px;
                            font-size:30px;
                            margin-bottom:14px;
                        "
                    >
                        {icon}
                    </div>

                    <div
                        style="
                            font-size:11px;
                            color:{color};
                            font-weight:700;
                            text-transform:uppercase;
                        "
                    >
                        {category}
                    </div>

                    <div
                        style="
                            font-size:17px;
                            font-weight:800;
                            color:#12163a;
                            margin-top:6px;
                        "
                    >
                        {title}
                    </div>

                    <div
                        style="
                            font-size:13px;
                            color:#6b7086;
                            margin-top:6px;
                            line-height:1.5;
                        "
                    >
                        {desc}
                    </div>

                    <div
                        style="
                            font-size:11px;
                            color:#8b8fa8;
                            margin-top:12px;
                        "
                    >
                        {duration}
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
# TEAMS CALENDAR PAGE
# ============================================================================

def render_calendar():

    st.markdown(
        '<div class="page-title">Teams Calendar</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-subtitle">
            Access invite-only AI sessions, private workshops and internal
            community events.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    st.markdown(
        """
        <div
            class="white-card"
            style="
                text-align:center;
                padding:55px 30px;
            "
        >

            <div style="font-size:48px;">
                🔒
            </div>

            <div
                style="
                    font-size:21px;
                    font-weight:800;
                    color:#12163a;
                    margin-top:15px;
                "
            >
                Invite-only calendar
            </div>

            <div
                style="
                    max-width:550px;
                    margin:10px auto;
                    font-size:14px;
                    color:#6b7086;
                    line-height:1.6;
                "
            >
                This calendar contains private Teams meetings, invite-only
                workshops and internal AI community events.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:

        st.button(
            "Request calendar access →",
            use_container_width=True,
        )


# ============================================================================
# HELP & SUPPORT PAGE
# ============================================================================

def render_help():

    st.markdown(
        '<div class="page-title">Help & Support</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-subtitle">
            Find answers, troubleshoot issues and get help with your AI
            learning journey.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    st.markdown(
        '<div class="section-title">Frequently Asked Questions</div>',
        unsafe_allow_html=True,
    )

    faqs = {

        "Where should I start?":
            "Start with the Fundamentals pathway if you are new to AI. If you already have experience, use the Capability Map to find the most relevant pathway.",

        "How do I access a Sandbox Lab?":
            "Select a lab from the Sandbox Labs page and follow the access instructions. Some environments may require additional permissions.",

        "How do I join a workshop?":
            "Visit Workshops & Events and select the session you are interested in. Some sessions require registration.",

        "Who can I contact about AI capability development?":
            "Contact the OA AI Team or ask a question in the AI Community channel.",

        "I need access to a tool or platform.":
            "Submit an access request through the appropriate internal IT or platform support process.",

    }

    for question, answer in faqs.items():

        with st.expander(question):

            st.write(answer)

    st.write("")

    st.markdown(
        '<div class="section-title">Still need help?</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="white-card">

                <div style="font-size:24px;">
                    💬
                </div>

                <div
                    style="
                        font-size:16px;
                        font-weight:800;
                        margin-top:8px;
                    "
                >
                    Ask the Community
                </div>

                <div
                    style="
                        font-size:12px;
                        color:#6b7086;
                        margin-top:5px;
                    "
                >
                    Get advice from colleagues working with AI across OA.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
            <div class="white-card">

                <div style="font-size:24px;">
                    🛠️
                </div>

                <div
                    style="
                        font-size:16px;
                        font-weight:800;
                        margin-top:8px;
                    "
                >
                    Technical Support
                </div>

                <div
                    style="
                        font-size:12px;
                        color:#6b7086;
                        margin-top:5px;
                    "
                >
                    Get help with access, environments and AI tooling.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


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

elif st.session_state.page in TRACKS:

    render_track_page(st.session_state.page)