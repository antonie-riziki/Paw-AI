import streamlit as st
import pandas as pd
import africastalking
import os
import sys
import requests
import google.generativeai as genai


sys.path.insert(1, './modules')

# from upload_file_rag import get_qa_chain, query_system
from func import welcome_message, send_otp

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

africastalking.initialize(
    username='EMID',
    api_key = os.getenv("AT_API_KEY")
)

sms = africastalking.SMS
airtime = africastalking.Airtime




col1, col2 = st.columns(2)




with col1:
	with st.form(key="user_registration"):
		st.subheader("Registration")
		fname, sname = st.columns(2)
		with fname:
			first_name = st.text_input("First Name")
		with sname:
			surname = st.text_input("Surname")	
		username = st.text_input('Username:')
		email = st.text_input("Email: ")
		phone_number = st.number_input("Phone Number:", value=None, min_value=0, max_value=int(10e10))
		password = st.text_input('Passowrd', type="password")
		confirm_password = st.text_input('Confirm password', type='password')
		face_id = st.file_uploader('Profile Photo')
		checkbox_val = st.checkbox("Subscribe to our Newsletter")
		submit_personal_details = st.form_submit_button("Create account", use_container_width=True, type="primary")
		if password != confirm_password:
			st.error('Password mismatch', icon='⚠️')
		else:
			if not (email and password):
				st.warning('Please enter your credentials!', icon='⚠️')
			else:
				st.success('Proceed to engaging with the system!', icon='👉')
				if submit_personal_details:
					welcome_message(first_name, phone_number)



with col2:
	st.image('https://www.azolifesciences.com/images/Article_Images/ImageForArticle_714_16449362895935733.jpg', width=700)
	st.image('https://detroitzooblog.org/wp-content/uploads/2022/08/adobestock_41579093597.jpg', width=800)
	st.image('https://risemalaysia.com.my/wp-content/uploads/2024/01/Wildlife-jpg.webp', width=900)