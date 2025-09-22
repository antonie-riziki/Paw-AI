from __future__ import annotations

import streamlit as st 
import sys

from datetime import datetime, timedelta


sys.path.insert(1, './modules')
# print(sys.path.insert(1, '../modules/'))


from dotenv import load_dotenv

load_dotenv()



st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h1 style="text-align: center; margin-top: -50px; color: #007B8A;">PAW AI 🐾</h1>
            <p style="text-align: center;">Guardians of the wild, powered by AI.</p>
        </div>
    </div> 
    """,
    unsafe_allow_html=True,
)

st.image('https://img.freepik.com/premium-vector/wild-animals-fauna-silhouettes-scene_24908-67621.jpg', width=900)