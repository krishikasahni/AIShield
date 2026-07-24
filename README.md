# 🛡️ AIShield

AIShield is an AI-powered Chrome Extension that detects spam comments on Instagram in real time. The extension automatically scans visible comments and highlights spam comments with a confidence score.

## 🚀 Features

- 🔍 Real-time Instagram comment scanning
- 🚩 Automatic spam comment highlighting
- 🌐 Chrome Extension

## 🔄 How To Use

1. User opens Instagram.
2. AIShield scans all visible comments.
3. Each comment is sent to the FastAPI backend.
4. The model predicts whether the comment is Spam or Not Spam.
5. Spam comments are highlighted with a confidence score.
6. New comments are automatically scanned while scrolling.

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AIShield.git
cd AIShield
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Backend

```bash
uvicorn backend.app:app --reload
```

Backend will start at:

```
http://127.0.0.1:8000
```

### Load Chrome Extension

1. Open Chrome
2. Navigate to `chrome://extensions`
3. Enable **Developer Mode**
4. Click **Load Unpacked**
5. Select the `extension` folder
   
## 📸 Screenshots

<img width="478" height="262" alt="Screenshot 2026-07-24 at 11 02 38 PM" src="https://github.com/user-attachments/assets/d7d3ded0-eedd-40fc-9ff5-f25c3e90d95b" />
