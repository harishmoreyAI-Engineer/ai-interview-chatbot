import streamlit as st
import requests
import json

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Engineer Interview Prep",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Space+Grotesk:wght@300;400;600;700&display=swap');

/* Base */
html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

/* Background */
.stApp {
    background: #0a0a0f;
    color: #e2e8f0;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0f0f1a !important;
    border-right: 1px solid #1e1e3a;
}

section[data-testid="stSidebar"] * {
    color: #c4c9e2 !important;
}

/* Header */
.hero-header {
    background: linear-gradient(135deg, #0d0d1f 0%, #1a1a3e 50%, #0d1f2d 100%);
    border: 1px solid #2a2a5a;
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}

.hero-header::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 30% 50%, rgba(99, 102, 241, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 70% 50%, rgba(6, 182, 212, 0.06) 0%, transparent 50%);
    pointer-events: none;
}

.hero-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.8rem;
    font-weight: 700;
    background: linear-gradient(90deg, #818cf8, #22d3ee, #818cf8);
    background-size: 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 3s infinite linear;
    margin: 0;
}

@keyframes shimmer {
    0% { background-position: 0% }
    100% { background-position: 200% }
}

.hero-sub {
    color: #64748b;
    font-size: 0.9rem;
    margin-top: 0.4rem;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.05em;
}

/* Chat messages */
.chat-wrapper {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-bottom: 1rem;
}

.msg-user {
    background: linear-gradient(135deg, #1e1e4a, #2a1a4a);
    border: 1px solid #4338ca44;
    border-radius: 16px 16px 4px 16px;
    padding: 1rem 1.25rem;
    align-self: flex-end;
    max-width: 80%;
    color: #c7d2fe;
    font-size: 0.95rem;
    line-height: 1.6;
}

.msg-assistant {
    background: linear-gradient(135deg, #0f1a2e, #0a1628);
    border: 1px solid #0e7490aa;
    border-radius: 16px 16px 16px 4px;
    padding: 1rem 1.25rem;
    align-self: flex-start;
    max-width: 85%;
    color: #e2e8f0;
    font-size: 0.95rem;
    line-height: 1.8;
}

.msg-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.4rem;
    opacity: 0.6;
}

.msg-user .msg-label { color: #818cf8; }
.msg-assistant .msg-label { color: #22d3ee; }

/* Chips */
.chip-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 1rem 0;
}

.chip {
    background: #1e1e3a;
    border: 1px solid #3730a3;
    color: #a5b4fc;
    border-radius: 999px;
    padding: 0.3rem 0.9rem;
    font-size: 0.8rem;
    font-family: 'JetBrains Mono', monospace;
    cursor: pointer;
    transition: all 0.2s;
    display: inline-block;
}

.chip:hover {
    background: #2e2e5a;
    border-color: #818cf8;
    color: #c7d2fe;
}

/* Input area */
.stTextInput > div > div > input,
.stTextArea textarea {
    background: #0f0f1a !important;
    border: 1px solid #2a2a5a !important;
    color: #e2e8f0 !important;
    border-radius: 12px !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

.stTextInput > div > div > input:focus,
.stTextArea textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #4338ca, #0891b2) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.03em !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 15px rgba(67, 56, 202, 0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(67, 56, 202, 0.4) !important;
}

/* Divider */
hr { border-color: #1e1e3a !important; }

/* Selectbox */
.stSelectbox > div > div {
    background: #0f0f1a !important;
    border: 1px solid #2a2a5a !important;
    color: #e2e8f0 !important;
    border-radius: 10px !important;
}

/* Category pills in sidebar */
.category-pill {
    background: #1e1e3a;
    border-left: 3px solid #6366f1;
    padding: 0.4rem 0.75rem;
    border-radius: 0 8px 8px 0;
    margin: 0.3rem 0;
    font-size: 0.82rem;
    color: #a5b4fc;
    cursor: pointer;
}

/* Stats bar */
.stats-bar {
    display: flex;
    gap: 1rem;
    margin: 0.5rem 0 1.5rem;
    flex-wrap: wrap;
}

.stat-chip {
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 8px;
    padding: 0.4rem 0.8rem;
    font-size: 0.78rem;
    font-family: 'JetBrains Mono', monospace;
    color: #6b7280;
}

.stat-chip span {
    color: #22d3ee;
    font-weight: 700;
}

/* Code blocks */
code {
    background: #1e1e3a !important;
    color: #7dd3fc !important;
    padding: 0.1em 0.4em !important;
    border-radius: 4px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.88em !important;
}

pre code {
    background: transparent !important;
    padding: 0 !important;
}

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0a0a0f; }
::-webkit-scrollbar-thumb { background: #2a2a5a; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

# ── Constants ─────────────────────────────────────────────────────────────────
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

FREE_MODELS = {
    "GPT-OSS 120B (OpenAI)": "openai/gpt-oss-120b:free",
}

CATEGORIES = {
    "🧠 ML Fundamentals": [
        "Explain bias-variance tradeoff with an example.",
        "What is overfitting and how do you prevent it?",
        "Explain gradient descent and its variants.",
        "What is regularization and why is it used?",
    ],
    "🤖 Deep Learning": [
        "Explain backpropagation step by step.",
        "What are vanishing/exploding gradients? How to fix them?",
        "Compare CNN, RNN, and Transformer architectures.",
        "What is attention mechanism and how does it work?",
    ],
    "🔤 NLP & LLMs": [
        "How does a Transformer architecture work?",
        "Explain BERT vs GPT training objectives.",
        "What is RAG and when would you use it?",
        "Explain fine-tuning vs prompt engineering trade-offs.",
    ],
    "⚙️ MLOps & System Design": [
        "How do you monitor ML models in production?",
        "Design an ML pipeline for a recommendation system.",
        "Explain A/B testing for ML models.",
        "What is model drift and how do you handle it?",
    ],
    "📊 Statistics & Math": [
        "Explain p-value in simple terms.",
        "What is the central limit theorem?",
        "Explain cross-entropy loss and when to use it.",
        "What is the difference between MLE and MAP?",
    ],
    "💻 Python & Coding": [
        "Implement a simple neural network from scratch in NumPy.",
        "How would you handle imbalanced datasets in Python?",
        "Explain Python generators and their use in ML.",
        "Write code for k-fold cross validation.",
    ],
}

SYSTEM_PROMPT = """You are an expert AI Engineering interview coach with deep knowledge in:
- Machine Learning (supervised, unsupervised, reinforcement learning)
- Deep Learning (CNNs, RNNs, Transformers, LLMs)
- NLP, LLMs, RAG, prompt engineering
- MLOps, model deployment, monitoring
- Statistics, probability, linear algebra
- Python, PyTorch, TensorFlow, scikit-learn

Your role is to help candidates prepare for AI/ML engineer interviews at top tech companies.

Guidelines:
1. Give clear, structured answers with examples
2. Include code snippets when relevant (in markdown code blocks)
3. Mention follow-up questions an interviewer might ask
4. Rate answer complexity as [Beginner] / [Intermediate] / [Advanced]
5. End responses with 1 follow-up question to deepen understanding
6. Be encouraging but honest about gaps

Format responses using markdown for readability."""

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "question_count" not in st.session_state:
    st.session_state.question_count = 0
if "selected_model" not in st.session_state:
    st.session_state.selected_model = list(FREE_MODELS.keys())[0]


# ── API call ──────────────────────────────────────────────────────────────────
def call_openrouter(messages: list, model_id: str, api_key: str) -> str:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://ai-interview-prep.streamlit.app",
        "X-Title": "AI Engineer Interview Prep",
    }
    payload = {
        "model": model_id,
        "messages": [{"role": "system", "content": SYSTEM_PROMPT}] + messages,
        "max_tokens": 1500,
        "temperature": 0.7,
    }
    try:
        r = requests.post(OPENROUTER_API_URL, headers=headers, json=payload, timeout=60)
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        if r.status_code == 401:
            return "❌ **Invalid API Key.** Please check your OpenRouter API key in the sidebar."
        elif r.status_code == 429:
            return "⏳ **Rate limited.** Please wait a moment and try again, or switch to a different model."
        elif r.status_code == 404:
            return f"❌ **Model not found.** The model `{model_id}` may no longer be available for free. Try switching to a different model in the sidebar."
        else:
            return f"❌ **API Error ({r.status_code}):** {str(e)}"
    except Exception as e:
        return f"❌ **Connection error:** {str(e)}"


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🔑 Configuration")
    
    api_key = st.text_input(
        "OpenRouter API Key",
        type="password",
        placeholder="sk-or-v1-...",
        help="Get a free key at openrouter.ai",
    )
    
    if not api_key:
        st.info("👆 Enter your free API key to start. Get one at [openrouter.ai](https://openrouter.ai)")

    st.markdown("### 🤖 Model")
    selected_model_name = "GPT-OSS 120B (OpenAI)"
    st.session_state.selected_model = selected_model_name
    model_id = FREE_MODELS[selected_model_name]
    st.markdown("**OpenAI: gpt-oss-120b** (free)")
    st.caption(f"`{model_id}`")

    st.markdown("---")
    st.markdown("### 📚 Question Bank")
    st.caption("Click a category to explore questions:")

    for cat, questions in CATEGORIES.items():
        with st.expander(cat):
            for q in questions:
                if st.button(q, key=f"sidebar_{q[:30]}", use_container_width=True):
                    st.session_state._sidebar_question = q

    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.question_count = 0
        st.rerun()

    st.markdown("---")
    st.markdown("""
    <div style='font-size:0.75rem; color:#374151; line-height:1.6'>
    <b style='color:#6366f1'>Free models via OpenRouter</b><br>
    No credit card needed.<br>
    Rate limits apply on free tier.
    </div>
    """, unsafe_allow_html=True)


# ── Main area ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-header">
    <p class="hero-title">⚡ AI Engineer Interview Prep</p>
    <p class="hero-sub">// Powered by OpenRouter Free LLMs &nbsp;·&nbsp; Ask anything about ML, DL, NLP, MLOps</p>
</div>
""", unsafe_allow_html=True)

# Stats bar
q_count = st.session_state.question_count
st.markdown(f"""
<div class="stats-bar">
    <div class="stat-chip">Questions asked: <span>{q_count}</span></div>
    <div class="stat-chip">Model: <span>{selected_model_name.split("(")[0].strip()}</span></div>
    <div class="stat-chip">Status: <span>{"🟢 Ready" if api_key else "🔴 No API Key"}</span></div>
</div>
""", unsafe_allow_html=True)

# Quick-start chips (only when no messages)
if not st.session_state.messages:
    st.markdown("**💡 Try a quick question:**")
    quick_questions = [
        "Explain transformers",
        "What is RAG?",
        "Bias-variance tradeoff",
        "Explain backprop",
        "LLM fine-tuning",
        "MLOps best practices",
    ]
    cols = st.columns(3)
    for i, q in enumerate(quick_questions):
        with cols[i % 3]:
            if st.button(q, key=f"quick_{q}", use_container_width=True):
                st.session_state._quick_question = q

# Chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="msg-user">
            <div class="msg-label">You</div>
            {msg["content"]}
        </div>
        """, unsafe_allow_html=True)
    else:
        with st.container():
            st.markdown(f'<div class="msg-label" style="color:#22d3ee;font-family:\'JetBrains Mono\',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.2rem">🤖 AI Coach</div>', unsafe_allow_html=True)
            st.markdown(msg["content"])
            st.markdown("---")

# ── Handle pre-selected questions ────────────────────────────────────────────
pending_q = None
if hasattr(st.session_state, "_sidebar_question"):
    pending_q = st.session_state._sidebar_question
    del st.session_state._sidebar_question
elif hasattr(st.session_state, "_quick_question"):
    pending_q = st.session_state._quick_question
    del st.session_state._quick_question

# ── Input form ────────────────────────────────────────────────────────────────
with st.container():
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input(
            "Ask an interview question...",
            value=pending_q or "",
            placeholder="e.g. How does attention mechanism work in Transformers?",
            label_visibility="collapsed",
            key="chat_input",
        )
    with col2:
        send = st.button("Send ➤", use_container_width=True)

# ── Process message ───────────────────────────────────────────────────────────
if (send or pending_q) and user_input.strip():
    if not api_key:
        st.error("Please enter your OpenRouter API key in the sidebar to continue.")
    else:
        st.session_state.messages.append({"role": "user", "content": user_input.strip()})
        st.session_state.question_count += 1

        with st.spinner("🧠 Thinking..."):
            reply = call_openrouter(
                st.session_state.messages,
                FREE_MODELS[st.session_state.selected_model],
                api_key,
            )

        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()
