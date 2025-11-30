# 🚀 **Meeting2Action AI – Enterprise Workflow Automation Agent**

**Turn long meetings into clear, structured action items — automatically.**
*A privacy-first, multi-agent, on-device AI system with Netflix-style UI.*

---

# ⭐ **1. Overview**

**Meeting2Action AI** is an end-to-end **enterprise-grade workflow automation agent** that converts raw meeting transcripts into:

* 🎯 Clean summaries
* ✔ Action items
* ✔ Owners & due dates
* ✔ Auto-created tasks (Jira-style)
* ✔ Notifications
* ✔ Beautiful downloadable reports (DOCX, PDF, RTF)

All processing happens **locally** — ensuring **zero cloud exposure**, full **data privacy**, and **enterprise compliance**.

This project is designed for the **Enterprise Agents Track** of the Kaggle Agents Intensive Capstone.

---

# 🎯 **2. Problem Statement**

Enterprises conduct thousands of meetings every month.
Most problems arise due to:

* No clear meeting documentation
* Missing deadlines
* Ambiguous responsibilities
* No standardized action format
* Employees forgetting tasks
* Manual note-taking taking 20–30 mins per meeting

This leads to:

* Lost productivity
* Repeated discussions
* Misalignment
* Project delays

Thus, companies need a **reliable automated system** that can instantly transform conversation transcripts into structured, actionable reports.

---

# 💡 **3. Solution Summary**

**Meeting2Action AI** takes any meeting transcript and automatically:

1. **Summarizes** the entire meeting
2. **Extracts tasks** with owners + due dates
3. **Creates tasks** (simulated Jira issues)
4. **Sends notifications** (simulated email)
5. Generates a **professional report** in:

   * DOCX
   * PDF
   * RTF
6. Displays results in a **Netflix-style premium web UI**

Everything runs *offline*, *locally*, and *safely*.

---

# 🧠 **4. System Architecture (Multi-Agent Pipeline)**

```
 ┌────────────────────────────────────────────────────────────┐
 │                     MEETING2ACTION AI                      │
 └────────────────────────────────────────────────────────────┘
                │
                ▼
     ┌──────────────────────┐
     │   Summarizer Agent   │
     └──────────────────────┘
                │
                ▼
     ┌──────────────────────┐
     │  Extractor Agent     │
     │ (tasks, owners, due) │
     └──────────────────────┘
                │
                ▼
     ┌────────────────────────┐
     │   Task Creator Agent    │
     │   (Simulated Jira)      │
     └────────────────────────┘
                │
                ▼
     ┌────────────────────────┐
     │  Notification Agent     │
     │   (Simulated Email)     │
     └────────────────────────┘
                │
                ▼
     ┌──────────────────────────┐
     │  Report Generator Tool    │
     │ (DOCX / PDF / RTF files)  │
     └──────────────────────────┘
                │
                ▼
     ┌──────────────────────────┐
     │   Netflix-Styled UI       │
     └──────────────────────────┘
```

---

# 🔧 **5. ADK Features / LLM Concepts Used**

(Required by Kaggle Capstone)

| Feature Required        | Implemented?           | How it’s used                                                                 |
| ----------------------- | ---------------------- | ----------------------------------------------------------------------------- |
| Multi-Agent System      | ✅                      | Summarizer, Extractor, Task Creator, Notification Agent, Loop Coordinator     |
| Tools                   | ✅                      | Custom tools: Memory Store, Report Generator, Jira Simulator, Email Simulator |
| Long-Running Operations | ✅                      | Loop agent coordinating multiple steps                                        |
| Sessions & Memory       | ✅                      | Local memory files under `/mem/`                                              |
| Observability           | ✅                      | Logs stored under `/logs/`                                                    |
| Agent Evaluation        | ✅                      | Accuracy of owner/due extraction tested with eval module                      |
| Deployment              | ❗ Optional             | Runs locally via FastAPI + Uvicorn                                            |
| Use of Gemini           | ⚠️ Not used (no cloud) | Privacy-first local pipeline                                                  |

This satisfies the Kaggle requirement of **minimum 3 AI agent features**.
We are using **7**, which is exceptional.

---

# 🎨 **6. Netflix-Style Web UI (Premium Look)**

Your UI includes:

* Dark cinematic background
* Glassmorphism panels
* Neon red (Netflix) accents
* Smooth animations
* Clean layout
* Download buttons
* Live report viewer

### 📸 **Screenshots (add after running):**

```
/screenshots/ui_home.png
/screenshots/ui_report.png
/screenshots/ui_downloads.png
/screenshots/ui_transcript.png
```

---

# 📁 **7. Project Folder Structure**

```
Meeting2Action/
│
├── src/
│   ├── app.py                 # FastAPI app + UI
│   ├── coordinator.py         # Loop agent orchestrating pipeline
│   ├── agents/
│   │     ├── summarizer.py
│   │     ├── extractor.py
│   │     ├── task_creator.py
│   │     ├── notifier.py
│   │     └── __init__.py
│   │
│   ├── tools/
│   │     ├── report_tool.py   # DOCX, PDF, RTF generator
│   │     ├── memory_store.py  # Persistent storage
│   │     ├── jira_tool.py     # Fake Jira
│   │     ├── email_tool.py    # Fake email
│   │     └── __init__.py
│   │
│   ├── utils/
│   │     ├── text_utils.py
│   │     └── __init__.py
│   │
│   ├── evaluation/
│   │     ├── eval.py
│   │     └── sample_labels.json
│   │
│   └── __init__.py
│
├── templates/
│     └── index.html           # Netflix UI HTML
│
├── static/
│     ├── style.css            # Netflix theme CSS
│     └── app.js               # Frontend logic
│
├── data/
│     └── sample_transcript.txt
│
├── artifacts/
│     └── reports/             # Generated DOCX / PDF / RTF files
│
├── logs/
├── mem/
├── requirements.txt
└── README.md
```

---

# ▶️ **8. Installation & Run Instructions**

### **1. Clone the repo**

```
git clone https://github.com/<yourusername>/Meeting2Action.git
cd Meeting2Action
```

### **2. Create virtual environment**

```
python -m venv .venv
.venv\Scripts\activate
```

### **3. Install dependencies**

```
pip install -r requirements.txt
```

### **4. Run the app**

```
uvicorn src.app:app --reload --port 8080
```

### **5. Open in browser**

```
http://localhost:8080/
```

That’s it.
Your Netflix-style UI will load.

---

# 📘 **9. How to Use the Agent**

1. Paste meeting transcript
2. Enter Meeting ID (optional)
3. Click **PROCESS MEETING**
4. Agents run automatically
5. Final output appears in the right panel
6. Download DOCX/PDF/RTF report

---

# 🏆 **10. Example Output (Formatted Report)**

```
Meeting Summary: Q4 Sales Sync

Summary of Discussion:
- Reviewed sales deck progress
- Discussed upcoming deadlines
- Assigned budget approval task

Action Items:
1. Complete Sales Deck
   Owner: rohit@example.com
   Due: 2025-12-01

2. Review Budget Documentation
   Owner: alice@example.com
   Due: Not specified
```

Reports are stored under:

```
/artifacts/reports/
```

---

# 🔒 **11. Privacy & Compliance**

This system is **100% offline**:

* No cloud APIs
* No external LLMs
* No data sent to internet
* All docs stored locally
* Runs safely inside corporate laptops

This solves the biggest enterprise concern:
**meeting transcripts often contain secret, confidential information.**

---

# 🧪 **12. Evaluation Module**

We evaluated extraction quality using labeled test data.

Sample:

```
Owner Extraction F1: 1.00
Due Date Extraction F1: 0.67
```

Evaluation file located at:

```
src/evaluation/eval.py
```

---

# 🎉 **13. Why This Project Stands Out**

* Multi-agent architecture
* Netflix-level UI
* DOCX, PDF, RTF report generation
* Local privacy-first processing
* Strong enterprise use case
* Beautiful and smooth user experience
* Fully modular and extensible
* Beginner-friendly setup
* Perfect Kaggle writeup flow

---

# 👑 **14. Author**

**Sneha Mekala**
AI · Data Science · Enterprise Automation
Meeting-to-Action AI – Kaggle Capstone Project
2025

or
**“Continue with video script”**
