import streamlit as st

# --------------------------------------
# PAGE CONFIG
# --------------------------------------
st.set_page_config(
    page_title="OA AI Capability Journey",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------
# STYLING
# --------------------------------------
st.markdown("""
<style>

.main {
    background-color:#f7f8fc;
}

div[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#020c3d,#001544);
}

.sidebar-title{
    color:white;
    font-size:24px;
    font-weight:bold;
}

.card {
    background:white;
    padding:18px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
    border:1px solid #e5e7eb;
    height:100%;
}

.path-card {
    background:white;
    padding:16px;
    border-radius:12px;
    border:2px solid #dedede;
    text-align:center;
}

.section-header{
    font-size:28px;
    font-weight:700;
    margin-bottom:10px;
}

.h2{
    font-size:20px;
    font-weight:600;
}

.metric-box{
    background:#ffffff;
    padding:15px;
    border-radius:12px;
    text-align:center;
}

.capability-stage{
    background:white;
    padding:15px;
    border-radius:12px;
    border-top:5px solid #6a0dad;
}

.tool-tile{
    background:white;
    border:1px solid #e9e9e9;
    border-radius:10px;
    text-align:center;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------
# SIDEBAR
# --------------------------------------

with st.sidebar:
    st.markdown("<div class='sidebar-title'>OA AI Journey</div>",
                unsafe_allow_html=True)

    st.divider()

    menu = [
        "Home",
        "Learning Pathways",
        "Capability Map",
        "Workshops",
        "Sandbox Labs",
        "Tools & Guides",
        "Use Cases",
        "Feedback",
        "Progress",
        "Community"
    ]

    for item in menu:
        st.button(item, use_container_width=True)

# --------------------------------------
# HEADER
# --------------------------------------

col1,col2,col3 = st.columns([6,2,2])

with col1:
    st.title("OA AI Capability Journey")
    st.caption("Learn. Build. Apply. Lead.")

with col2:
    st.button("📖 AI Capability Guide", use_container_width=True)

with col3:
    st.button("💬 Share Feedback", use_container_width=True)

st.divider()

# --------------------------------------
# LEARNING PATHWAYS
# --------------------------------------

st.subheader("Choose your learning pathway")

c1,c2,c3,c4,c5,c6 = st.columns(6)

tracks = [
    ("🏆","Fundamentals",8,"#2563eb"),
    ("⚙️","Agentic AI",6,"#16a34a"),
    ("🧠","RAG & Data",5,"#7c3aed"),
    ("✨","LLM & Prompt Ops",6,"#ea580c"),
    ("🛡️","Governance AI",4,"#dc2626"),
    ("🚀","Simulation",4,"#374151")
]

for col,(icon,title,count,color) in zip(
        [c1,c2,c3,c4,c5,c6],tracks):

    with col:
        st.markdown(f"""
        <div class="path-card" style="border-color:{color}">
            <h3>{icon}</h3>
            <b>{title}</b><br>
            {count} Capabilities
        </div>
        """,
        unsafe_allow_html=True)

st.write("")

# --------------------------------------
# MAIN CONTENT
# --------------------------------------

left,right = st.columns([3,1])

# --------------------------------------
# JOURNEY
# --------------------------------------

with left:

    st.subheader("Your AI Capability Journey")

    stages = [
        "Foundation",
        "Practitioner",
        "Advanced Builders",
        "Agentic AI",
        "Enterprise Deployment",
        "Innovation Lab"
    ]

    cols = st.columns(len(stages))

    for col,stage in zip(cols,stages):
        with col:
            st.markdown(f"""
            <div class="capability-stage">
                <b>{stage}</b>
            </div>
            """,
            unsafe_allow_html=True)

    st.write("")

    capability_cols = st.columns(6)

    data = {
        "Foundation":[
            "AI Fundamentals",
            "Prompt Engineering",
            "Responsible AI",
            "Governance"
        ],
        "Practitioner":[
            "GPT-4",
            "Claude",
            "Gemini",
            "GitHub Copilot"
        ],
        "Advanced Builders":[
            "Azure AI Search",
            "Vector DB",
            "LangChain",
            "LangGraph"
        ],
        "Agentic AI":[
            "MCP",
            "Copilot Studio",
            "Agent Frameworks",
            "Multi-Agent"
        ],
        "Enterprise Deployment":[
            "Guardrails",
            "Monitoring",
            "Compliance",
            "Security"
        ],
        "Innovation Lab":[
            "Synthetic Data",
            "Digital Twins",
            "Mistral",
            "Simulation"
        ]
    }

    for col,key in zip(capability_cols,data.keys()):
        with col:
            st.markdown("<div class='card'>",unsafe_allow_html=True)
            st.markdown(f"**{key}**")

            for item in datast.write("•",item)

            st.markdown("</div>",
                        unsafe_allow_html=True)

# --------------------------------------
# RIGHT PANEL
# --------------------------------------

with right:

    st.markdown("""
    <div class='card'>
    <h3>Capability Initial Survey</h3>
    Assess your current capability level and receive personalised learning recommendations.
    </div>
    """, unsafe_allow_html=True)

    st.button(
        "Take Capability Test",
        use_container_width=True
    )

    st.write("")

    st.markdown("### Tools We Work With")

    tools = [
        "Azure AI Search",
        "Redis",
        "LangChain",
        "LangGraph",
        "Copilot Studio",
        "MS Foundry",
        "GitHub API",
        "OpenAI",
        "Claude",
        "Gemini",
        "Mistral",
        "Llama"
    ]

    tcols = st.columns(2)

    for i,tool in enumerate(tools):
        with tcols[i%2]:
            st.markdown(f"""
            <div class="tool-tile">
            {tool}
            </div>
            """,
            unsafe_allow_html=True)

# --------------------------------------
# LEARNING FLOW
# --------------------------------------

st.write("")
st.subheader("How You Learn")

flow = st.columns(6)

steps = [
    "Learn",
    "Workshop",
    "Sandbox Lab",
    "Build",
    "Showcase",
    "Badge"
]

for col,step in zip(flow,steps):
    with col:
        st.markdown(f"""
        <div class="metric-box">
            <h4>{step}</h4>
        </div>
        """,
        unsafe_allow_html=True)

st.write("")

# --------------------------------------
# EVENTS + LABS
# --------------------------------------

col1,col2 = st.columns(2)

with col1:

    st.subheader("Upcoming Workshops")

    workshops = [
        ("Intro to Prompt Engineering","22 July"),
        ("Building with RAG","29 July"),
        ("Multi-Agent Systems","05 Aug")
    ]

    for title,date in workshops:
        st.info(f"📅 {title} — {date}")

with col2:

    st.subheader("Sandbox Labs")

    labs = [
        "RAG Lab",
        "Agent Builder Lab",
        "Prompt Flow Lab",
        "Synthetic Data Lab"
    ]

    lab_cols = st.columns(2)

    for i,lab in enumerate(labs):
        with lab_cols[i%2]:
            st.success(lab)

# --------------------------------------
# QUICK LINKS
# --------------------------------------

st.subheader("Quick Links & Resources")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.link_button("AI Tooling Guide","#")

with c2:
    st.link_button("Prompt Engineering","#")

with c3:
    st.link_button("Responsible AI","#")

with c4:
    st.link_button("Use Case Library","#")

st.divider()

st.success(
    "New to AI? Start with the Foundations pathway and build toward Agentic AI."
)