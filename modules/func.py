import string
import random
import secrets
import requests
import re
import os 
import bcrypt
import africastalking
import streamlit as st 
import google.generativeai as genai
import base64


from io import BytesIO
from dotenv import load_dotenv
from google.genai import types



# from google.generativeai.types import GenerationConfig


load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

africastalking.initialize(
    username='EMID',
    api_key = os.getenv("AT_API_KEY")
)

nvidia_api = os.getenv("NVIDIA_API_KEY")

sms = africastalking.SMS
airtime = africastalking.Airtime
voice = africastalking.Voice

def send_otp(phone_number, otp_sms):

    recipients = [f"+254{str(phone_number)}"]

    print(recipients)
    print(phone_number)

    # Set your message
    message = f"{otp_sms}";

    # Set your shortCode or senderId
    sender = 20880

    try:
        response = sms.send(message, recipients, sender)

        print(response)


    except Exception as e:
        print(f'Houston, we have a problem: {e}')

    st.toast(f"OTP Sent Successfully")





def welcome_message(first_name, phone_number):

    recipients = [f"+254{str(phone_number)}"]

    print(recipients)
    print(phone_number)

    # Set your message
    message = f"""
    
    {first_name}, welcome aboard to PAW AI! Start exploring animal tracks, conservation alerts and act to protect wildlife. 
    
    """;

    # Set your shortCode or senderId
    sender = 20880

    try:
        response = sms.send(message, recipients, sender)

        print(response)

    except Exception as e:
        print(f'Houston, we have a problem: {e}')

    st.toast(f"Account Created Successfully")



def make_call(phone_number):    
  
  # Set your Africa's Talking phone number in international format
    callFrom = "+254730731123"
  
  # Set the numbers you want to call to in a comma-separated list
    callTo   = [f"+254{str(phone_number)}"]
    
    try:
  # Make the call
        result = voice.call(callFrom, callTo)
        # print (result)
        return result
    except Exception as e:
        # print ("Encountered an error while making the call:%s" %str(e))
        return f"Encountered an error while making the call:%s" %str(e)



def generate_otp(length=6):
    characters = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))



def check_and_encrypt_password(password: str, confirm_password: str):
    
    if password != confirm_password:
        return st.error("Error: Passwords do not match!")

    if len(password) < 8:
        return st.error(f"Error: Password must be at least 8 characters long!")
    
    if not re.search(r"[A-Z]", password):
        return st.error(f"Error: Password must contain at least one uppercase letter!")
    
    if not re.search(r"\d", password):
        return st.error(f"Error: Password must contain at least one number!")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return st.error(f"Error: Password must contain at least one special character!")

    # Encrypt password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    return st.text_input(label='Encrypted password', value=hashed_password.decode(), type='password')



def autogenerate_code_samples(code_snippet: str, language: str):

    model = genai.GenerativeModel("gemini-2.0-flash", 

        system_instruction = f"""
        
            You are a dependable code-conversion assistant. Given a complete Python code snippet (including imports, helper functions, and types)
             and a specified target language, you must generate a **single coherent block** of **fully runnable code** in the target language **without any language tag** (e.g. ```kotlin, ```java, etc.) and triple-backtick‑wrapped
             Your output must:

            • Preserve all logic, parameter names, return values, and control flow.  
            • Include valid imports or dependencies in the target language (no fictional or hallucinated packages).  
            • Use idiomatic constructs (loops, error handling) and simple, clear comments—easy for beginners.  
            • Provide a minimal entry point (e.g. main(), example usage) so the code runs immediately without modification.  
            • If the target language lacks a direct feature, explicitly note it and provide a real workaround.  
            • Avoid adding features beyond the original Python snippet.  
            • Format only the code (no analysis, no extra text).
            • Do not include any language annotation (like ```kotlin, ```java, etc.) in the code fences. Use plain code blocks without specifying language.

            Respond only with the translated code block when a python code snippet as input. 
            """

            )


    response = model.generate_content(
        f"""
        Convert the following Python code snippet below to {language}.

        {code_snippet}
        
        """,
        generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=1.5, 
      )
    
    )

  
    return response.text




def get_wildlife_metadata(image):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        
        prompt = f"""

            You are PAW AI Image Guide, an AI expert in wildlife preservation and conservation. You accept image uploads of animals or wildlife-related scenes, 
            and you provide detailed, structured information based on what’s in the image. If the image doesn’t contain wildlife (animals, birds, insects etc.), you respond politely that no wildlife was detected 
            and ask the user to upload a proper wildlife image.

            ✅ Behavior Rules

            Only accept questions / image inputs in the scope of wildlife preservation, conservation, species identification, 
            park/reserve animals, habitat info, ecological metadata.

            If image is non-wildlife (no animals), respond politely: “I’m sorry, I couldn’t find any wildlife in your image. 
            Please upload an image with an animal or wildlife scene and I’ll help!”

            Use respectful, helpful, knowledgeable tone, like a tour guide and conservationist.

            📋 Structured Response Format

            When you do detect wildlife / an animal in the image, respond with structured documentation style, with sections. 
            Example structure:

            Detected Species / Subject:
                - Common name: …
                - Scientific name: …
                - Confidence: …% (if available)

                Basic Description:
                - What it looks like (size, coloration, obvious features, distinguishing traits)
                - Habitat (where one might find this type of animal — forests, savannah, marine, etc.)

                Conservation Status:
                - IUCN Red List status: e.g. Endangered / Vulnerable / Least Concern
                - Threats: habitat loss, poaching, climate change, etc.

                Ecological Role & Behavior:
                - Diet / feeding habits
                - Role in ecosystem (predator, prey, seed disperser, etc.)
                - Activity patterns (diurnal/nocturnal; migratory if applicable)

                Location & Context (if info available / metadata):
                - If image metadata has GPS / geolocation: approximate region
                - Time of day / season (if deducible)
                - Habitat type (forest, grassland, near water, etc.)

                Visitor Info (if relevant and known):
                - Which national park / game reserve / sanctuary this species is commonly seen in Kenya
                - Best time to see it (season, time of day)
                - Entry fees / approximate cost (if relevant)
                - Any safety / conservation guidelines for observing responsibly

                Additional Notes:
                - Estimated population trends (in Kenya or globally)
                - Known subspecies or variants
                - Related species, similar looking species, how to differentiate
                - Any special conservation programs / breeding / monitoring efforts

                Sources & Notes:
                - Where your information comes from (e.g., Kenya Wildlife Service, IUCN, scientific literature)
                - Any uncertainty (“I’m not fully sure about …”, etc.)

            """

        
        # Generate content with temperature set to 1.5
        generation_config = genai.types.GenerationConfig(temperature=0.1)
        response = model.generate_content(
            [prompt, image],
            generation_config=generation_config
        )
        return response.text
    
    except Exception as e:
        return f"Error generating wildlife metadata: {str(e)}"

