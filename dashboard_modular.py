import streamlit as st
import sqlite3
from crisis_engine_modular import ai_tone_optimization, fetch_sentiment, recommend_action, trigger_workflow_alert, log_to_database

st.set_page_config(page_title="Crisis Decision Matrix Tool")
st.title("📊 Crisis Decision Matrix Dashboard")

menu = st.sidebar.selectbox("Menu", ["Audit Trail", "Templates", "Add Template"])

conn = sqlite3.connect("crisis_engine.db")
cursor = conn.cursor()

if menu == "Audit Trail":
    st.subheader("Audit Trail")
    cursor.execute("SELECT * FROM audit_trail ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    st.dataframe(rows)

elif menu == "Templates":
    st.subheader("Templates")
    cursor.execute("SELECT * FROM templates")
    templates = cursor.fetchall()
    for t in templates:
        st.markdown(f"**{t[1]}**")
        st.code(t[2])

elif menu == "Add Template":
    st.subheader("Add New Template")
    name = st.text_input("Template Name")
    content = st.text_area("Template Content")
    if st.button("Save Template"):
        cursor.execute("INSERT INTO templates (name, content) VALUES (?, ?)", (name, content))
        conn.commit()
        st.success("Template saved.")

st.sidebar.subheader("Run Decision Matrix")
input_text = st.sidebar.text_area("Enter input text")
if st.sidebar.button("Analyze"):
    tone = ai_tone_optimization(input_text)
    sentiment = fetch_sentiment(input_text)
    action = recommend_action(tone, sentiment)
    log_to_database(input_text, tone, sentiment, action)
    trigger_workflow_alert(f"Action Recommended: {action}")
    st.sidebar.success(f"Tone: {tone}, Sentiment: {sentiment}, Action: {action}")

conn.close()
