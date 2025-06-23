import streamlit as st
from datetime import datetime
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
            placeholder_title.markdown("## HAPPY BIRTHDAY SRIHAN! 🎂🎈")
            placeholder_timer.empty()
            st.balloons()
            break

        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        placeholder_title.title("⏳ Time Remaining:")
        placeholder_timer.write(f"**{days} days, {hours:02d} hours, {minutes:02d} minutes, {seconds:02d} seconds**")

        time.sleep(1)
