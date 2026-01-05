import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Earnings Report", layout="wide")

st.title("📊 Earnings Report")

with open("Earnings_2411091 (1) (1).html", "r", encoding="utf-8") as f:
    html_content = f.read()

html(html_content, height=1000, scrolling=True)
