# ⚡ AI Engineer Interview Prep Chatbot

An intelligent Q&A chatbot for AI/ML engineer interview preparation, powered by free LLMs via OpenRouter.

## ✨ Features

- 🤖 **Multiple Free LLM Models** — Gemma 3, Llama 3.1, Qwen3, Mistral, DeepSeek via OpenRouter
- 📚 **6 Topic Categories** — ML Fundamentals, Deep Learning, NLP/LLMs, MLOps, Statistics, Python
- 💬 **Conversational Memory** — Maintains chat context for follow-up questions
- 🎯 **Quick Question Chips** — One-click common interview topics
- 🌑 **Dark Terminal UI** — Clean, developer-friendly interface

## 🚀 Local Setup

### 1. Clone / download the project

```bash
cd ai_interview_chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Get a free OpenRouter API key

1. Go to [openrouter.ai](https://openrouter.ai)
2. Sign up (free, no credit card needed)
3. Navigate to **Keys** → Create a new key
4. Copy the key starting with `sk-or-v1-...`

### 4. Run locally

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## ☁️ Deploy to Streamlit Cloud

### Step 1 — Push to GitHub

1. Create a new GitHub repository (e.g., `ai-interview-chatbot`)
2. Push all files:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/ai-interview-chatbot.git
git push -u origin main
```

### Step 2 — Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click **"New app"**
4. Fill in:
   - **Repository:** `YOUR_USERNAME/ai-interview-chatbot`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click **"Deploy!"**

### Step 3 — Add API Key as Secret (Recommended)

Instead of users entering their own keys, you can pre-configure one:

1. In Streamlit Cloud, go to your app → **⋮ menu → Settings → Secrets**
2. Add:
```toml
OPENROUTER_API_KEY = "sk-or-v1-your-key-here"
```
3. In `app.py`, update the API key section to use:
```python
import os
api_key = st.secrets.get("OPENROUTER_API_KEY", "") or st.text_input(...)
```

---

## 📁 Project Structure

```
ai_interview_chatbot/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── .streamlit/
    └── config.toml         # Streamlit theme & server config
```

## 🆓 Free Models Available

| Model | Provider | Best For |
|-------|----------|---------|
| Gemma 3 27B | Google | Balanced, high quality |
| Llama 3.1 8B | Meta | Fast responses |
| Qwen3 8B | Alibaba | Math/coding heavy |
| Mistral 7B | Mistral AI | General Q&A |
| DeepSeek R1 | DeepSeek | Reasoning tasks |

## 📝 Topics Covered

- **ML Fundamentals** — bias-variance, overfitting, gradient descent, regularization
- **Deep Learning** — backprop, CNNs, RNNs, Transformers, attention
- **NLP & LLMs** — BERT, GPT, RAG, fine-tuning, prompt engineering
- **MLOps** — model monitoring, pipelines, A/B testing, drift detection
- **Statistics** — p-values, CLT, cross-entropy, MLE vs MAP
- **Python & Coding** — NumPy, PyTorch, sklearn implementations
