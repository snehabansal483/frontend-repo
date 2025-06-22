# AI Interview Coach - Frontend Application

---

## 🚀 Demo

> **🎥 Click to watch the demo:**  
<p align="center">
  <a href="https://www.youtube.com/watch?v=uj4IVj0S-T8" target="_blank">
    <img src="https://github.com/snehabansal483/frontend-repo/blob/main/Screenshots/Ai%20Interview%20Coach.png" alt="Watch the demo" style="width: 80%; max-width: 600px;" />
  </a>
</p>

---




## 🔗 Related Repository

This frontend application works in conjunction with the backend API available at:  
👉 [snehabansal483/backend-repo](https://github.com/snehabansal483/backend-repo)

The backend is a Flask-based REST API that powers the interview question generation using Google's Gemini AI.

## Overview

The AI Interview Coach is a Streamlit-based web application designed to help job seekers prepare for interviews by generating tailored questions and model answers based on their target role, experience level, and background.

## Features

- 🎯 **Role-specific questions**: Generate interview questions tailored to your target job role
- 📊 **Experience-level customization**: Get questions appropriate for your career stage (Entry-level to Executive)
- 💡 **AI-powered answers**: Receive expert-crafted model answers to practice with
- 🏢 **Company-specific preparation**: Option to include specific companies in your preparation
- 🌙 **Dark/Light mode**: Automatically adapts to your system preferences

## Tech Stack Architecture

**Frontend**: 
- 🖥️ Streamlit (Python) - [Live Demo](https://interview-coach-frontend.onrender.com/)
- 🚀 Hosted on Render

**Backend**: 
- ⚙️ Flask REST API - [Live Demo](https://interview-coach-backend.onrender.com/)
- 🚀 Hosted on Render

 **Extension Download**: 
 
 - 📦 [Get it on Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/ai-interview-coach/)

**AI Core**:
- 🧠 Google's Gemini AI (integrated via backend API)

### Base URL
`https://interview-coach-frontend.onrender.com/`

## Directory Structure

```   
snehabansal483-frontend-repo/
    ├── README.md            # Readme file
    ├── app.py               # Main Streamlit application
    ├── requirements.txt     # Python dependencies
    └── Screenshots/         # Application screenshots
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/snehabansal483/frontend-repo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Configuration

The application is configured to connect to a backend service at `https://interview-coach-backend.onrender.com/`. To change this:

1. Open `app.py`
2. Modify the `BACKEND_URL` variable at the top of the file

## Usage

1. **Generate Questions**:
   - Enter your target job role (required)
   - Optionally specify company name and relevant projects
   - Select your experience level
   - Click "Generate Questions"

2. **Practice Answers**:
   - Select a generated question
   - Provide additional context about your background
   - Click "Generate Answer" to get a model response

## Screenshots

- Question Generation
![Question Generation Tab](https://github.com/snehabansal483/frontend-repo/blob/main/Screenshots/Questions%20generation.png) 

- Answer Practice
![Answer Practice Tab](https://github.com/snehabansal483/frontend-repo/blob/main/Screenshots/Answer%20generation.png) 

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact

For questions or feedback, please contact Sneha Bansal at snehabansal481@gmail.com
