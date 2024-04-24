from openai import OpenAI, OpenAIError
import streamlit as st

# Read the API Key and Setup an OpenAI Client
try:
    with open("\python_code_review\openai key.txt") as f:
        key = f.read().strip()
        client = OpenAI(api_key=key)
except FileNotFoundError:
    st.error("API key file not found.")
    st.stop()
except OpenAIError as e:
    st.error(f"OpenAI Error: {e}")
    st.stop()

st.title("Python Code Reviewer")
st.subheader("Improves Code Quality 🛠️ & Sharpens Python Code")

# Take User's Input
prompt = st.text_area("Enter Your Python Code Here....", height=100)

# If the button is clicked, generate responses
if st.button("Generate"):
    if not prompt.strip():
        st.warning("Please enter some code.")
    else:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an AI assistant skilled in Python programming and debugging. Help users identify and fix errors in their Python code, offer suggestions for optimization, and provide guidance on using debugging tools and techniques. Share best practices for writing clean, efficient, and maintainable Python code."},
                    {"role": "user", "content": prompt}
                ]
            )
            corrected_code = response.choices[0].message.content
            st.write(corrected_code)
        except OpenAIError as e:
            st.error(f"OpenAI Error: {e}")