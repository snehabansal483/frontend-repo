# AI Interview Coach - Frontend Application

![AI Interview Coach Screenshot]()

## Overview

The AI Interview Coach is a Streamlit-based web application designed to help job seekers prepare for interviews by generating tailored questions and model answers based on their target role, experience level, and background.

## Features

- 🎯 **Role-specific questions**: Generate interview questions tailored to your target job role
- 📊 **Experience-level customization**: Get questions appropriate for your career stage (Entry-level to Executive)
- 💡 **AI-powered answers**: Receive expert-crafted model answers to practice with
- 🏢 **Company-specific preparation**: Option to include specific companies in your preparation
- 🌙 **Dark/Light mode**: Automatically adapts to your system preferences

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: REST API (hosted separately)
- **AI**: Google's Gemini AI (via backend)

## Directory Structure

```
snehabansal483-frontend-repo/
├── app.py               # Main Streamlit application
└── requirements.txt     # Python dependencies
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

![Question Generation Tab]() 

![Answer Practice Tab]() 

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact

For questions or feedback, please contact Sneha Bansal at snehabansal481@gmail.com
