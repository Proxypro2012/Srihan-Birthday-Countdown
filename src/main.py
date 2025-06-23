import streamlit as st
from datetime import datetime
from streamlit_extras.let_it_rain import rain
import time

st.set_page_config(page_title="Countdown to Srihan's Birthday")

# Create three columns: middle column is wider
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.title("🎉 Countdown to Srihan's Birthday")

    target_time = datetime(2025, 6, 30, 0, 0, 0)
    placeholder_title = st.empty()
    placeholder_timer = st.empty()

    for _ in range(9999999):
        now = datetime.now()
        remaining = target_time - now

        if remaining.total_seconds() <= 0:
            placeholder_title.markdown(
                "<h2 style='text-align:center; color:#FF4B4B;'>🎉 HAPPY BIRTHDAY SRIHAN! 🎂🎈</h2>", 
                unsafe_allow_html=True
            )
            placeholder_timer.empty()
            st.balloons()
            break

        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Smaller but bold for "Time Remaining:"
        placeholder_title.markdown(
            "<h3 style='text-align:center; color:#333;'>⏳ Time Remaining:</h3>", 
            unsafe_allow_html=True
        )

        # Larger countdown timer, centered, no line breaks
        countdown_html = f"""
        <p style='font-size:48px; font-weight:bold; text-align:center; margin:0; color:#111;'>
            {days} days, {hours:02d} hours, {minutes:02d} minutes, {seconds:02d} seconds
        </p>
        """
        placeholder_timer.markdown(countdown_html, unsafe_allow_html=True)

        time.sleep(1)

rain('•', 20, falling_speed=5, animation_length="infinite")