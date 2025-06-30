# Generative-AI
project on gen ai
# 🏙️ Sustainable Smart City Assistant

An AI-powered assistant that helps cities like Mumbai monitor sustainability indicators, detect anomalies, summarize policies, and provide eco-friendly tips using IBM's Granite LLM and an interactive Streamlit dashboard.

---

## 📌 Project Overview

The **Sustainable Smart City Assistant** is a modular application developed to support smart governance, urban planning, and eco-awareness using AI. It leverages IBM Watsonx Granite LLM to perform:

- 📊 Real-time dashboard display of city metrics (e.g., AQI, Water Supply, Waste)
- 🔍 Anomaly detection in energy/water/KPI datasets
- 🌱 Eco-tip generation using sustainability keywords
- 💬 Smart assistant chat for answering policy or environment-related questions
- 📄 Policy summarization (LLM-ready in future extensions)
- 📈 KPI forecasting (planned module)

---

## 🧠 Technologies Used

| Component             | Technology                             |
|----------------------|-----------------------------------------|
| 🧠 LLM                | IBM Watsonx Granite LLM (via HuggingFace) |
| 📊 Frontend           | Streamlit                               |
| ⚙️ Backend API        | Python / FastAPI (future expansion)     |
| 📁 Data Format        | JSON, CSV                               |
| 📈 ML Forecasting     | scikit-learn (Linear Regression)        |
| 🔍 Vector Search (opt)| Pinecone (for doc search)               |

---

## 🏗️ Project Structure

smart_city_assistant/
├── smart_city_app.py # Main Streamlit dashboard
├── smart_city_model.py # AI logic and function calls
├── city_data.json # Sample city data (Mumbai)
├── requirements.txt # Python dependencies
├── SmartCity_Documentation.pdf
├── Demo_Video.mp4 # Demo (or use Drive/YouTube link)
└── README.md # This file

yaml
Copy
Edit

---

## 🏙️ Features

### 🌇 City Dashboard (e.g., Mumbai)
- View **Air Quality**, **Water Supply**, **Energy Usage**, and more
- Get latest feedback indicators and environmental status

### 🧠 AI Smart Assistant
- Ask questions like:
  > “How to reduce pollution in cities?”
  > “What are Mumbai’s top sustainability concerns?”

### 🚨 Anomaly Detection
- Upload your KPI `.csv` file (must contain a "Value" column)
- See abnormal spikes in resource usage or waste generation

### 🌱 Eco Tips Generator
- Input any keyword like `"plastic"`, `"solar"`, or `"recycle"`
- Get actionable eco-friendly suggestions instantly from LLM

---

## ▶️ How to Run

### 🔧 1. Install dependencies

```bash
pip install -r requirements.txt
🚀 2. Start the App
bash
Copy
Edit
streamlit run smart_city_app.py
🖥️ 3. View in Browser
Localhost: http://localhost:8501

🧪 Sample Fake City Data (Mumbai)
This is a sample of the structured JSON file used:

json
Copy
Edit
{
  "Mumbai": {
    "AQI": 120,
    "Energy Usage": 75,
    "Water Supply": "Sufficient",
    "Waste Level": "Moderate",
    "Feedback": "Neutral",
    "Weather": "Cloudy",
    "Congestion": "High",
    "Alerts": "None",
    "Safety": "Moderate",
    "Health Index": "Fair"
  }
}
