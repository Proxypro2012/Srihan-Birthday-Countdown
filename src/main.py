import streamlit as st
from datetime import datetime
import time



st.set_page_config(page_title="Countdown to Srihan's Birthday")
r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 1])
r3col1, r3col2, r3col3 = st.columns([1, 2, 1])

with r1col2:
    st.title("🎉Countdown to Srihan's birthday")


target_time = datetime(2025, 6, 30, 0, 0, 0)

placeholder = st.empty()

for _ in range(9999999):
    now = datetime.now()
    remaining = target_time - now

    if remaining.total_seconds() <= 0:
        placeholder.markdown("## HAPPY BIRTHDAY SRIHAN! 🎂🎈")
        st.balloons()
        break

    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    with r2col2:
        placeholder.title("⏳ Time Remaining:")
    with r3col2:
        placeholder.write(f"**{days} days, {hours:02d} hours, {minutes:02d} minutes, {seconds:02d} seconds**")

    time.sleep(1)
