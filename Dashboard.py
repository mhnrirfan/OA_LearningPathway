import streamlit as st

st.set_page_config(
    page_title="OA AI Capability Journey",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# GLOBAL CSS
# ----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    .main {
        background-color: #f3f5f9;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1500px;
    }

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"] {
        background-color: #131a3a;
    }
    section[data-testid="stSidebar"] * {
        color: #d7dbf0 !important;
    }
    .sidebar-logo {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 4px 0 18px 0;
        font-weight: 800;
        font-size: 20px;
        color: white !important;
    }
    .nav-item {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 10px 14px;
        border-radius: 8px;
        margin-bottom: 2px;
        font-size: 14.5px;
        font-weight: 500;
        color: #c7cbe6;
        cursor: default;
    }
    .nav-item.active {
        background-color: #2b3570;
        color: white !important;
        font-weight: 600;
    }
    .quote-box {
        background-color: #1c2450;
        border-radius: 10px;
        padding: 16px 16px 12px 16px;
        margin-top: 22px;
        font-size: 13px;
        line-height: 1.5;
        color: #b8bde0;
    }
    .quote-attr {
        margin-top: 10px;
        font-weight: 700;
        color: #7f8ad4 !important;
    }

    /* ---------- Header ---------- */
    .page-title {
        font-size: 30px;
        font-weight: 800;
        color: #101433;
        margin-bottom: 0px;
    }
    .page-subtitle {
        color: #6b7086;
        font-size: 14.5px;
        margin-top: 2px;
    }
    div[data-testid="stButton"] > button {
        border-radius: 8px;
        font-weight: 600;
        font-size: 13.5px;
        border: 1px solid #d7dae3;
        background-color: white;
        color: #2c3050;
        padding: 8px 14px;
    }
    .purple-btn button {
        background-color: #5b3df0 !important;
        color: white !important;
        border: none !important;
    }

    /* ---------- Section headers ---------- */
    .section-title {
        font-size: 19px;
        font-weight: 800;
        color: #12163a;
        margin: 6px 0 14px 0;
    }

    /* ---------- Track cards ---------- */
    .track-card {
        border-radius: 12px;
        padding: 16px 16px 14px 16px;
        border: 1.5px solid;
        height: 108px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .track-icon {
        font-size: 20px;
        margin-bottom: 6px;
    }
    .track-name {
        font-weight: 700;
        font-size: 15px;
        color: #16193b;
        margin: 0;
    }
    .track-sub {
        font-size: 12.5px;
        color: #6b7086;
        margin: 1px 0 3px 0;
    }
    .track-count {
        font-size: 12.5px;
        font-weight: 700;
        color: #16193b;
    }

    /* ---------- Journey ---------- */
    .journey-wrap {
        background: white;
        border-radius: 14px;
        padding: 26px 24px 8px 24px;
        border: 1px solid #e7e9f2;
        margin-bottom: 24px;
    }
    .journey-circle {
        width: 74px; height: 74px;
        border-radius: 50%;
        border: 3px solid;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 26px;
        margin: 0 auto 10px auto;
        background: white;
    }
    .journey-stage-title {
        text-align: center;
        font-weight: 800;
        font-size: 13.5px;
        letter-spacing: 0.3px;
        color: #12163a;
        line-height: 1.25;
    }
    .journey-stage-sub {
        text-align: center;
        font-size: 12px;
        color: #6b7086;
        margin-bottom: 14px;
    }
    .journey-list {
        list-style: none;
        padding-left: 0;
        margin: 0;
        font-size: 12.8px;
        color: #33364f;
    }
    .journey-list li {
        padding: 5px 0;
        border-bottom: 1px dashed #eef0f6;
    }
    .journey-list li:before {
        content: "•  ";
    }
    .view-all-link {
        font-size: 12.5px;
        font-weight: 700;
        margin-top: 10px;
        display: inline-block;
    }

    /* ---------- How you learn ---------- */
    .step-card {
        background: white;
        border-radius: 12px;
        border: 1px solid #e7e9f2;
        padding: 14px 12px;
        text-align: center;
        height: 118px;
    }
    .step-icon { font-size: 22px; margin-bottom: 6px; }
    .step-title { font-weight: 700; font-size: 12.5px; color: #12163a; }
    .step-sub { font-size: 11.5px; color: #6b7086; margin-top: 2px; }

    /* ---------- Generic white card ---------- */
    .white-card {
        background: white;
        border-radius: 14px;
        border: 1px solid #e7e9f2;
        padding: 18px 20px;
        height: 100%;
    }

    .event-row {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        padding: 10px 0;
        border-bottom: 1px solid #f0f1f6;
    }
    .event-icon {
        width: 34px; height: 34px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 15px;
        flex-shrink: 0;
    }
    .event-title { font-weight: 600; font-size: 13.5px; color: #16193b; }
    .event-date { font-size: 11.5px; color: #6b7086; }
    .badge {
        display: inline-block;
        font-size: 10.5px;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 10px;
        margin-top: 3px;
    }

    .lab-card {
        border-radius: 12px;
        padding: 16px;
        height: 150px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .lab-title { font-weight: 700; font-size: 14px; margin-bottom: 4px; }
    .lab-desc { font-size: 12px; color: #454868; }
    .lab-link { font-weight: 700; font-size: 12.5px; margin-top: 8px; }

    .tool-chip {
        display: flex;
        align-items: center;
        gap: 8px;
        background: #f7f8fb;
        border: 1px solid #edeef4;
        border-radius: 8px;
        padding: 8px 10px;
        font-size: 12.5px;
        font-weight: 600;
        color: #23264a;
        margin-bottom: 8px;
    }

    .qlink {
        font-size: 13px;
        font-weight: 600;
        color: #23264a;
        padding: 6px 0;
    }

    .survey-card {
        background: white;
        border-radius: 14px;
        border: 1px solid #e7e9f2;
        padding: 18px 20px;
        margin-bottom: 20px;
    }
    .survey-check { font-size: 12.5px; color: #33364f; padding: 3px 0; }

    .footer-banner {
        background: #eef1fb;
        border-radius: 12px;
        padding: 14px 20px;
        display: flex;
        align-items: center;
        gap: 14px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown('<div class="sidebar-logo">🔷 &nbsp;</div>', unsafe_allow_html=True)

    nav_items = [
        ("🏠", "Home", True),
        ("🎯", "Learning Pathways", False),
        ("🗺️", "Capability Map", False),
        ("🗓️", "Workshops & Events", False),
        ("🧪", "Sandbox Labs", False),
        ("🛠️", "Tools & Guides", False),
        ("📁", "Use Cases", False),
        ("📝", "Surveys & Feedback", False),
        ("📈", "My Progress", False),
        ("🏅", "Badges & Achievements", False),
        ("👥", "Community", False),
        ("❓", "Help & Support", False),
    ]
    for icon, label, active in nav_items:
        cls = "nav-item active" if active else "nav-item"
        st.markdown(f'<div class="{cls}">{icon} &nbsp;{label}</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="quote-box">
        "We connect AI models to our foundational tools and semantics layers —
        enabling agents to read, reason and act across data and models."
        <div class="quote-attr">— OA AI Team</div>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# HEADER
# ----------------------------------------------------------------------------
h1, h2 = st.columns([3, 2])
with h1:
    st.markdown('<div class="page-title">OA AI Capability Journey</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Learn. Build. Apply. Lead.</div>', unsafe_allow_html=True)
with h2:
    b1, b2, b3 = st.columns(3)
    with b1:
        st.button("ℹ️ How to use this board", use_container_width=True)
    with b2:
        st.button("📄 AI Capability Guide", use_container_width=True)
    with b3:
        st.markdown('<div class="purple-btn">', unsafe_allow_html=True)
        st.button("💬 Share feedback", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# ----------------------------------------------------------------------------
# MAIN + RIGHT RAIL LAYOUT
# ----------------------------------------------------------------------------
main_col, right_col = st.columns([3, 1], gap="large")

with main_col:
    st.markdown('<div class="section-title">Choose your learning pathway</div>', unsafe_allow_html=True)

    tracks = [
        ("🏆", "Fundamentals", "Track", "8 Capabilities", "#2f6fed", "#eaf1ff"),
        ("🕸️", "Agentic AI", "Track", "6 Capabilities", "#2f9e5c", "#e9f8ee"),
        ("💠", "RAG & Data", "Track", "5 Capabilities", "#8b5cf6", "#f2edfe"),
        ("💡", "LLM & Prompt Ops", "Track", "6 Capabilities", "#e8781f", "#fef1e6"),
        ("🛡️", "Governance & Responsible AI", "Track", "4 Capabilities", "#e0373f", "#fdecec"),
        ("🚀", "Simulation & Innovation", "Track", "4 Capabilities", "#12163a", "#eceef5"),
    ]
    cols = st.columns(6)
    for col, (icon, name, sub, count, color, bg) in zip(cols, tracks):
        with col:
            st.markdown(f"""
            <div class="track-card" style="border-color:{color}33; background:{bg};">
                <div class="track-icon">{icon}</div>
                <p class="track-name" style="color:{color};">{name}</p>
                <p class="track-sub">{sub}</p>
                <p class="track-count">{count}</p>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="section-title">Your AI Capability Journey</div>', unsafe_allow_html=True)

    stages = [
        ("🌱", "FOUNDATION", "Build your basics", "#2f6fed",
         ["AI & LLM Fundamentals", "Prompt Engineering", "Responsible AI", "Governance Basics"], "View all (8)"),
        ("🛠️", "PRACTITIONER", "Apply & build", "#2f9e5c",
         ["Work with GPT-4/4.1/5", "Claude 3.x & Gemini", "Multi-Modal AI", "GitHub Copilot"], "View all (8)"),
        ("</>", "ADVANCED BUILDERS", "Design & integrate", "#8b5cf6",
         ["Azure AI Search", "Vector Databases", "Redis (Memory Cache)", "LangChain", "LangGraph", "Prompt Flow"], "View all (5)"),
        ("🕸️", "AGENTIC AI", "Orchestrate & scale", "#e8781f",
         ["MCP & Tool Abstraction", "Copilot Studio", "Agent Frameworks", "LangGraph", "Multi-Agent Systems"], "View all (6)"),
        ("🛡️", "ENTERPRISE DEPLOYMENT", "Secure & govern", "#e0373f",
         ["Security & Guardrails", "Auditing & Monitoring", "Compliance", "Decision Guardrails"], "View all (4)"),
        ("🚀", "INNOVATION LAB", "Simulate & explore", "#12163a",
         ["Synthetic Data Generation", "Digital Twins (Unreal Engine)", "Mistral & LLAMA", "Simulation & Sandbox"], "View all (4)"),
    ]

    st.markdown('<div class="journey-wrap">', unsafe_allow_html=True)
    circ_cols = st.columns(6)
    for col, (icon, title, sub, color, items, view) in zip(circ_cols, stages):
        with col:
            st.markdown(f"""
                <div class="journey-circle" style="border-color:{color}; color:{color};">{icon}</div>
                <div class="journey-stage-title" style="color:{color};">{title}</div>
                <div class="journey-stage-sub">{sub}</div>
                <ul class="journey-list">
                    {''.join(f'<li>{i}</li>' for i in items)}
                </ul>
                <a class="view-all-link" style="color:{color};" href="#">{view}</a>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- HOW YOU LEARN ----------------
    st.markdown('<div class="section-title">How you learn</div>', unsafe_allow_html=True)
    steps = [
        ("📖", "1. LEARN", "Self-paced content (1-2 hrs)"),
        ("👥", "2. WORKSHOP", "Instructor-led (2-4 hrs)"),
        ("🧪", "3. SANDBOX LAB", "Guided hands-on (2-4 hrs)"),
        ("⚙️", "4. BUILD", "Mini project / use case (½ - 1 day)"),
        ("📊", "5. SHOWCASE", "Demo to community (15 mins)"),
        ("🏅", "6. BADGE", "Earn capability accreditation"),
    ]
    step_cols = st.columns(6)
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

    # ---------------- EVENTS + LABS ----------------
    ev_col, lab_col = st.columns(2, gap="large")

    with ev_col:
        st.markdown('<div class="section-title" style="display:inline;">Upcoming Workshops & Events</div>'
                     '<span style="float:right; font-size:12.5px; font-weight:700; color:#2f6fed;">View calendar →</span>',
                     unsafe_allow_html=True)
        st.markdown('<div class="white-card">', unsafe_allow_html=True)

        events = [
            ("📅", "#e8f0ff", "#2f6fed", "Intro to Prompt Engineering for Consultants", "22 May 2025", None),
            ("📗", "#e9f8ee", "#2f9e5c", "Building with RAG on Azure AI Search", "29 May 2025", ("Practitioner", "#e9f8ee", "#2f9e5c")),
            ("📘", "#f2edfe", "#8b5cf6", "Multi-Agent Orchestration with LangGraph", "5 June 2025", ("Advanced", "#f2edfe", "#8b5cf6")),
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
        st.markdown('<div class="section-title" style="display:inline;">Sandbox Labs</div>'
                     '<span style="float:right; font-size:12.5px; font-weight:700; color:#2f6fed;">Open Lab Environment →</span>',
                     unsafe_allow_html=True)
        labs = [
            ("RAG Lab", "Build a company knowledge assistant", "#eaf1ff", "#2f6fed", "Start Lab"),
            ("Agent Builder Lab", "Create your first AI agent", "#e9f8ee", "#2f9e5c", "Start Lab"),
            ("Prompt Flow Lab", "Test, evaluate and improve prompts", "#f2edfe", "#8b5cf6", "Start Lab"),
            ("Synthetic Data Lab", "Generate data for AI & analytics", "#fef1e6", "#e8781f", "Start Lab"),
        ]
        lc = st.columns(4)
        for col, (title, desc, bg, color, link) in zip(lc, labs):
            with col:
                st.markdown(f"""
                <div class="lab-card" style="background:{bg};">
                    <div>
                        <div class="lab-title" style="color:{color};">{title}</div>
                        <div class="lab-desc">{desc}</div>
                    </div>
                    <div class="lab-link" style="color:{color};">{link} →</div>
                </div>
                """, unsafe_allow_html=True)

    st.write("")
    st.markdown("""
    <div class="footer-banner">
        <div style="font-size:20px;">🌱</div>
        <div>
            <a href="#" style="font-weight:700; color:#12163a; text-decoration:none;">New to AI? Start here →</a>
            &nbsp;&nbsp;<span style="color:#6b7086; font-size:13px;">Begin your journey with our AI Foundations path designed for everyone.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# RIGHT RAIL
# ----------------------------------------------------------------------------
with right_col:
    st.markdown("""
    <div class="survey-card">
        <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:18px;">✅</span>
            <span style="font-weight:800; font-size:14px; color:#12163a;">CAPABILITY INITIAL SURVEY</span>
        </div>
        <p style="font-size:12.5px; color:#6b7086; margin:8px 0 10px 0;">Start your journey with a quick assessment</p>
        <div class="survey-check">✔ Understand your current capability</div>
        <div class="survey-check">✔ Identify strengths and gaps</div>
        <div class="survey-check">✔ Get personalized learning recommendations</div>
        <div class="survey-check">✔ Track your growth over time</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="purple-btn">', unsafe_allow_html=True)
    st.button("Take a Capability Test →", use_container_width=True, key="survey_btn")
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="section-title" style="font-size:16px;">Tools We Work With</div>', unsafe_allow_html=True)

    tools = [
        ("🔷", "Azure AI Search"), ("🟥", "Redis"), ("⛓️", "LangChain"), ("🔗", "LangGraph"),
        ("🧩", "Copilot Studio"), ("Ⓜ️", "Microsoft Foundry"), ("🐙", "GitHub Copilot"), ("🌀", "Celonis REST API"),
        ("🌐", "OpenAI"), ("✨", "Claude"), ("💎", "Gemini"), ("🦙", "Llama"),
        ("🌪️", "Mistral"), ("🎨", "DALL-E"), ("🌆", "Midjourney"), ("🔊", "Whisper"),
        ("🏛️", "Unreal Engine"), ("🌊", "Prompt Flow"), ("🦜", "LangSmith"), ("⚖️", "Weights & Biases"),
    ]
    tc = st.columns(4)
    for i, (icon, name) in enumerate(tools):
        with tc[i % 4]:
            st.markdown(f'<div class="tool-chip">{icon} {name}</div>', unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="section-title" style="font-size:16px;">Quick Links & Resources</div>', unsafe_allow_html=True)
    links = [
        "🛠️ AI Tooling Guide", "📚 OA AI Use Cases Library",
        "💬 Prompt Engineering Guide", "✅ Secure AI Checklist",
        "📋 Responsible AI Principles", "❓ Ask the Community",
    ]
    lc2 = st.columns(2)
    for i, link in enumerate(links):
        with lc2[i % 2]:
            st.markdown(f'<div class="qlink">{link}</div>', unsafe_allow_html=True)