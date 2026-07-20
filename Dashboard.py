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

EVENTS = [
    ("📗", "Building with RAG on Azure AI Search", "29 October 2026", "rag_data", "Practitioner", "Virtual"),
    ("📘", "Multi-Agent Orchestration with LangGraph", "5 December 2026", "agentic", "Advanced", "In-person"),
    ("🧠", "Prompt Engineering Fundamentals", "12 September 2026", "fundamentals", "Beginner", "Virtual"),
    ("🛡️", "Governance & Guardrails Workshop", "3 November 2026", "governance", "Practitioner", "In-person"),
    ("🚀", "Simulating with Digital Twins", "18 December 2026", "simulation", "Advanced", "Virtual"),
    ("💡", "Working with Claude 3.x & Gemini", "22 September 2026", "llm_promptops", "Beginner", "Virtual"),
]

# Homepage "Upcoming Workshops & Events" preview — fixed custom styling per event
HOME_EVENTS = [
    ("🧠", "#eef6ff", "#3b82f6", "Prompt Engineering Fundamentals", "12 September 2026",
        ("Beginner", "#eef6ff", "#3b82f6")),
    ("💡", "#fff7e6", "#f59f00", "Working with Claude 3.x & Gemini", "22 September 2026",
        ("Beginner", "#fff7e6", "#f59f00")),
    ("📗", "#e9f8ee", "#2f9e5c", "Building with RAG on Azure AI Search", "29 October 2026",
        ("Practitioner", "#e9f8ee", "#2f9e5c")),
]

LABS = [
    ("🧪", "RAG Lab", "Build a company knowledge assistant", "rag_data", "Intermediate"),
    ("🤖", "Agent Builder Lab", "Create your first AI agent", "agentic", "Intermediate"),
    ("🌊", "Prompt Flow Lab", "Test, evaluate and improve prompts", "llm_promptops", "Beginner"),
    ("🧬", "Synthetic Data Lab", "Generate data for AI & analytics", "simulation", "Advanced"),
    ("🛡️", "Guardrails Sandbox", "Practice building safe AI approval flows", "governance", "Intermediate"),
    ("🏆", "Foundations Playground", "Warm up with core LLM concepts", "fundamentals", "Beginner"),
]

LEVELS = ["New to this", "Beginner", "Comfortable", "Expert"]

import datetime as _datetime
def parse_event_date(d):
    return _datetime.datetime.strptime(d, "%d %B %Y")

# Full course-catalogue breakdown, mapped into whichever of the 6 pathways each course fits best.
COURSE_BREAKDOWN = {
    "fundamentals": [
        {
            "title": "Microsoft Azure AI Fundamentals (AI-901)",
            "audience": "Everyone — leads into 'Develop AI Agents on Azure'",
            "duration": "Self-paced",
            "link": "Available on Degreed — search 'AI-901: Microsoft Azure AI Fundamentals'",
            "outline": """
**AI concepts for developers and technology professionals**
- Introduction to AI concepts
- Introduction to generative AI and agents
- Introduction to natural language processing concepts
- Introduction to AI speech concepts
- Introduction to computer vision concepts
- Introduction to AI-powered information extraction concepts

**Get started with AI applications and agents on Azure**
- Get started with AI in Azure
- Get started with generative AI and agents in Azure
- Get started with text analysis in Azure
- Get started with speech in Azure
- Get started with computer vision in Azure
- Get started with AI-powered information extraction in Azure

**Practice assessment for the AI-901 exam**
""",
        },
        {
            "title": "Intro to LLMs",
            "audience": "Everyone (35 min core), optional technical extension (+16 min)",
            "duration": "35–51 mins",
            "link": "https://capgemini.udemy.com/course/intro-to-large-language-models-llms/",
            "outline": """
**Intro to LLMs** — 7 lectures (15 mins)

**Getting started with GPT models** (20 mins)
- What does GPT mean?
- The development of ChatGPT
- Setting up the environment (overview only, non-technical)
- OpenAI API (conceptual overview)
- Generating text
- Customizing GPT output
- Keyword text summarization

**Optional — for a technical background/experience** (+16 mins)
- Setting up the environment
- Coding a simple chatbot
- LangChain introduction
- LangChain
- Adding custom data to a chatbot
""",
        },
    ],
    "agentic": [
        {
            "title": "Intro to Agentic AI",
            "audience": "Everyone",
            "duration": "6 hrs",
            "link": "https://degreed.com/pathway/v83jrwgqpx/pathway",
            "outline": """
- Ethics
- Example
- Multi-agent systems
- Technical
- Value measurements
- Readiness
""",
        },
        {
            "title": "Get started with Microsoft 365 Agent",
            "audience": "Everyone",
            "duration": "48 mins",
            "link": "https://learn.microsoft.com/en-us/training/modules/agent-365-get-started/",
            "outline": """
- Introduction to challenges for frontier firms
- What is Microsoft Agent 365?
- What are the benefits of using Microsoft Agent 365?
- Explore agent observability
- Implement governance across the agent lifecycle
- Protect agents using security capability
- Who uses Microsoft Agent 365?
- Check your knowledge / Summary
""",
        },
        {
            "title": "Develop AI Agents on Azure",
            "audience": "Technical background or experience",
            "duration": "9 hrs 52 mins",
            "link": "Microsoft Learn — 'Develop AI Agents on Azure' training path",
            "outline": """
- Develop AI agents with Microsoft Foundry and Visual Studio Code
- Integrate custom tools into your agent
- Integrate MCP tools with Azure AI Agents
- Build knowledge-enhanced AI agents with Foundry IQ
- Integrate your agent with Microsoft 365
- Build agent-driven workflows using Microsoft Foundry
- Develop an AI agent with Microsoft Agent Framework
- Orchestrate a multi-agent solution using the Microsoft Agent Framework
- Discover Azure AI Agents with A2A
""",
        },
        {
            "title": "LangGraph & Multi-Agent Systems",
            "audience": "Technical background or experience — part of 'Production AI Agents with LangChain + LangGraph'",
            "duration": "~6 hrs of a 17 hr course",
            "link": "Udemy Business — 'Production AI Agents with LangChain + LangGraph [2026]'",
            "outline": """
**LangGraph — A Full Deep Dive**
- Building your first graph, reducers and accumulating state
- Message state, multi-node pipelines, chaining LLM calls
- Edges, conditional edges and routing
- Cycles/loops (e.g. self-correcting code writer)
- Human in the loop, checkpointing

**Multi-Agent Systems with LangGraph and LangChain**
- ReAct pattern, tool-calling agents, custom tools with error handling
- The Supervisor agent and agent handoffs
- Map-reduce strategy, message passing and shared state
- Hierarchical architecture
- Final project: multi-agent research system, built from the ground up
""",
        },
        {
            "title": "Model Context Protocol & Claude Code",
            "audience": "Technical background or experience — part of 'Complete Agentic AI Bootcamp'",
            "duration": "~4 hrs of a 40+ hr bootcamp",
            "link": "Udemy Business — 'Complete Agentic AI Bootcamp With LangGraph and LangChain'",
            "outline": """
**Model Context Protocol**
- Introduction to MCP, its components and how they communicate
- Demo of MCP with Claude Desktop, Cursor IDE setup, Smithery AI
- Building MCP servers with tools and clients from scratch using LangChain

**Claude Code**
- Introduction to the Claude ecosystem, setup and working with Claude Code
- Claude Code agents, agent views and agent teams
- Hooks, skills and plugins in Claude Code

**Building Deep Agents with LangChain**
- Introduction and basics implementation, customization
- Backends, Deep Agents vs Claude SDK
- Context engineering and using skills for it
- Sub-agents, and a full project implementing all features
""",
        },
        {
            "title": "End-to-End Agentic AI Projects",
            "audience": "Technical background or experience — part of 'Complete Agentic AI Bootcamp'",
            "duration": "~2 hrs of hands-on projects",
            "link": "Udemy Business — 'Complete Agentic AI Bootcamp With LangGraph and LangChain'",
            "outline": """
- End-to-end agentic AI project with LangGraph (Streamlit front end, graph builder, node implementation, full pipeline & testing)
- End-to-end agentic chatbot with web search functionality
- AI News Summariser — end-to-end agentic AI project
- End-to-end blog generation agentic AI app (with translation, FastAPI, LangGraph Studio debugging)
""",
        },
        {
            "title": "MCP Crash Course: Complete Model Context Protocol in a Day",
            "audience": "Technical background or experience for most modules; highlighted areas suit everyone",
            "duration": "8 hrs 29 mins",
            "link": "https://capgemini.udemy.com/course/complete-mcp-bootcamp-build-next-gen-ai-agents-with-mcp/",
            "outline": """
- MCP fundamentals: introduction, components, communication between them
- Getting started with Claude Desktop and Cursor IDE, and Smithery AI
- Building your own MCP client using Python and the Google Gemini API
- Building a Dockerised MCP server
- LangChain MCP Adapters, and MCP with multiple-server support
- MCP server and client using SSE, and deployment to AWS Cloud
- Hands-on projects: Real-Time Weather Agent, Job Recommendation System, StoryForge Agent, Clinisight AI, and a full multi-agent app with MCP
- Building an agent with Google's Agent Development Kit (ADK)
""",
        },
    ],
    "rag_data": [
        {
            "title": "LangChain Foundations & RAG",
            "audience": "Technical background or experience — part of 'Production AI Agents with LangChain + LangGraph'",
            "duration": "~5 hrs of a 17 hr course",
            "link": "Udemy Business — 'Production AI Agents with LangChain + LangGraph [2026]'",
            "outline": """
**LangChain Foundations — A Deep Dive**
- The LangChain ecosystem, LCEL and runnable chains
- Batch execution, real-time streaming, schema inspection
- Prompt templates & messages, output parsers and structured outputs
- Project: Smart Q&A Bot

**Chain Patterns**
- Basic and parallel chains, passthrough runnables, chain branching, debugging

**Document Loading, Chunking & Embeddings**
- Document loaders (text, web, lazy, PDF)
- Text splitting strategies (recursive, markdown, code) and why chunking matters
- Embeddings overview, free embedding models
- Vector stores: architecture, Chroma setup, similarity search, metadata filtering, persistence

**RAG and Memory — A Comprehensive Dive**
- Basic RAG pipeline through to advanced RAG (multi-query, contextual compression, hybrid search, parent document retriever)
- Conversation memory (windowed, summary, multi-session)
- Project: AI Research Assistant, built up in stages
""",
        },
        {
            "title": "LangChain Hands-On & Retrieval",
            "audience": "Technical background or experience — part of 'Complete Agentic AI Bootcamp'",
            "duration": "~6 hrs of a 40+ hr bootcamp",
            "link": "Udemy Business — 'Complete Agentic AI Bootcamp With LangGraph and LangChain'",
            "outline": """
- LangChain hands-on: core components, document loaders, text splitters
- Embeddings with OpenAI, Ollama and HuggingFace; vector stores with FAISS and ChromaDB
- Getting started with OpenAI and Ollama: retrievers, chains, a simple GenAI app, and tracking with LangSmith
- Building AI agents with conversation history: chat message history and vector store retrievers
- RAG with LangGraph: agentic RAG, corrective RAG, adaptive RAG
- Vectorless RAG: PageIndex and vectorless vs. traditional RAG approaches
""",
        },
    ],
    "llm_promptops": [
        {
            "title": "LLM Mastery: ChatGPT, Gemini, Claude, Llama, OpenAI & APIs",
            "audience": "Technical background or experience",
            "duration": "3 hrs 45 mins",
            "link": "Available on Capgemini Udemy Business — search 'LLM Mastery'",
            "outline": """
- Closed-source LLMs and how to use them (2 hrs 51 mins)
- APIs of closed-source LLMs (48 mins)
""",
        },
        {
            "title": "Understanding APIs and RESTful APIs Crash Course",
            "audience": "Everyone (core, 12 mins); technical roles/experience (+25 mins)",
            "duration": "12–37 mins",
            "link": "https://capgemini.udemy.com/course/learn-and-understand-apis-and-restful-apis/",
            "outline": """
**Core (everyone)**
- What is an API? The simplest way to think about it, and a real-life use case
- What programming languages can we use?
- Introduction to RESTful APIs and JSON

**Extension (technical roles/experience)**
- A real JavaScript API example
- GET, POST, DELETE and PUT/PATCH requests
- Consuming APIs: requests, responses, and common status codes
- API security
""",
        },
    ],
    "governance": [
        {
            "title": "Agent Guardrails & Production Deployment",
            "audience": "Technical background or experience — part of 'Production AI Agents with LangChain + LangGraph'",
            "duration": "~3 hrs of a 17 hr course",
            "link": "Udemy Business — 'Production AI Agents with LangChain + LangGraph [2026]'",
            "outline": """
**Production Deployment — Deploying AI Agents**
- Observability with LangSmith
- PII detection, prompt-injection defence, and the "LLM Guard" pattern
- Testing: unit, integration, LLM-as-judge and regression testing
- Resilience patterns: circuit breaker, fallback chain, retry with backoff
- Cost control: semantic caching, token budgeting, model routing
- Final project: a production-ready, secured and monitored agent API

**Guardrails with LangChain**

**LLM Gateways** — understanding and implementation
""",
        },
    ],
    "simulation": [],
}

SURVEY_QUESTIONS = [
    ("fundamentals", "How well do you understand the basics of how AI tools work?"),
    ("llm_promptops", "How comfortable are you using AI chat tools day-to-day for tasks and writing?"),
    ("rag_data", "How familiar are you with connecting AI to documents or company data?"),
    ("agentic", "How much experience do you have with AI that can take actions or complete multi-step tasks on its own?"),
    ("governance", "How confident are you with the rules and safe practices around using AI at work?"),
    ("simulation", "How much have you explored newer or more experimental AI tools and techniques?"),
]

FAQS = [
    ("What is the OA AI Capability Journey?",
     "It's a structured learning programme covering six pathways, from AI fundamentals through to advanced simulation, "
     "so everyone can build AI skills at their own pace."),
    ("How do I know where to start?",
     "Take the Capability Survey — answer six quick questions and you'll get a recommended pathway to start with."),
    ("Do I have to complete pathways in order?",
     "No. The Journey is a suggested progression, but you can jump into any pathway that matches your current project or interests."),
    ("What's the difference between a course, a workshop and a lab?",
     "Courses are self-paced content you work through solo. Workshops are instructor-led sessions with the community. "
     "Sandbox Labs are guided, hands-on environments to practise what you've learned."),
    ("How long does each pathway take?",
     "Each course lists its own duration, generally 1-3 hours. A full pathway usually takes a few weeks if done alongside your day-to-day work."),
    ("Who do I contact if I have questions?",
     "Reach out to the Learning & Capability Team, or leave feedback using the 'Share feedback' button at the top of the board."),
]

# ============================================================================
# STATE
# ============================================================================
if "page" not in st.session_state:
    st.session_state.page = "home"
if "survey_scores" not in st.session_state:
    st.session_state.survey_scores = {k: 0 for k in TRACKS}
if "survey_submitted" not in st.session_state:
    st.session_state.survey_submitted = False


def go_home():
    st.session_state.page = "home"


def go_track(key):
    st.session_state.page = key


def go_page(key):
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
        padding: 4px 0 22px 0; font-weight: 800; font-size: 16.5px; color: white !important;
        line-height: 1.3;
    }
    .sidebar-logo .logo-icon { font-size: 24px; flex-shrink: 0; }

    /* secondary (inactive) nav buttons */
    section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="secondary"] {
        background: transparent !important; border: 1px solid transparent !important;
        text-align: left !important; justify-content: flex-start !important;
        padding: 9px 12px !important; font-size: 13.8px !important; font-weight: 500 !important;
        color: #c7cbe6 !important; min-height: unset !important; border-radius: 8px !important;
    }
    section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="secondary"]:hover {
        background: #1c2450 !important; color: white !important; border-color: transparent !important;
    }
    /* primary (active) nav button */
    section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="primary"] {
        background: linear-gradient(90deg, #5b3df0, #2f6fed) !important;
        border: none !important; text-align: left !important; justify-content: flex-start !important;
        padding: 9px 12px !important; font-size: 13.8px !important; font-weight: 700 !important;
        color: white !important; min-height: unset !important; border-radius: 8px !important;
        box-shadow: 0 3px 10px rgba(91,61,240,0.35) !important;
    }
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

    /* ---------- Section headers ---------- */
    .section-title { font-size: 18px; font-weight: 800; color: #12163a; margin: 6px 0 12px 0; line-height: 1.3; }
    .section-title-row { display: flex; align-items: center; justify-content: space-between; margin: 6px 0 12px 0; }
    .section-link { font-size: 12.5px; font-weight: 700; color: #2f6fed; text-decoration: none; white-space: nowrap; }

    /* ---------- Track cards (clickable pathway buttons) ---------- */
    .track-caption { font-size: 12px; color: #6b7086; margin: 8px 2px 14px 2px; line-height: 1.4; text-align: center; }
    .track-caption b { color: #12163a; }
    .track-dot { display:inline-block; width:8px; height:8px; border-radius:50%; margin-right:5px; vertical-align:middle; }

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
    .badge { display: inline-block; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; margin-top: 4px; margin-right:6px;}

    .lab-card {
        border-radius: 12px; padding: 15px; min-height: 140px;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .lab-title { font-weight: 700; font-size: 13.5px; margin-bottom: 4px; line-height: 1.3; }
    .lab-desc { font-size: 11.5px; color: #454868; line-height: 1.4; }

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

    /* ---------- Generic page hero ---------- */
    .page-hero {
        border-radius: 14px; padding: 22px 24px; margin-bottom: 22px;
        display: flex; align-items: center; gap: 14px;
    }
    .page-hero-icon {
        width: 50px; height: 50px; border-radius: 12px; background: rgba(255,255,255,0.55);
        display: flex; align-items: center; justify-content: center; font-size: 24px; flex-shrink: 0;
    }
    .page-hero-title { font-size: 21px; font-weight: 800; margin: 0; color: #12163a; line-height: 1.25; }
    .page-hero-sub { font-size: 13px; margin-top: 3px; color: #454868; }

    /* survey */
    .survey-card {
        background: white; border-radius: 12px; border: 1px solid #e7e9f2;
        padding: 16px 18px; margin-bottom: 14px;
    }
    .survey-track-label { font-weight: 700; font-size: 14px; margin-bottom: 2px; }
    .survey-track-sub { font-size: 11.5px; color: #6b7086; margin-bottom: 10px; }
    .result-bar-bg { background: #eef0f6; border-radius: 8px; height: 14px; width: 100%; overflow: hidden; }
    .result-bar-fill { height: 14px; border-radius: 8px; }
    .result-row { display:flex; align-items:center; gap:12px; margin-bottom: 12px; }
    .result-label { width: 190px; font-size: 12.5px; font-weight: 700; color:#12163a; flex-shrink:0; }
    .result-pct { width: 40px; font-size: 11.5px; font-weight: 700; color:#6b7086; text-align:right; flex-shrink:0; }

    /* events */
    .event-card { background: white; border-radius: 12px; border: 1px solid #e7e9f2; padding: 16px; margin-bottom: 12px; }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR
# ============================================================================
with st.sidebar:
    st.markdown(
        '<div class="sidebar-logo"><span class="logo-icon">🔷</span>'
        '<span>OA AI Capability Journey</span></div>',
        unsafe_allow_html=True,
    )
    nav_items = [
        ("🏠", "Home", "home"),
        ("📚", "Capability Survey", "capability_survey"),
        ("🗓️", "Workshops & Events", "workshops"),
        ("🧪", "Sandbox Labs", "sandbox"),
        ("❓", "FAQ", "faq"),
    ]

    current_page = st.session_state.get("page", "home")
    for icon, label, page_key in nav_items:
        active = current_page == page_key or (page_key == "home" and current_page in TRACKS)
        st.button(
            f"{icon}  {label}",
            key=f"nav_{page_key}",
            use_container_width=True,
            type="primary" if active else "secondary",
            on_click=go_page,
            args=(page_key,),
        )

    st.markdown("""
    <div class="quote-box">
        "The best way to predict the future is to build it."
        <div class="quote-attr">— Learning & Capability Team</div>
    </div>
    """, unsafe_allow_html=True)

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
            - Take the **Capability Survey** to get a personalised starting point.
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

    breakdown = COURSE_BREAKDOWN.get(key, [])
    if breakdown:
        st.write("")
        st.markdown('<div class="section-title">📖 In-depth course content</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="page-subtitle" style="margin:-6px 0 14px 0;">Full syllabus for the training courses that map to this pathway.</div>',
            unsafe_allow_html=True,
        )
        for course in breakdown:
            with st.expander(f"{course['title']}  ·  {course['duration']}"):
                st.markdown(f"**Audience:** {course['audience']}")
                st.markdown(f"**Where to find it:** {course['link']}")
                st.markdown(course["outline"])


# ============================================================================
# HOME PAGE
# ============================================================================
def render_home():
    main_col, right_col = st.columns([3, 1], gap="large")

    with main_col:
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
        st.markdown('<div class="section-title">Your AI Capability Journey</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle" style="margin:-6px 0 14px 0;">Pick a stage below to jump straight into that pathway.</div>', unsafe_allow_html=True)

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

        st.markdown('<div class="journey-wrap">', unsafe_allow_html=True)
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
                    f"background:{color}12 !important; color:{color} !important; "
                    f"border:1.5px solid {color}55 !important; border-radius:8px !important; "
                    f"min-height:40px !important; height:40px !important; padding:6px 4px !important; "
                    f"font-size:12px !important; font-weight:700 !important; "
                    f"text-align:center !important; justify-content:center !important; "
                    f"white-space:nowrap !important; overflow:hidden !important; text-overflow:ellipsis !important;}}"
                    f"div[data-testid='column']:has(#marker-stage-{track_key}) "
                    f"div[data-testid='stButton'] button:hover {{"
                    f"background:{color} !important; color:white !important; border-color:{color} !important;}}</style>"
                    f"<span id='marker-stage-{track_key}'></span>",
                    unsafe_allow_html=True,
                )
                st.button("Explore →", key=f"stage_{track_key}",
                          use_container_width=True, on_click=go_track, args=(track_key,))
        st.markdown('</div>', unsafe_allow_html=True)

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
            'Upcoming Workshops & Events</span></div>',
            unsafe_allow_html=True,
        )
        rows_html = ""
        for icon, ibg, icolor, title, date, badge in HOME_EVENTS:
            badge_html = ""
            if badge:
                btxt, bbg, bcolor = badge
                badge_html = f'<span class="badge" style="background:{bbg}; color:{bcolor};">{btxt}</span>'
            rows_html += (
                '<div class="event-row">'
                f'<div class="event-icon" style="background:{ibg}; color:{icolor};">{icon}</div>'
                '<div style="flex:1;">'
                f'<div class="event-title">{title}</div>'
                f'{badge_html}'
                '</div>'
                f'<div class="event-date">{date}</div>'
                '</div>'
            )
        st.markdown(f'<div class="white-card">{rows_html}</div>', unsafe_allow_html=True)
        st.write("")
        st.button("View all events →", key="view_all_events", on_click=go_page, args=("workshops",))

    with lab_col:
        st.markdown(
            '<div class="section-title-row"><span class="section-title" style="margin:0;">'
            'Sandbox Labs</span></div>',
            unsafe_allow_html=True,
        )
        lc = st.columns(4)
        for col, (icon, title, desc, track_key, level) in zip(lc, LABS[:4]):
            t = TRACKS[track_key]
            with col:
                st.markdown(f"""
                <div class="lab-card" style="background:{t['bg']};">
                    <div>
                        <div style="font-size:18px; margin-bottom:4px;">{icon}</div>
                        <div class="lab-title" style="color:{t['color']};">{title}</div>
                        <div class="lab-desc">{desc}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        st.write("")
        st.button("Open Lab Environment →", key="view_all_labs", on_click=go_page, args=("sandbox",))

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
# CAPABILITY SURVEY PAGE
# ============================================================================
def render_capability_survey():
    st.markdown("""
    <div class="page-hero" style="background:#eaf1ff;">
        <div class="page-hero-icon">📚</div>
        <div>
            <p class="page-hero-title">Capability Survey</p>
            <p class="page-hero-sub">Answer 6 quick questions — from complete beginner to expert — to get a personalised pathway recommendation.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("survey_form"):
        for i, (track_key, question) in enumerate(SURVEY_QUESTIONS):
            st.markdown(f"""
            <div class="survey-card">
                <div class="survey-track-label" style="color:#12163a;">{i+1}. {question}</div>
            """, unsafe_allow_html=True)
            st.radio(
                f"q_{track_key}",
                options=LEVELS,
                index=st.session_state.survey_scores.get(track_key, 0),
                key=f"survey_{track_key}",
                horizontal=True,
                label_visibility="collapsed",
            )
            st.markdown("</div>", unsafe_allow_html=True)

        submitted = st.form_submit_button("Get my recommendation →", use_container_width=True)
        if submitted:
            for track_key, _ in SURVEY_QUESTIONS:
                st.session_state.survey_scores[track_key] = LEVELS.index(st.session_state[f"survey_{track_key}"])
            st.session_state.survey_submitted = True

    if st.session_state.survey_submitted:
        st.write("")
        st.markdown('<div class="section-title">Your capability snapshot</div>', unsafe_allow_html=True)
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        for track_key, t in TRACKS.items():
            score = st.session_state.survey_scores.get(track_key, 0)
            pct = int((score / (len(LEVELS) - 1)) * 100)
            st.markdown(f"""
            <div class="result-row">
                <div class="result-label">{t['icon']} {t['name']}</div>
                <div class="result-bar-bg"><div class="result-bar-fill" style="width:{pct}%; background:{t['color']};"></div></div>
                <div class="result-pct">{pct}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        lowest_key = min(st.session_state.survey_scores, key=st.session_state.survey_scores.get)
        lowest_t = TRACKS[lowest_key]
        overall_avg = sum(st.session_state.survey_scores.values()) / len(st.session_state.survey_scores)

        st.write("")
        if overall_avg <= 0.75:
            headline = f"Recommended starting point: {lowest_t['name']}"
            sub = "You're just getting going — this pathway builds the foundations everything else relies on."
        else:
            headline = f"Recommended next step: {lowest_t['name']}"
            sub = "This was your lowest-confidence pathway — a great place to focus on next to round out your skills."

        st.markdown(f"""
        <div class="page-hero" style="background:{lowest_t['bg']};">
            <div class="page-hero-icon">{lowest_t['icon']}</div>
            <div>
                <p class="page-hero-title" style="color:{lowest_t['color']};">{headline}</p>
                <p class="page-hero-sub">{sub}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"Go to {lowest_t['name']} track →", key="survey_cta", on_click=go_track, args=(lowest_key,))


# ============================================================================
# WORKSHOPS & EVENTS PAGE
# ============================================================================
def render_workshops_events():
    st.markdown("""
    <div class="page-hero" style="background:#e9f8ee;">
        <div class="page-hero-icon">🗓️</div>
        <div>
            <p class="page-hero-title">Workshops & Events</p>
            <p class="page-hero-sub">Instructor-led sessions to deepen your skills alongside the community.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    filter_options = ["All pathways"] + [t["name"] for t in TRACKS.values()]
    choice = st.selectbox("Filter by pathway", filter_options, label_visibility="collapsed")

    name_to_key = {t["name"]: k for k, t in TRACKS.items()}
    filtered = EVENTS if choice == "All pathways" else [e for e in EVENTS if e[3] == name_to_key[choice]]
    filtered = sorted(filtered, key=lambda e: parse_event_date(e[2]))

    st.write("")
    cols = st.columns(2)
    for i, (icon, title, date, track_key, level, mode) in enumerate(filtered):
        t = TRACKS[track_key]
        with cols[i % 2]:
            st.markdown(f"""
            <div class="event-card" style="border-top:4px solid {t['color']};">
                <div style="display:flex; align-items:flex-start; gap:12px;">
                    <div class="event-icon" style="background:{t['bg']}; color:{t['color']}; width:38px; height:38px; font-size:16px;">{icon}</div>
                    <div style="flex:1;">
                        <div class="event-title" style="font-size:14px;">{title}</div>
                        <div style="margin-top:6px;">
                            <span class="badge" style="background:{t['bg']}; color:{t['color']};">{level}</span>
                            <span class="badge" style="background:#f0f1f6; color:#6b7086;">{mode}</span>
                        </div>
                    </div>
                </div>
                <div class="event-date" style="margin-top:10px;">📅 {date}</div>
            </div>
            """, unsafe_allow_html=True)
            st.button("Register interest →", key=f"event_{i}", use_container_width=True)

    if not filtered:
        st.info("No events found for this pathway yet — check back soon.")


# ============================================================================
# SANDBOX LABS PAGE
# ============================================================================
def render_sandbox_labs():
    st.markdown("""
    <div class="page-hero" style="background:#f2edfe;">
        <div class="page-hero-icon">🧪</div>
        <div>
            <p class="page-hero-title">Sandbox Labs</p>
            <p class="page-hero-sub">Hands-on, guided environments to practise before you build for real.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    for i, (icon, title, desc, track_key, level) in enumerate(LABS):
        t = TRACKS[track_key]
        with cols[i % 3]:
            st.markdown(f"""
            <div class="lab-card" style="background:{t['bg']}; border-top:5px solid {t['color']}; min-height:170px;">
                <div>
                    <div style="font-size:22px; margin-bottom:6px;">{icon}</div>
                    <div class="lab-title" style="color:{t['color']}; font-size:15px;">{title}</div>
                    <div class="lab-desc">{desc}</div>
                    <span class="badge" style="background:white; color:{t['color']}; margin-top:8px;">{level}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Launch Lab →", key=f"lab_launch_{i}", use_container_width=True):
                st.toast(f"Launching {title}... (demo environment)", icon="🧪")
            st.write("")


# ============================================================================
# FAQ PAGE
# ============================================================================
def render_faq():
    st.markdown("""
    <div class="page-hero" style="background:#fef1e6;">
        <div class="page-hero-icon">❓</div>
        <div>
            <p class="page-hero-title">Frequently Asked Questions</p>
            <p class="page-hero-sub">Everything you need to know about using the Capability Journey board.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    for question, answer in FAQS:
        with st.expander(question):
            st.write(answer)


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
elif page == "faq":
    render_faq()
elif page in TRACKS:
    render_track_page(page)
else:
    st.session_state.page = "home"
    render_home()