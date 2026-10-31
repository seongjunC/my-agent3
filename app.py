import streamlit as st
from dotenv import load_dotenv

load_dotenv()

page_01 = st.Page("page_01.py", title = '1페이지')
page_02 = st.Page("page_02.py", title = '2페이지')
page_03 = st.Page("page_03.py", title = '3페이지')

pages = st.navigation([page_01, page_02, page_03], position = 'top')

pages.run()