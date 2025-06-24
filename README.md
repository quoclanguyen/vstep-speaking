# 🎤 VSTEP Speaking Evaluation App

A web application that allows users to upload `.wav` audio responses to VSTEP speaking questions and receive detailed evaluations. The app assesses pronunciation, grammar, fluency, and coherence using AI (Gemini or OpenAI), and displays feedback in rendered Markdown format.

---

## 🚀 Features

- 🎧 Upload `.wav` audio files
- ✍️ Submit custom speaking prompts
- 🤖 AI-powered assessment using Gemini (or OpenAI as fallback)
- 📝 Feedback rendered in Markdown (grammar errors highlighted)
- 🔊 Audio playback preview
- ⏳ Loading animation with “Evaluating…” message
- 📦 Easy to deploy with FastAPI & TailwindCSS

---

## 📁 Project Structure
```
project-root/
├── static/
│ └── icons/
│ └── favicon.ico
├── templates/
│ └── index.html 
├── uploads/ 
├── main.py 
├── utils.py 
├── README.md
```

---

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI, Gemini / OpenAI API
- **Frontend**: TailwindCSS, Jinja2, Marked.js (for Markdown rendering)
- **Speech-to-text**: Google Speech or Whisper (configurable)
- **Grammar analysis**: AI-based or `language_tool_python` (optional)

--- 

## Visit demo website
Click [here](https://vstep-speaking.onrender.com/)