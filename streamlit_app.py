import streamlit as st
import pandas as pd
import random
import time

# Load or initialize journal data
JOURNAL_FILE = "data/journal.csv"
try:
    journal_df = pd.read_csv(JOURNAL_FILE)
except FileNotFoundError:
    journal_df = pd.DataFrame(columns=["Date", "Mood", "Notes"])

# List of inspirational quotes
QUOTES = [
    "Keep going. Everything you need will come to you at the perfect time.",
    "Every day is a new beginning. Take a deep breath and start again.",
    "You are stronger than you think.",
    "Be kind to yourself. You are doing the best you can."
]

# Streamlit UI
st.set_page_config(page_title="Mental Well-Being", layout="centered", initial_sidebar_state="expanded")

st.sidebar.image("assets/logo.png", use_container_width=True)
st.sidebar.title("🌿 Mental Well-Being App")
page = st.sidebar.radio("Navigate", ["Daily Check-in", "Breathing Exercise", "Gratitude Journal", "Quotes", "Meditation Timer"])

if page == "Daily Check-in":
    st.title("📅 Daily Mood Check-in")
    
    mood = st.slider("How are you feeling today?", 1, 10, 5)
    notes = st.text_area("Journal your thoughts...")
    
    if st.button("Save Entry"):
        new_entry = pd.DataFrame([[pd.Timestamp.today().date(), mood, notes]], columns=["Date", "Mood", "Notes"])
        journal_df = pd.concat([journal_df, new_entry], ignore_index=True)
        journal_df.to_csv(JOURNAL_FILE, index=False)
        st.success("Entry saved successfully!")

elif page == "Breathing Exercise":
    st.title("🌬️ Guided Breathing Exercise")
    st.write("Follow the animation below for a **relaxing breathing session**.")

    col1, col2, col3 = st.columns(3)
    for i in range(3):
        with col1:
            st.write("Inhale... 😌")
            time.sleep(2)
        with col2:
            st.write("Hold... ⏳")
            time.sleep(2)
        with col3:
            st.write("Exhale... 🧘‍♂️")
            time.sleep(2)
    st.success("Well done! Keep practicing mindful breathing.")

elif page == "Gratitude Journal":
    st.title("🙏 Gratitude Journal")
    gratitude_text = st.text_area("What are you grateful for today?")
    
    if st.button("Save Gratitude"):
        with open("data/gratitude.txt", "a") as file:
            file.write(f"{pd.Timestamp.today().date()}: {gratitude_text}\n")
        st.success("Your gratitude note has been saved!")

elif page == "Quotes":
    st.title("💡 Daily Inspiration")
    st.write("Here's a **positive quote** to boost your day:")
    st.success(random.choice(QUOTES))

elif page == "Meditation Timer":
    st.title("🧘 Meditation Timer")
    duration = st.slider("Set meditation time (minutes)", 1, 30, 5)
    
    if st.button("Start Meditation"):
        with st.empty():
            for i in range(duration, 0, -1):
                st.write(f"🕰️ {i} minutes remaining...")
                time.sleep(60)
        st.success("Well done! Meditation complete. 🎉")

# Footer
st.sidebar.write("---")
st.sidebar.write("💙 Made with Streamlit")
