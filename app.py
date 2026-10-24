import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Kalviora AI - CEO Dashboard", page_icon="🤖", layout="wide")

st.title("🚀 Kalviora AI - Autonomous CEO Dashboard")
st.markdown("Aapka AI CEO agent yahan se saari marketing, sales, aur social media tasks ko manage karega!")

# Sidebar for API Key & Settings
st.sidebar.header("⚙️ Settings & API Key")
api_key_input = st.sidebar.text_input("Gemini API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))

user_instruction = st.text_area(
    "💡 CEO Agent ko kya instruction ya goal dena chahte hain?",
    value="Scale Kalviora AI to achieve 100 daily paid users through organic marketing, social media automation, and sales funnels."
)

if st.button("🚀 Run AI CEO Agent"):
    if not api_key_input:
        st.error("❌ Pehle apni Gemini API Key enter karein ya .env file check karein!")
    else:
        with st.spinner("🤖 AI CEO planning kar raha hai aur agents ko tasks delegate kar raha hai..."):
            try:
                client = genai.Client(api_key=api_key_input)
                
                ceo_prompt = f"""
                You are the autonomous AI CEO of Kalviora AI. 
                Your founder's primary instruction is: "{user_instruction}"

                As the CEO, you must:
                1. Analyze this goal deeply.
                2. Break it down into step-by-step actionable tasks for your specialized subordinate agents (Growth Marketer, Social Media Manager, Sales & Outreach Agent).
                3. Provide a clear, executed blueprint and daily schedule to achieve this goal successfully.
                """

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=ceo_prompt,
                )
                
                ceo_output = response.text

                st.success("✅ CEO Execution Report Successfully Generated!")
                st.markdown("### 📋 CEO Agent Execution Report & Plan:")
                st.markdown(ceo_output)

                st.download_button(
                    label="📥 Download CEO Report (.txt)",
                    data=ceo_output,
                    file_name="ceo_daily_report.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"❌ Error aagya: {e}")
