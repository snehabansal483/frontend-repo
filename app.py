import streamlit as st
import requests
import json


# Page setup
st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Configuration
BACKEND_URL = "https://interview-coach-backend.onrender.com/"  # Update if your backend is hosted elsewhere

def is_backend_live():
    try:
        response = requests.get(f"{BACKEND_URL}/health")  # Assumes your backend has a /health or similar route
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# Conditional warning
if not is_backend_live():
    st.warning("⚠️ Make sure to run the backend server before using the AI Interview Coach.")


def call_backend(endpoint, data):
    try:
        response = requests.post(f"{BACKEND_URL}/{endpoint}", json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}



# Custom CSS
# Update the Custom CSS section with this improved version:
st.markdown("""
    <style>
        /* Base styles that work in both light and dark modes */
        .main {
            background-color: var(--background-color);
        }
        .stTextInput input, .stTextArea textarea {
            border-radius: 10px;
            padding: 10px;
            background-color: var(--input-bg);
            color: var(--text-color);
        }
        .stButton button {
            background-color: #4a6fa5;
            color: white;
            border-radius: 10px;
            padding: 10px 24px;
            font-weight: bold;
            border: none;
        }
        .stButton button:hover {
            background-color: #3a5a80;
        }
        .question-card {
            background-color: var(--card-bg);
            color: var(--text-color);
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .answer-card {
            background-color: var(--answer-bg);
            color: var(--text-color);
            border-radius: 10px;
            padding: 20px;
            margin-top: 10px;
            border-left: 4px solid #4a6fa5;
        }
        
        /* Dark mode variables */
        @media (prefers-color-scheme: dark) {
            :root {
                --background-color: #0e1117;
                --text-color: #f0f2f6;
                --input-bg: #262730;
                --card-bg: #1a1c24;
                --answer-bg: #262730;
            }
        }
        
        /* Light mode variables */
        @media (prefers-color-scheme: light) {
            :root {
                --background-color: #f5f7fa;
                --text-color: #2c3e50;
                --input-bg: #ffffff;
                --card-bg: #ffffff;
                --answer-bg: #f0f4f8;
            }
        }
        
        /* Force dark text in specific elements if needed */
        .stMarkdown, .stText, .stExpander {
            color: var(--text-color) !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("💼 AI Interview Coach")
    st.markdown("""
        **Your personal interview preparation assistant**  
        Get tailored interview questions and expert answers for your dream job.
    """)
    
    st.markdown("---")
    st.markdown("### How to use:")
    st.markdown("1. Enter your target job role")
    st.markdown("2. Select your experience level")
    st.markdown("3. Get relevant questions")
    st.markdown("4. Practice with AI-generated answers")
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("This tool uses Google's Gemini AI to help you prepare for interviews by generating role-specific questions and model answers.")

# Main content
st.title("AI Interview Coach")
st.markdown("""
    Prepare for your next job interview with personalized questions and expert-crafted answers 
    tailored to your target role and experience level.
""")

# Tab interface
tab1, tab2 = st.tabs(["Generate Questions", "Practice Answers"])

with tab1:
    st.header("Generate Interview Questions")
    
    with st.form("question_form"):
        col1, col2 = st.columns(2)
        with col1:
            job_role = st.text_input("Job Role*", placeholder="e.g., Software Engineer")
            company_name = st.text_input("Company Name", placeholder="e.g., Google")
        with col2:
            experience_level = st.selectbox(
                "Experience Level",
                ("Entry-level", "Mid-level", "Senior", "Executive"),
                index=1
            )
            project = st.text_input("Your Relevant Project", placeholder="e.g., E-commerce platform")
        
        submitted = st.form_submit_button("Generate Questions")
        
        if submitted:
            if not job_role:
                st.error("Please enter a job role")
            else:
                with st.spinner("Generating tailored interview questions..."):
                    response = requests.post(
                        f"{BACKEND_URL}/generate-questions",
                        json={
                            "job_role": job_role,
                            "company_name": company_name,
                            "project": project,
                            "experience_level": experience_level.lower()
                        }
                    )
                    
                    if response.status_code == 200:
                        questions = response.json().get("questions", [])
                        # Store the original questions list in session state
                        st.session_state.questions_list = questions
                        st.session_state.job_role = job_role
                        st.session_state.company_name = company_name
                        st.session_state.project = project
                        
                        st.success(f"Questions tailored for {company_name or 'your target role'}:")
                        for i, question in enumerate(questions):
                            with st.expander(f"Question {i+1}"):
                                st.markdown(f"<div class='question-card'>{question}</div>", unsafe_allow_html=True)
                    else:
                        st.error(f"Error: {response.json().get('error', 'Unknown error')}")

with tab2:
    st.header("Practice with Model Answers")
    
    if "questions_list" not in st.session_state or not st.session_state.questions_list:
        st.warning("First generate questions in the previous tab")
    else:
        selected_question = st.selectbox(
            "Select a question to practice",
            st.session_state.questions_list
        )
        
        col1, col2 = st.columns(2)
        with col1:
            job_role_answer = st.text_input("Job Role (for answer)", value=st.session_state.get("job_role", ""))
            company_name_answer = st.text_input("Company Name (for answer)", value=st.session_state.get("company_name", ""))
        with col2:
            project_answer = st.text_input("Your Project (for answer)", value=st.session_state.get("project", ""))
        
        context = st.text_area("Additional Context About You", height=100,
                             placeholder="e.g., I led a team of 3 developers...")
        
        if st.button("Generate Answer"):
            with st.spinner("Generating expert answer..."):
                response = requests.post(
                    f"{BACKEND_URL}/generate-answer",
                    json={
                        "question": selected_question,
                        "job_role": job_role_answer,
                        "company_name": company_name_answer,
                        "project": project_answer,
                        "context": context
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    st.markdown("### Question")
                    st.markdown(f"<div class='question-card'>{selected_question}</div>", unsafe_allow_html=True)
                    
                    st.markdown("### Suggested Answer")
                    answer = data.get("answer", "")
                    st.markdown(f"<div class='answer-card'>{answer}</div>", unsafe_allow_html=True)
                else:
                    st.error(f"Error: {response.json().get('error', 'Unknown error')}")
