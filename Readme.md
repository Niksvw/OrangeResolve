# 🟧 OrangeResolve

## Smart Incident Resolution Platform

OrangeResolve is an enterprise-grade incident intelligence platform designed for DevOps and Platform teams. The application uses Semantic Search, FAISS Vector Database, Retrieval-Augmented Generation (RAG), and Groq-powered LLMs to analyze historical incidents and generate intelligent natural-language resolution recommendations.

The goal of OrangeResolve is to reduce MTTR (Mean Time To Resolution) by helping engineers quickly identify relevant historical incidents and recommended remediation actions.

---

# 🚀 Features

* Semantic Incident Search
* Retrieval-Augmented Generation (RAG)
* Intelligent Natural-Language Recommendations
* Historical Incident Correlation
* Fast Similarity Search using FAISS
* Groq LLM Integration
* Orange & White Enterprise UI
* Streamlit Deployment
* Scalable for large SNOW datasets

---

# 🛠️ Tech Stack

* Python
* Streamlit
* Sentence Transformers
* FAISS Vector Database
* Groq API
* Llama 3.3 70B Model
* Pandas
* NumPy

---

# 📂 Project Structure

```text
OrangeResolve/
│
├── app.py
├── rag_engine.py
├── utils.py
├── incidents.csv
├── requirements.txt
│
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/OrangeResolve.git
```

Navigate to the project directory:

```bash
cd OrangeResolve
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Groq API Setup

1. Generate your Groq API key from the Groq Console.

2. Inside the `.streamlit` folder, create a new file named `secrets.toml`.

3. Add the following configuration:

```toml
GROQ_API_KEY="your_actual_groq_api_key"
```

4. Save the file and restart the Streamlit application.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🌐 Streamlit Deployment

The application can be deployed for free using Streamlit Community Cloud.

1. Push the project to GitHub
2. Open Streamlit Community Cloud
3. Create a new app
4. Select the repository
5. Add the Groq API key in Streamlit Secrets
6. Deploy the application

---

# 🧠 How It Works

1. User enters an incident description
2. Sentence Transformer converts incident into embeddings
3. FAISS performs semantic similarity search
4. Relevant historical incidents are retrieved
5. Groq LLM analyzes the context
6. Natural-language resolution recommendation is generated

---

# 🎯 Use Cases

* Production Incident Resolution
* DevOps Incident Intelligence
* Platform Engineering Support
* Root Cause Assistance
* Operational Troubleshooting
* Historical Incident Analysis

---

# 📌 Example Query

```text
Production services are down since 1 hour
```

---

# 📌 Example Response

```text
Based on historical incidents INC0015 and INC0045, the issue appears similar to previous production outages caused by unstable backend services after deployment. It is recommended to restart the impacted services, validate connectivity between dependent systems, and review recent deployment logs to confirm whether any infrastructure changes triggered the outage.
```

---

# 👨‍💻 Developed For

Hackathons, DevOps innovation initiatives, and enterprise incident intelligence use cases.

---
