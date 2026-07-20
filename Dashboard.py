import streamlit as st

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
        "icon": "🏆", "name": "Fundamentals", "color": "#2f6fed", "bg": "#eaf1ff",
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
        "icon": "🕸️", "name": "Agentic AI", "color": "#2f9e5c", "bg": "#e9f8ee",
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
        "icon": "💠", "name": "RAG & Data", "color": "#8b5cf6", "bg": "#f2edfe",
        "courses": [
            ("Azure AI Search", "Index and retrieve enterprise content with Azure AI Search.", "2 hrs"),
            ("Vector Databases", "Understand embeddings and vector search for retrieval.", "2 hrs"),
            ("Redis (Memory Cache)", "Use Redis for fast agent memory and caching.", "1.5 hrs"),
            ("LangChain", "Build retrieval-augmented pipelines using LangChain.", "2.5 hrs"),
            ("Embedding Strategies", "Choose the right embedding model and chunking strategy.", "1.5 hrs"),
        ],
    },
    "llm_promptops": {
        "icon": "💡", "name": "LLM & Prompt Ops", "color": "#e8781f", "bg": "#fef1e6",
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
        "icon": "🛡️", "name": "Governance & Responsible AI", "color": "#e0373f", "bg": "#fdecec",
        "courses": [
            ("Security & Guardrails", "Put technical guardrails around AI systems in production.", "2 hrs"),
            ("Auditing & Monitoring", "Track AI decisions and outputs for accountability.", "1.5 hrs"),
            ("Compliance", "Navigate regulatory requirements for enterprise AI.", "1.5 hrs"),
            ("Decision Guardrails", "Design approval and escalation paths for high-stakes AI decisions.", "1 hr"),
        ],
    },
    "simulation": {
        "icon": "🚀", "name": "Simulation & Innovation", "color": "#12163a", "bg": "#eceef5",
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

# Tool -> official documentation link
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
# STATE
# ============================================================================
if "page" not in st.session_state:
    st.session_state.page = "home"
if "feedback_sent" not in st.session_state:
    st.session_state.feedback_sent = False


def go_home():
    st.session_state.page = "home"


def go_track(key):
    st.session_state.page = key


# ============================================================================
# GLOBAL CSS
# ============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"]  { font-family: 'Inter', sans-serif; }
    * { box-sizing: border-box; }

    .main { background-color: #f3f5f9; }
    .block-container { padding-top: 3rem; padding-bottom: 2rem; max-width: 1500px; }

    p, div, span, li, a { overflow-wrap: break-word; word-break: break-word; }

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"] { background-color: #131a3a; }
    section[data-testid="stSidebar"] * { color: #d7dbf0 !important; }
    .sidebar-logo {
        display: flex; align-items: center; gap: 10px;
        padding: 4px 0 20px 0; font-weight: 800; font-size: 16.5px; color: white !important;
        line-height: 1.3;
    }
    .sidebar-logo .logo-icon { font-size: 24px; flex-shrink: 0; }
    .nav-item {
        display: flex; align-items: center; gap: 12px;
        padding: 9px 12px; border-radius: 8px; margin-bottom: 2px;
        font-size: 13.8px; font-weight: 500; color: #c7cbe6; line-height: 1.3;
    }
    .nav-item.active { background-color: #2b3570; color: white !important; font-weight: 600; }
    .quote-box {
        background-color: #1c2450; border-radius: 10px; padding: 16px 16px 12px 16px;
        margin-top: 22px; font-size: 12.5px; line-height: 1.55; color: #b8bde0;
    }
    .quote-attr { margin-top: 10px; font-weight: 700; color: #7f8ad4 !important; }

    /* ---------- Header ---------- */
    .page-title {
        font-size: 28px; font-weight: 800; color: #101433;
        margin: 0; line-height: 1.45; padding-top: 2px; overflow: visible;
    }
    .page-subtitle { color: #6b7086; font-size: 14px; margin-top: 3px; line-height: 1.4; overflow: visible; }

    div[data-testid="stButton"] > button {
        border-radius: 8px; font-weight: 600; font-size: 13px;
        border: 1px solid #d7dae3; background-color: white; color: #2c3050;
        padding: 8px 12px; white-space: normal; line-height: 1.3; min-height: 40px;
    }
    div[data-testid="stButton"] > button:hover { border-color: #2f6fed; color: #2f6fed; }
    div[data-testid="stPopover"] > button {
        border-radius: 8px; font-weight: 600; font-size: 13px;
        border: 1px solid #d7dae3; background-color: white; color: #2c3050;
        padding: 8px 12px; white-space: normal; line-height: 1.3; min-height: 40px;
    }
    .purple-btn button { background-color: #5b3df0 !important; color: white !important; border: none !important; }

    /* ---------- Section headers ---------- */
    .section-title { font-size: 18px; font-weight: 800; color: #12163a; margin: 6px 0 12px 0; line-height: 1.3; }
    .section-title-row { display: flex; align-items: center; justify-content: space-between; margin: 6px 0 12px 0; }
    .section-link { font-size: 12.5px; font-weight: 700; color: #2f6fed; text-decoration: none; white-space: nowrap; }

    /* ---------- Track cards (clickable pathway buttons) ---------- */
    div[data-testid="stButton"] > button.track-btn,
    .track-marker + div[data-testid="stButton"] button {
        width: 100%; min-height: 96px; border-radius: 12px; text-align: left;
        padding: 14px 14px; font-weight: 700; font-size: 14px;
        display: flex; align-items: flex-start; white-space: normal;
    }
    .track-caption { font-size: 12px; color: #6b7086; margin: -8px 2px 14px 2px; line-height: 1.4; }
    .track-caption b { color: #12163a; }

    /* ---------- Journey ---------- */
    .journey-wrap {
        background: white; border-radius: 14px; padding: 26px 24px 18px 24px;
        border: 1px solid #e7e9f2; margin-bottom: 24px;
    }
    .journey-circle {
        width: 68px; height: 68px; border-radius: 50%; border: 3px solid;
        display: flex; align-items: center; justify-content: center;
        font-size: 24px; margin: 0 auto 10px auto; background: white;
    }
    .journey-stage-title {
        text-align: center; font-weight: 800; font-size: 12.5px;
        letter-spacing: 0.2px; color: #12163a; line-height: 1.3; padding: 0 2px;
    }
    .journey-stage-sub { text-align: center; font-size: 11.5px; color: #6b7086; margin-bottom: 12px; }
    .journey-list { list-style: none; padding-left: 0; margin: 0; font-size: 12.3px; color: #33364f; line-height: 1.4; }
    .journey-list li { padding: 5px 2px; border-bottom: 1px dashed #eef0f6; }
    .journey-list li:before { content: "•  "; }

    /* ---------- How you learn ---------- */
    .step-card {
        background: white; border-radius: 12px; border: 1px solid #e7e9f2;
        padding: 14px 10px; text-align: center; min-height: 108px;
        display: flex; flex-direction: column; justify-content: center;
    }
    .step-icon { font-size: 20px; margin-bottom: 6px; }
    .step-title { font-weight: 700; font-size: 12px; color: #12163a; line-height: 1.3; }
    .step-sub { font-size: 11px; color: #6b7086; margin-top: 3px; line-height: 1.3; }

    /* ---------- Generic white card ---------- */
    .white-card { background: white; border-radius: 14px; border: 1px solid #e7e9f2; padding: 16px 18px; height: 100%; }

    .event-row { display: flex; align-items: flex-start; gap: 12px; padding: 10px 0; border-bottom: 1px solid #f0f1f6; }
    .event-icon {
        width: 32px; height: 32px; border-radius: 8px; display: flex;
        align-items: center; justify-content: center; font-size: 14px; flex-shrink: 0;
    }
    .event-title { font-weight: 600; font-size: 13px; color: #16193b; line-height: 1.35; }
    .event-date { font-size: 11px; color: #6b7086; white-space: nowrap; flex-shrink: 0; }
    .badge { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; margin-top: 4px; }

    .lab-card {
        border-radius: 12px; padding: 15px; min-height: 140px;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .lab-title { font-weight: 700; font-size: 13.5px; margin-bottom: 4px; line-height: 1.3; }
    .lab-desc { font-size: 11.5px; color: #454868; line-height: 1.4; }

    /* Tool chips are now real links */
    a.tool-chip {
        display: flex; align-items: center; gap: 7px; background: #f7f8fb;
        border: 1px solid #edeef4; border-radius: 8px; padding: 8px 9px;
        font-size: 11.5px; font-weight: 600; color: #23264a !important; margin-bottom: 8px; line-height: 1.25;
        text-decoration: none; transition: all 0.15s ease;
    }
    a.tool-chip:hover { border-color: #2f6fed; background: #eaf1ff; color: #2f6fed !important; }
    a.tool-chip .chip-arrow { margin-left: auto; opacity: 0.45; font-size: 10px; }
    a.tool-chip:hover .chip-arrow { opacity: 1; }

    .qlink { font-size: 12.5px; font-weight: 600; color: #23264a; padding: 6px 0; line-height: 1.3; }

    .footer-banner {
        background: #eef1fb; border-radius: 12px; padding: 14px 20px;
        display: flex; align-items: center; gap: 14px; margin-top: 20px;
    }

    /* ---------- Track detail page ---------- */
    .track-hero {
        border-radius: 14px; padding: 24px; margin-bottom: 22px;
        display: flex; align-items: center; gap: 16px;
    }
    .track-hero-icon {
        width: 56px; height: 56px; border-radius: 14px; background: white;
        display: flex; align-items: center; justify-content: center; font-size: 26px; flex-shrink: 0;
    }
    .track-hero-title { font-size: 24px; font-weight: 800; margin: 0; line-height: 1.2; }
    .track-hero-sub { font-size: 13.5px; margin-top: 3px; opacity: 0.85; }

    .course-card {
        background: white; border-radius: 12px; border: 1px solid #e7e9f2;
        padding: 16px; min-height: 168px; display: flex; flex-direction: column; justify-content: space-between;
        transition: box-shadow 0.15s ease;
    }
    .course-card:hover { box-shadow: 0 4px 14px rgba(18,22,58,0.08); }
    .course-number {
        width: 26px; height: 26px; border-radius: 7px; display: flex;
        align-items: center; justify-content: center; font-size: 12px; font-weight: 800; margin-bottom: 8px;
    }
    .course-title { font-weight: 700; font-size: 14px; color: #12163a; margin-bottom: 5px; line-height: 1.35; }
    .course-desc { font-size: 12px; color: #5c6079; line-height: 1.45; margin-bottom: 10px; }
    .course-meta { font-size: 11px; color: #8b8fa8; font-weight: 600; }

    .back-marker + div[data-testid="stButton"] button {
        border: none; background: transparent; color: #2f6fed; font-weight: 700;
        font-size: 13.5px; padding: 4px 0; min-height: unset;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-logo">'
        '<span class="logo-icon">🔷</span>'
        '<span>OA AI Capability Journey</span>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown("""
    <style>

    div[data-testid="stButton"] button {
        width:100%;
        border:none !important;
        text-align:left;
        background:transparent !important;
        padding:10px 12px !important;
        font-size:15px !important;
        font-weight:600 !important;
        color:#12163a !important;
        border-radius:8px !important;
    }

    div[data-testid="stButton"] button p {
        color:#12163a !important;
    }

    div[data-testid="stButton"] button:hover {
        background:#eef2ff !important;
        color:#12163a !important;
    }

    </style>
    """, unsafe_allow_html=True)


    nav_items = [
        ("🏠", "Home", "home"),
        ("📚", "Capability Survey", "capability_survey"),
        ("🗓️", "Workshops & Events", "workshops"),
        ("🧪", "Sandbox Labs", "sandbox"),
    ]


    for icon, label, page_key in nav_items:

        if st.button(
            f"{icon}  {label}",
            key=f"nav_{page_key}",
            use_container_width=True
        ):
            st.session_state.page = page_key
            st.rerun()
# ============================================================================
# HEADER (shared)
# ============================================================================
h1, h2 = st.columns([3, 2])
with h1:
    st.markdown('<div class="page-title">OA AI Capability Journey</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Learn. Build. Apply. Lead.</div>', unsafe_allow_html=True)
with h2:
    b1, b2, b3 = st.columns(3, gap="medium")

    with b1:
        with st.popover("How to use this board", use_container_width=True):
            st.markdown("## How to use this board")
            st.markdown("""
            **Getting around the board**
            - Pick a **pathway** to see every course in that track.
            - Follow the **Journey** left to right — each stage builds on the last.
            - Use the learning loop:
            **Learn → Workshop → Sandbox → Build → Showcase → Badge**
            - Explore **Sandbox Labs** for hands-on practice.
            - Use **Tools We Work With** for official documentation.
            """)
    with b2:
        with st.popover("AI Capability Guide", use_container_width=True):
            st.markdown("## AI Capability Guide")

            st.markdown("""
            This board maps six AI capability pathways:
            - AI Fundamentals
            - Generative AI
            - Agentic Systems
            - RAG & Data
            - Governance
            - Simulation
            Start with Fundamentals if you are new,
            or jump directly to the pathway that matches your project.
            """)
    with b3:
        with st.popover("Share feedback", use_container_width=True):
            st.markdown("## Share feedback")
            st.markdown("""
            Help us improve the board.
            Tell us:
            - What works well
            - What is unclear
            - What content is missing
            - What would improve your experience
            """)
            fb = st.text_area(
                "Your feedback",
                placeholder="What would make this board more useful?",
                label_visibility="collapsed",
                key="fb_text"
            )
            if st.button("Submit feedback", key="fb_submit"):
                st.success("Thanks — your feedback has been noted.")
    st.markdown("""
    <style>
    div[data-testid="stPopover"] button {
        height: 70px;
        font-size: 20px;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)
st.write("")

# ============================================================================
# TRACK DETAIL PAGE
# ============================================================================
def render_track_page(key):
    t = TRACKS[key]
    st.markdown('<div class="back-marker"></div>', unsafe_allow_html=True)
    st.button("← Back to all pathways", key="back_btn", on_click=go_home)

    st.markdown(f"""
    <div class="track-hero" style="background:{t['bg']};">
        <div class="track-hero-icon">{t['icon']}</div>
        <div>
            <p class="track-hero-title" style="color:{t['color']};">{t['name']} Track</p>
            <p class="track-hero-sub" style="color:{t['color']};">{len(t['courses'])} capabilities in this pathway</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(4)
    for i, (title, desc, duration) in enumerate(t["courses"]):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="course-card">
                <div>
                    <div class="course-number" style="background:{t['color']}1a; color:{t['color']};">{i + 1:02d}</div>
                    <div class="course-title">{title}</div>
                    <div class="course-desc">{desc}</div>
                </div>
                <div class="course-meta">⏱ {duration}</div>
            </div>
            """, unsafe_allow_html=True)
            st.button("Start course →", key=f"course_{key}_{i}", use_container_width=True)
            st.write("")


# ============================================================================
# HOME PAGE
# ============================================================================
def render_home():
    main_col, right_col = st.columns([3, 1], gap="large")

    with main_col:
        st.markdown('<div class="section-title">Choose your learning pathway</div>', unsafe_allow_html=True)
        cols = st.columns(6)
        for col, key in zip(cols, TRACKS.keys()):
            t = TRACKS[key]
            with col:
                st.markdown(
                    f"<style>div[data-testid='column']:has(#marker-track-{key}) "
                    f"div[data-testid='stButton'] button {{"
                    f"background:{t['bg']} !important; color:{t['color']} !important;"
                    f"border:1.5px solid {t['color']}44 !important; width:100%; min-height:96px; "
                    f"border-radius:12px; text-align:left; padding:14px; font-weight:700; "
                    f"font-size:14px; display:flex; align-items:flex-start; white-space:normal;}}</style>"
                    f"<span id='marker-track-{key}'></span>",
                    unsafe_allow_html=True,
                )
                st.button(f"{t['icon']}  {t['name']}", key=f"track_{key}",
                          use_container_width=True, on_click=go_track, args=(key,))
                st.markdown(
                    f'<div class="track-caption">Track · <b>{len(t["courses"])} Capabilities</b></div>',
                    unsafe_allow_html=True,
                )

        st.write("")
        st.markdown('<div class="section-title">Your AI Capability Journey</div>', unsafe_allow_html=True)

        stages = [
            ("🌱", "FOUNDATION", "Build your basics", "#2f6fed",
             ["AI & LLM Fundamentals", "Prompt Engineering", "Responsible AI", "Governance Basics"]),
            ("🛠️", "PRACTITIONER", "Apply & build", "#e8781f",
             ["Work with GPT-4/4.1/5", "Claude 3.x & Gemini", "Multi-Modal AI", "GitHub Copilot"]),
            ("🏗️", "ADVANCED BUILDERS", "Design & integrate", "#8b5cf6",
             ["Azure AI Search", "Vector Databases", "Redis (Memory Cache)", "LangChain"]),
            ("🕸️", "AGENTIC AI", "Orchestrate & scale", "#2f9e5c",
             ["MCP & Tool Abstraction", "Copilot Studio", "Agent Frameworks", "LangGraph"]),
            ("🛡️", "ENTERPRISE DEPLOYMENT", "Secure & govern", "#e0373f",
             ["Security & Guardrails", "Auditing & Monitoring", "Compliance", "Decision Guardrails"]),
            ("🚀", "INNOVATION LAB", "Simulate & explore", "#12163a",
             ["Synthetic Data Generation", "Digital Twins (Unreal Engine)", "Mistral & LLAMA", "Simulation & Sandbox"]),
        ]

        circ_cols = st.columns(6)
        for col, (icon, title, sub, color, items) in zip(circ_cols, stages):
            with col:
                st.markdown(f"""
                    <div class="journey-circle" style="border-color:{color}; color:{color};">{icon}</div>
                    <div class="journey-stage-title" style="color:{color};">{title}</div>
                    <div class="journey-stage-sub">{sub}</div>
                    <ul class="journey-list">{''.join(f'<li>{i}</li>' for i in items)}</ul>
                """, unsafe_allow_html=True)
                track_key = STAGE_TO_TRACK[title]
                st.markdown(
                    f"<style>div[data-testid='column']:has(#marker-stage-{track_key}) "
                    f"div[data-testid='stButton'] button {{"
                    f"background:transparent !important; color:{color} !important; border:none !important;"
                    f"min-height:unset !important; padding:2px 0 !important; font-size:12px !important;"
                    f"font-weight:700 !important; text-align:center !important; justify-content:center !important;}}</style>"
                    f"<span id='marker-stage-{track_key}'></span>",
                    unsafe_allow_html=True,
                )
            st.markdown('</div>', unsafe_allow_html=True)

        # ---------------- HOW YOU LEARN ----------------
        st.markdown('<div class="section-title">How you learn</div>', unsafe_allow_html=True)
        steps = [
            ("📖", "1. LEARN", "Self-paced content (1-2 hrs)"),
            ("👥", "2. WORKSHOP", "Instructor-led (2-4 hrs)"),
            ("🧪", "3. SANDBOX LAB", "Guided hands-on (2-4 hrs)"),
            ("⚙️", "4. BUILD", "Mini project / use case (½-1 day)"),
            ("📊", "5. SHOWCASE", "Demo to community (15 mins)"),
        ]
        step_cols = st.columns(5)
        for col, (icon, title, sub) in zip(step_cols, steps):
            with col:
                st.markdown(f"""
                <div class="step-card">
                    <div class="step-icon">{icon}</div>
                    <div class="step-title">{title}</div>
                    <div class="step-sub">{sub}</div>
                </div>
                """, unsafe_allow_html=True)

        st.write("")
    with right_col:
        st.markdown('<div class="section-title" style="font-size:15px;">Tools We Work With</div>', unsafe_allow_html=True)
        tc = st.columns(2)
        for i, (name, (icon, url)) in enumerate(TOOL_LINKS.items()):
            with tc[i % 2]:
                st.markdown(
                    f'<a class="tool-chip" href="{url}" target="_blank" rel="noopener noreferrer">'
                    f'{icon} {name}<span class="chip-arrow">↗</span></a>',
                    unsafe_allow_html=True,
                )
        st.write("")
        st.markdown(
            '<div class="section-title" style="font-size:15px;">Quick Links & Resources</div>',
            unsafe_allow_html=True
        )

        links = [
            ("🛠️ AI Tooling Guide", "https://learn.microsoft.com/en-us/ai/"),
            ("📚 OA AI Use Cases Library", "https://www.microsoft.com/en-us/ai"),
            ("💬 Prompt Engineering Guide", "https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering"),
            ("✅ Secure AI Checklist", "https://learn.microsoft.com/en-us/security/ai-security"),
            ("📋 Responsible AI Principles", "https://www.microsoft.com/en-us/ai/principles-and-approach"),
            ("❓ Ask the Community", "https://learn.microsoft.com/en-us/answers/topics/azure-ai.html"),
        ]

        for title, url in links:
            st.markdown(
                f'<div class="qlink"><a href="{url}" target="_blank">{title}</a></div>',
                unsafe_allow_html=True
            )

    # ---------------- EVENTS + LABS ----------------
    ev_col, lab_col = st.columns(2, gap="large")

    with ev_col:
        st.markdown(
            '<div class="section-title-row"><span class="section-title" style="margin:0;">'
            'Upcoming Workshops & Events</span><a class="section-link" href="#">View calendar →</a></div>',
            unsafe_allow_html=True,
        )
        events = [
            ("📗", "#e9f8ee", "#2f9e5c", "Building with RAG on Azure AI Search", "29 October 2026",
                ("Practitioner", "#e9f8ee", "#2f9e5c")),
            ("📘", "#f2edfe", "#8b5cf6", "Multi-Agent Orchestration with LangGraph", "5 December 2026",
                ("Advanced", "#f2edfe", "#8b5cf6")),
        ]
        rows_html = ""
        for icon, ibg, icolor, title, date, badge in events:
            badge_html = ""
            if badge:
                btxt, bbg, bcolor = badge
                badge_html = f'<span class="badge" style="background:{bbg}; color:{bcolor};">{btxt}</span>'
            rows_html += f"""
            <div class="event-row">
                <div class="event-icon" style="background:{ibg}; color:{icolor};">{icon}</div>
                <div style="flex:1;">
                    <div class="event-title">{title}</div>
                    {badge_html}
                </div>
                <div class="event-date">{date}</div>
            </div>
            """
        st.markdown(rows_html, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with lab_col:
        st.markdown(
            '<div class="section-title-row"><span class="section-title" style="margin:0;">'
            'Sandbox Labs</span><a class="section-link" href="#">Open Lab Environment →</a></div>',
            unsafe_allow_html=True,
        )
        labs = [
            ("RAG Lab", "Build a company knowledge assistant", "#eaf1ff", "#2f6fed"),
            ("Agent Builder Lab", "Create your first AI agent", "#e9f8ee", "#2f9e5c"),
            ("Prompt Flow Lab", "Test, evaluate and improve prompts", "#f2edfe", "#8b5cf6"),
            ("Synthetic Data Lab", "Generate data for AI & analytics", "#fef1e6", "#e8781f"),
        ]
        lc = st.columns(4)
        for col, (title, desc, bg, color) in zip(lc, labs):
            with col:
                st.markdown(f"""
                <div class="lab-card" style="background:{bg};">
                    <div>
                        <div class="lab-title" style="color:{color};">{title}</div>
                        <div class="lab-desc">{desc}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(
                    f"<style>div[data-testid='column']:has(#marker-lab-{title.replace(' ', '')}) "
                    f"div[data-testid='stButton'] button {{"
                    f"background:transparent !important; color:{color} !important; border:none !important;"
                    f"font-size:12px !important; font-weight:700 !important; padding:2px 0 !important; "
                    f"min-height:unset !important; text-align:left !important;}}</style>"
                    f"<span id='marker-lab-{title.replace(' ', '')}'></span>",
                    unsafe_allow_html=True,
                )
                st.button("Start Lab →", key=f"lab_{title}", use_container_width=True)

    st.write("")
    st.markdown("""
    <div class="footer-banner">
        <div style="font-size:20px;">🌱</div>
        <div>
            <a href="#" style="font-weight:700; color:#12163a; text-decoration:none;">New to AI? Start here →</a>
            &nbsp;&nbsp;<span style="color:#6b7086; font-size:12.5px;">Begin your journey with our AI Foundations path designed for everyone.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)



# ============================================================================
# ROUTER
# ============================================================================
page = st.session_state.get("page", "home")


if page == "home":
    render_home()

elif page == "capability_survey":
    render_capability_survey()

elif page == "workshops":
    render_workshops_events()

elif page == "sandbox":
    render_sandbox_labs()

elif page in TRACKS:
    render_track_page(page)
else:
    render_track_page(st.session_state.page)


# ============================================================================
# Capability survey page 
# ============================================================================
