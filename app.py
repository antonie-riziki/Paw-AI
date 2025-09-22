import streamlit as st 
from st_social_media_links import SocialMediaIcons
from streamlit.components.v1 import html



reg_page = st.Page("./pgs/registration.py", title="register", icon=":material/person_add:")
signin_page = st.Page("./pgs/signin.py", title="sign in", icon=":material/login:")
home_page = st.Page("./pgs/main.py", title="home page", icon=":material/home:")
# starter_page = st.Page("./pgs/starter.py", title="Getting started", icon=":material/app_registration:")
# setup_page = st.Page("./pgs/setup.py", title="Setup & Installation", icon=":material/apk_install:")
# sms_service_page = st.Page("./pgs/sms_service.py", title="Messaging", icon=":material/sms:")
# airtime_page = st.Page("./pgs/airtime.py", title="Airtime", icon=":material/redeem:")
# mobile_data_page = st.Page("./pgs/mobile_data.py", title="Mobile Data", icon=":material/lte_plus_mobiledata_badge:")
# ussd_page = st.Page("./pgs/ussd.py", title="USSD", icon=":material/linked_services:")
# chatbot_page = st.Page("./pgs/chatbot.py", title="chatbot", icon=":material/chat:")


st.set_page_config(
    page_title="PAW AI",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.echominds.africa',
        'Report a bug': "https://www.echominds.africa",
        'About': """
        
        PAW AI (Predictive Animal Watch: AI-powered system) is a smart conservation platform designed to protect wildlife, prevent poaching, and support habitat and community engagement using real-time data, 
        machine learning, and communication tools.
        
        PAW AI combines GPS tracking, environmental sensors, and historical threat data to generate predictive insights and alerts. 
        It helps rangers and conservation managers plan effective patrols, monitor animal movements, detect threats (poaching, habitat encroachment), engage communities 
        through SMS/USSD or mobile platforms, and raise awareness through education tools.
        
        """
    }
)


with st.sidebar:
    button = """
        <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="echominds" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
        """

    html(button, height=70, width=220)
    st.markdown(
        """
        <style>
            iframe[width="220"] {
                position: fixed;
                bottom: 60px;
                right: 40px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


    social_media_links = [
        "https://www.x.com/am_tonie",
        "https://www.youtube.com/@echobytes-ke",
        "https://www.instagram.com/antonie_generall",
        "https://www.github.com/antonie-riziki",
    ]

    social_media_icons = SocialMediaIcons(social_media_links)

    social_media_icons.render()

pg = st.navigation([reg_page, signin_page, home_page])



pg.run()

