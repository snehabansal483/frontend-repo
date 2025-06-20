// Full popup.js file with DOMPurify sanitation

const backend = "https://interview-coach-backend.onrender.com/";

document.addEventListener("DOMContentLoaded", () => {
  const tab1 = document.getElementById("tab1");
  const tab2 = document.getElementById("tab2");
  const tabQuestions = document.getElementById("tabQuestions");
  const tabAnswers = document.getElementById("tabAnswers");
  const questionsContainer = document.getElementById("questionsContainer");
  const questionSelect = document.getElementById("questionSelect");
  const answerContainer = document.getElementById("answerContainer");
  const questionsLoading = document.getElementById("questionsLoading");
  const answerLoading = document.getElementById("answerLoading");

  // Tab switch
  tabQuestions.addEventListener("click", () => {
    tab1.classList.add("active");
    tab2.classList.remove("active");
    tabQuestions.classList.add("active");
    tabAnswers.classList.remove("active");
  });

  tabAnswers.addEventListener("click", () => {
    tab2.classList.add("active");
    tab1.classList.remove("active");
    tabAnswers.classList.add("active");
    tabQuestions.classList.remove("active");
  });

  // Generate Questions
  document.getElementById("generateQuestionsBtn").addEventListener("click", async () => {
    const jobRole = document.getElementById("jobRole").value;
    if (!jobRole) {
      showError("Please enter a job role");
      return;
    }

    const companyName = document.getElementById("companyName").value;
    const project = document.getElementById("project").value;
    const experience = document.getElementById("experienceLevel").value;

    questionsContainer.innerHTML = "";
    questionsLoading.classList.remove("hidden");

    try {
      const res = await fetch(`${backend}/generate-questions`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          job_role: jobRole, 
          company_name: companyName, 
          project, 
          experience_level: experience 
        })
      });

      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.error || "Failed to generate questions");
      }

      const data = await res.json();
      let questions = Array.isArray(data.questions) ? 
        data.questions : 
        (data.questions || "").split("\n").filter(q => q.trim());

      if (questions.length === 0) throw new Error("No questions generated");

      renderQuestions(questions);
      document.getElementById("jobRoleAnswer").value = jobRole;
      tabAnswers.click();
      if (questionSelect.options.length > 1) {
        questionSelect.selectedIndex = 1;
      }
    } catch (error) {
      showError(error.message);
    } finally {
      questionsLoading.classList.add("hidden");
    }
  });

  // Generate Answer
  document.getElementById("generateAnswerBtn").addEventListener("click", async () => {
    const question = questionSelect.value;
    if (!question || question.startsWith("--")) {
      showError("Please select a question");
      return;
    }

    const job_role = document.getElementById("jobRoleAnswer").value;
    const company_name = document.getElementById("companyAnswer").value;
    const project = document.getElementById("projectAnswer").value;
    const context = document.getElementById("context").value;

    answerContainer.innerHTML = "";
    answerLoading.classList.remove("hidden");

    try {
      const res = await fetch(`${backend}/generate-answer`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          question, 
          job_role, 
          company_name, 
          project, 
          context 
        })
      });

      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.error || "Failed to generate answer");
      }

      const data = await res.json();
      renderAnswer(data.answer || "No answer generated");
    } catch (error) {
      showError(error.message);
    } finally {
      answerLoading.classList.add("hidden");
    }
  });

  function renderQuestions(questions) {
    questionsContainer.innerHTML = "";
    questionSelect.innerHTML = `<option disabled selected>-- Select a question --</option>`;

    questions.forEach((q, idx) => {
      const cleanQuestion = q.replace(/^\d+\.\s*/, '').trim();

      const div = document.createElement("div");
      div.className = "card question-card";
      div.innerHTML = DOMPurify.sanitize(`<strong>Q${idx + 1}:</strong> ${cleanQuestion}`);
      questionsContainer.appendChild(div);

      const option = document.createElement("option");
      option.value = cleanQuestion;
      const displayText = cleanQuestion.length > 50 ? 
        cleanQuestion.substring(0, 47) + "..." : 
        cleanQuestion;
      option.innerHTML = DOMPurify.sanitize(`Q${idx + 1}: ${displayText}`);
      option.title = cleanQuestion;
      questionSelect.appendChild(option);
    });
  }

  function renderAnswer(answer) {
    answerContainer.innerHTML = DOMPurify.sanitize(`
      <div class="card answer-card">
        <strong>Suggested Answer:</strong><br><br>
        ${answer.replace(/\n/g, '<br>')}
      </div>
      <div class="card tips-card">
        <strong>Tips:</strong><br><br>
        <ul>
          <li>Practice saying this out loud</li>
          <li>Tailor it to your specific experience</li>
          <li>Keep it concise (1-2 minutes)</li>
          <li>Highlight your achievements</li>
        </ul>
      </div>
    `);
  }

  function showError(message) {
    const errorDiv = document.createElement("div");
    errorDiv.className = "card error-card";
    errorDiv.innerHTML = DOMPurify.sanitize(`<strong>Error:</strong> ${message}`);

    if (tab1.classList.contains("active")) {
      questionsContainer.innerHTML = "";
      questionsContainer.appendChild(errorDiv);
    } else {
      answerContainer.innerHTML = "";
      answerContainer.appendChild(errorDiv);
    }
  }
});
