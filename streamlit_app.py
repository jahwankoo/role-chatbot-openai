# streamlit_app.py
import streamlit as st
from openai import OpenAI

# -----------------------
# 1. Page Configuration
# -----------------------
st.set_page_config(page_title="🎭 Role-based Creative Chatbot", layout="wide")
st.title("🎭 Role-based Creative Chatbot")
st.write("Select a creative role and ask your question!")

# -----------------------
# 2. Sidebar Role Selection
# -----------------------
roles = {
    "🎥 Video Director": "You are a professional film director. You analyze camera angles, lighting, and emotion in each scene.",
    "💃 Dance Instructor": "You are a dance instructor. You teach movement, rhythm, and body expression in artistic ways.",
    "👗 Fashion Stylist": "You are a fashion stylist. You suggest styles, colors, and materials that match the client’s mood.",
    "🎭 Acting Coach": "You are an acting coach. You guide emotional delivery and body language for stage performance.",
    "🎨 Art Curator": "You are an art curator. You interpret artworks and explain their aesthetic and emotional meaning."
}

role_name = st.sidebar.selectbox("Choose a role:", list(roles.keys()))
role_description = roles[role_name]
st.sidebar.write(role_description)

# -----------------------
# 3. User Input
# -----------------------
user_input = st.text_area("💬 Enter your question or idea:", height=100, placeholder="e.g., How can I express sadness in movement?")

# -----------------------
# 4. Chatbot Response
# -----------------------
if st.button("Generate Response"):
    if not user_input:
        st.warning("Please enter a question first!")
    else:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])  # store key in Streamlit Cloud secrets
        with st.spinner("AI is thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": role_description},
                    {"role": "user", "content": user_input}
                ]
            )
            answer = response.choices[0].message.content
            st.success("🎬 Response:")
            st.write(answer)

# -----------------------
# 5. Footer
# -----------------------
st.markdown("---")
st.caption("Built for 'Art & Advanced Big Data' • Prof. Jahwan Koo (SKKU)")
