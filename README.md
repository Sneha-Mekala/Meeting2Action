# Meeting-To-Action AI  
### A Local Multi-Agent Workflow Automation System (No Cloud, No Billing)

This project converts **meeting transcripts → action items → tasks → notifications**,  
using a fully **local**, **privacy-safe** multi-agent pipeline.

This project is created for the **Kaggle Agents Intensive Capstone Project (Enterprise Track)**  
by **Sneha Mekala**.

---

# 💡 Why This Project?

Organizations often struggle with:
- Missing meeting notes  
- Lost action items  
- Forgotten deadlines  
- Manual transcription  
- No central tracking  
- Noise in communication  
- Privacy concerns about sending data outside the company  

This agent solves all of these problems **locally**, without any cloud or external servers.

---

# 🧩 Multi-Agent Architecture

### The system uses 5 dedicated agents:

1. **Summarizer Agent**  
   Creates a short summary of the meeting.

2. **Extractor Agent**  
   Extracts tasks, owners, and deadlines from text.

3. **Task Creator Agent**  
   Creates tasks in:
   - Local Jira mock (JSON file)
   - Sheet tracker (CSV file)

4. **Notifier Agent**  
   Sends notifications to owners (stored in `logs/email_log.json`).

5. **Loop Agent**  
   Long-running agent that automatically follows up on meetings without a follow-up flag.

### Coordinator  
All agents are orchestrated by a `Coordinator` which runs the entire workflow.

---

# 🔒 Privacy & Security

✔ 100% **local processing**  
✔ No cloud (no GCP, no AWS, no external APIs)  
✔ No billing  
✔ No external servers  
✔ Enterprises can run the agent **inside their own private environment**  
✔ Sensitive meeting data stays fully inside the organization  

---

# 🚀 Features Demonstrated

This project meets the **Kaggle Capstone minimum requirements**:

- Multi-Agent System  
- Custom Tools  
- Long-Running Operations  
- Memory System  
- Observability (local logs & artifacts)  
- Evaluation Script  
- (Optional Bonus) Local Deployment via FastAPI  
- (Optional Bonus) Dockerfile  

---

# 📁 Project Structure