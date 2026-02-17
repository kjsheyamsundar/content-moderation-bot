# 🛡️ AI Content Moderation Bot

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![ML](https://img.shields.io/badge/Machine%20Learning-NLP-green.svg)
![Flask](https://img.shields.io/badge/Flask-API-red.svg)
![GitHub Pages](https://img.shields.io/badge/Hosted-GitHub%20Pages-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> An AI-powered content moderation system that automatically detects toxic content using Natural Language Processing and Machine Learning.

## 🌐 Live Demo
**[👉 Try it here: kjsheyamsundar.github.io/content-moderation-bot](https://kjsheyamsundar.github.io/content-moderation-bot/)**

---

## 📋 Table of Contents
- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [API Usage](#api-usage)
- [How It Works](#how-it-works)
- [Real World Application](#real-world-application)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## 🎯 About

During my 2 years working in the **Unacceptable Business Process (UBP)** department, I manually reviewed thousands of cases flagged by AI systems. I saw firsthand where automation succeeded and where it struggled.

This project was born from that experience — I wanted to **understand and build** the AI systems I worked with every day.

This system automatically detects toxic, hateful, and harmful content in text using state-of-the-art NLP models, reducing the burden on human moderators while maintaining high accuracy.

---

## ✨ Features

- 🤖 **AI-Powered Detection** - Uses BERT transformer model trained on millions of examples
- ⚡ **Real-time Analysis** - Instant toxicity detection with confidence scores
- 📊 **Batch Processing** - Analyze multiple texts in a single API call
- 🎯 **Adjustable Threshold** - Customize sensitivity based on your use case
- 📈 **Statistics Dashboard** - Track moderation metrics in real-time
- 📝 **Analysis History** - View recent moderation decisions
- 🌐 **REST API** - Easy integration with any application
- 💻 **Interactive UI** - Beautiful web interface for demos

---

## 🔧 Tech Stack

| Category | Technology |
|----------|-----------|
| **Language** | Python 3.9+ |
| **ML Framework** | PyTorch, Hugging Face Transformers |
| **NLP Model** | BERT (toxic-bert) |
| **API Framework** | Flask, Flask-CORS |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Version Control** | Git, GitHub |
| **Hosting** | GitHub Pages |
| **Data Processing** | Pandas, NumPy |

---

## 📁 Project Structure
```
content-moderation-bot/
│
├── src/
│   ├── moderator.py      # Core AI moderation engine
│   └── app.py            # Flask REST API
│
├── data/                 # Dataset storage
├── models/               # Saved model files
├── frontend/             # Frontend assets
├── index.html            # Main web interface
├── test_api.py           # API test scripts
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

---

## 🚀 Installation

### Prerequisites
- Python 3.9+
- pip
- Git

### Steps

**1. Clone the repository:**
```bash
git clone https://github.com/kjsheyamsundar/content-moderation-bot.git
cd content-moderation-bot
```

**2. Create virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the API:**
```bash
python src/app.py
```

**5. Open the website:**
```
http://localhost:5000
```

---

## 📡 API Usage

### Base URL
```
http://localhost:5000
```

### Endpoints

#### Check Single Text
```http
POST /moderate
Content-Type: application/json

{
    "text": "Your text here",
    "threshold": 0.5
}
```

**Response:**
```json
{
    "success": true,
    "result": {
        "text": "Your text here",
        "is_toxic": false,
        "confidence": 12.5,
        "status": "SAFE",
        "threshold": 50
    }
}
```

#### Batch Moderation
```http
POST /moderate/batch
Content-Type: application/json

{
    "texts": ["Text 1", "Text 2", "Text 3"],
    "threshold": 0.5
}
```

**Response:**
```json
{
    "success": true,
    "results": [...],
    "statistics": {
        "total": 3,
        "flagged": 1,
        "safe": 2,
        "flagged_percentage": 33.33
    }
}
```

#### Health Check
```http
GET /health
```

---

## 🧠 How It Works
```
User Input Text
      ↓
REST API (Flask)
      ↓
Content Moderator Class
      ↓
BERT Transformer Model
      ↓
NLP Processing Pipeline
      ↓
Toxicity Classification
      ↓
Confidence Score (0-100%)
      ↓
SAFE ✅ or FLAGGED 🚫
```

### Key Concepts:

**1. Tokenization** - Text is broken into tokens the model understands

**2. Transformer Model** - BERT analyzes context and meaning, not just keywords

**3. Confidence Scoring** - Model returns probability of toxicity (0-100%)

**4. Threshold System** - Configurable cutoff point for flagging content

---

## 🌍 Real World Applications

- 💬 **Social Media Platforms** - Auto-flag toxic comments
- 🎮 **Gaming** - Monitor in-game chat
- 🛒 **E-commerce** - Filter abusive reviews
- 💼 **Customer Service** - Protect support staff
- 📱 **Dating Apps** - Create safer environments
- 🏫 **Education Platforms** - Maintain healthy learning spaces

---

## 🔮 Future Improvements

- [ ] Multi-category detection (hate speech, threats, harassment separately)
- [ ] Multi-language support (Hindi, Tamil, Spanish)
- [ ] Image and video content moderation
- [ ] Analytics dashboard with trends
- [ ] AWS Lambda cloud deployment
- [ ] Model fine-tuning on domain-specific data
- [ ] User authentication for API
- [ ] Rate limiting and abuse prevention

---

## 👨‍💻 Author

**Sheyam** (kjsheyamsundar)

- 🎓 BCA Graduate - CMR University (2023)
- 💼 2 Years Experience - Content Moderation (UBP Department)
- 🚀 Transitioning into AI/ML Development

[![GitHub](https://img.shields.io/badge/GitHub-kjsheyamsundar-black.svg)](https://github.com/kjsheyamsundar)

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ **If you found this project helpful, please give it a star!** ⭐