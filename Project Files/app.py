import streamlit as st
from datetime import datetime
from utils import (
    load_cities, add_or_update_city, ask_question,
    summarize_text, extract_text, aqi_severity, export_city_report
)

st.set_page_config(page_title="Smart City Lite", layout="wide")
st.title("🏙️ Smart City Lite Assistant")

pages = ["Dashboard", "Chat Assistant", "Document Summarizer", "City Data Manager"]
choice = st.sidebar.radio("Choose Feature", pages)

cities = load_cities()
city_list = list(cities.keys())

if choice == "Dashboard":
    st.header("📊 City Dashboard")
    selected_city = st.selectbox("Select city", city_list)
    data = cities[selected_city]

    for key, info in data.items():
        value = info.get("value", "N/A")
        if key == "environment":
            label, color = aqi_severity(value)
            pct = int(value) if value.isdigit() else 0
            st.markdown(f"**{key.title()} (AQI): {label}**")
            st.progress(min(pct, 100))
        elif "%" in value:
            pct = int(value.replace("%", ""))
            st.markdown(f"**{key.title()}**")
            st.progress(min(pct, 100))
        else:
            st.markdown(f"**{key.title()}**: {value}")

    st.download_button("⬇️ Export City Report", export_city_report(selected_city), file_name=f"{selected_city}_report.txt")

elif choice == "Chat Assistant":
    st.header("🤖 Chat Assistant")
    city = st.selectbox("Select city", city_list)
    question = st.text_input("Ask a question about the city")
    if question:
        answer = ask_question(city, question)
        st.success(answer)
        st.download_button("⬇️ Download Response", answer, file_name=f"{city}_qa.txt")

elif choice == "Document Summarizer":
    st.header("📄 Document Summarizer")
    uploaded_file = st.file_uploader("Upload a TXT or PDF")
    if uploaded_file:
        text = extract_text(uploaded_file)
        if st.button("📝 Summarize"):
            summary = summarize_text(text)
            st.info(summary)
            st.download_button("⬇️ Download Summary", summary, file_name="summary.txt")

elif choice == "City Data Manager":
    st.header("🏗️ Manage City Data")
    selected = st.selectbox("Edit City", city_list)
    current = cities[selected]
    fields = list(current.keys())

    with st.form("edit_form"):
        new_data = {}
        for field in fields:
            val = current[field]["value"]
            user_val = st.text_input(f"{field.title()}", value=val)
            new_data[field] = {"value": user_val}
        if st.form_submit_button("💾 Save"):
            add_or_update_city(selected, new_data)
            st.success("City Updated.")

    st.markdown("### ➕ Add New City")
    new_city = st.text_input("Enter new city name")
    if st.button("Add City"):
        if new_city not in city_list:
            default = {k: {"value": "0"} for k in fields}
            add_or_update_city(new_city, default)
            st.success("City Added.")
