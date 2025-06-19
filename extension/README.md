
# AI Interview Coach – Firefox Extension

## 🔍 Overview

**AI Interview Coach** is a Firefox extension that connects to a Flask-based backend powered by Google's Gemini AI to help users generate personalized interview questions and answers. It works seamlessly with a Streamlit-based frontend and is built for candidates preparing for tech or non-tech roles.

This extension enhances your interview prep by allowing you to input job-related information directly from your browser and instantly receive tailored questions or AI-generated model answers.

---

## ✨ Features

- 🎯 Role-specific question generation
- 💬 AI-generated model answers
- 🧠 Context-aware suggestions (based on job, company, projects)
- 🔐 Private and secure communication with backend
- 🖥️ Seamless integration with the existing backend API

---

## 🧱 Tech Stack

- **Frontend UI**: Streamlit (Python)
- **Extension Backend**: Flask REST API
- **AI Integration**: Google's Gemini AI
- **Hosting**: Render.com

---

## 📡 API Base URL

```
https://interview-coach-backend.onrender.com/
```

---

## 📁 Project Structure

```
ai-interview-coach-extension/
├── manifest.json          # Firefox extension manifest
├── popup.html             # UI popup
├── popup.js               # JS logic for interacting with the API
├── style.css              # Minimal CSS styling
├── icons/                 # Extension icons
└── README.md              # Project README
```

---

## 🔐 Privacy Policy

**Effective Date:** June 17, 2025

AI Interview Coach is a Firefox Extension designed to help users prepare for job interviews by generating personalized AI-powered questions and answers. We are committed to maintaining your privacy and being transparent about how your data is used.

### 1. Information We Collect

The extension may temporarily access:

- Text inputted by the user (e.g., job role, company name, project experience)
- Generated interview questions or answers

We **do not collect or store**:
- User identity (email, name, credentials)
- Authentication tokens or passwords
- Unrelated page content or browsing data

### 2. How We Use Your Data

User inputs are sent securely to our backend API at:

```
https://interview-coach-backend.onrender.com
```

This data is used solely to:
- Generate interview questions
- Provide model answers

Data is processed in real-time and **not stored** after the request is completed.

### 3. Data Sharing

We **do not sell, rent, or share** any user data. All processing is local to the extension and our backend.

### 4. Data Security

All communication uses HTTPS for secure transmission. While no system is completely secure, we implement best practices to protect your data in transit.

### 5. User Control

- You may uninstall the extension at any time.
- The extension does not store any persistent data.

### 6. Changes to This Policy

We may revise this Privacy Policy as necessary. Changes will be updated in this README with a revised effective date.

### 7. Contact

📧 [Sneha Bansal](mailto:snehabansal481@gmail.com)  
🔗 [Frontend GitHub](https://github.com/snehabansal483/frontend-repo)  
🔗 [Backend GitHub](https://github.com/snehabansal483/backend-repo)

---

## 🤝 Contributing

Feel free to open issues or pull requests to improve the extension.

---