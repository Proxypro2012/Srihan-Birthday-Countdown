import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="Countdown to June 30, 2025")
st.title("🎉 Countdown to June 30, 2025")


target_time = datetime(2025, 6, 30, 0, 0, 0)

placeholder = st.empty()

for _ in range(9999999):
    now = datetime.now()
    remaining = target_time - now

    if remaining.total_seconds() <= 0:
        placeholder.markdown("## 🎊 It's June 30, 2025!")
        st.balloons()
        break

    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    placeholder.markdown(f"""
    ### ⏳ Time Remaining:
    **{days} days, {hours:02d} hours, {minutes:02d} minutes, {seconds:02d} seconds**
    """)
    
    time.sleep(1)
