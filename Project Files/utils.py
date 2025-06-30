import os, json, torch
from datetime import datetime
import PyPDF2
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

MODEL_ID = "ibm-granite/granite-3.3-2b-instruct"
HUGGINGFACE_HUB_TOKEN = os.getenv("HUGGINGFACE_HUB_TOKEN")
CITY_DATA_PATH = "data/cities.json"

# === Load AI model ===
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, token=HUGGINGFACE_HUB_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(MODEL_ID, token=HUGGINGFACE_HUB_TOKEN)
    return pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

pipe = load_model()

# === City Data Handling ===
def load_cities():
    if not os.path.exists(CITY_DATA_PATH):
        return {}
    with open(CITY_DATA_PATH, "r") as f:
        return json.load(f)

def save_cities(data):
    with open(CITY_DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)

def add_or_update_city(name, data):
    cities = load_cities()
    data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cities[name] = data
    save_cities(cities)

# === AI Functions ===
def ask_question(city, question):
    info = load_cities().get(city, {})
    prompt = f"""You are a helpful Smart City AI Assistant.

City: {city}
Data: {json.dumps(info)}

Question: {question}
"""
    result = pipe(prompt, max_new_tokens=300)[0]["generated_text"]
    return result.replace(prompt, "").strip()

def summarize_text(text):
    prompt = f"Summarize this document:\n{text[:3500]}"
    result = pipe(prompt, max_new_tokens=250)[0]["generated_text"]
    return result.replace(prompt, "").strip()

def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""

def aqi_severity(aqi_val):
    try:
        aqi = int(aqi_val)
        if aqi <= 50:
            return "Good", "#00FF00"
        elif aqi <= 100:
            return "Moderate", "#FFFF00"
        elif aqi <= 150:
            return "Unhealthy (Sensitive)", "#FFA500"
        elif aqi <= 200:
            return "Unhealthy", "#FF0000"
        elif aqi <= 300:
            return "Very Unhealthy", "#800080"
        else:
            return "Hazardous", "#800000"
    except:
        return "Unknown", "#555555"

def export_city_report(city_name):
    data = load_cities().get(city_name, {})
    lines = [f"{city_name} Smart City Report\n", "-"*40]
    for k, v in data.items():
        lines.append(f"{k.title()}: {v.get('value', 'N/A')}")
    return "\n".join(lines)
