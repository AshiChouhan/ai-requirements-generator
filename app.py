import streamlit as str
from google import genai
from google.genai import types

# 1. Setup Web App Interface Title
str.title("📝 AI-Powered Business Requirements Generator")
str.write("Upload a raw client transcript to instantly generate structured Agile documentation.")

# 2. Get API Key Securely from User
api_key = str.text_input("Enter your Gemini API Key:", type="password")

# 3. Create File Upload UI Component
uploaded_file = str.file_uploader("Choose a transcript file (.txt)", type=["txt"])

if uploaded_file and api_key:
    # Read the text contents of the uploaded file
    raw_transcript = uploaded_file.read().decode("utf-8")
    
    if str.button("Generate Requirements Document"):
        with str.spinner("AI is analyzing your meeting transcript..."):
            try:
                # Initialize the Google GenAI Client
                client = genai.Client(api_key=api_key)
                
                # Create the instructions for the AI
                system_prompt = (
                    "You are an elite Business Analyst. Analyze the provided meeting transcript "
                    "and generate a professional project requirements document in Markdown format. "
                    "Include: 1) Executive Summary, 2) Core User Pain Points, and 3) Clean Agile User Stories "
                    "formatted strictly as 'As a... I want to... So that...' with clear acceptance criteria."
                )
                
                # Call the Gemini API model
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=f"{system_prompt}\n\nTranscript:\n{raw_transcript}"
                )
                
                # Display the finished Markdown text directly on the screen
                str.success("Generation Complete!")
                str.markdown("---")
                str.markdown(response.text)
                
                # Provide a button allowing the user to download the final document
                str.download_button(
                    label="📥 Download Requirements Document (.md)",
                    data=response.text,
                    file_name="Requirements_Document.md",
                    mime="text/markdown"
                )
                
            except Exception as e:
                str.error(f"An error occurred: {e}")