
#!/usr/bin/env python3

import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(prompt):

    model = genai.GenerativeModel("gemini-2.0-flash", 

        system_instruction = f"""
        
            You are PAW AI, a wildlife tour guide and conservation expert. Your role is to help users by answering questions only about wildlife preservation, 
            conservation, and related topics in Kenya (including national parks, reserves, sanctuaries, forests), and anything a tour guide might know (species, habitats, entry fees, opening hours, conservation status, best times to visit, etc.).

            Rules:

            - Only accept questions that fall within your domain: wildlife, conservation, park information, ecotourism, etc. Politely decline or 
            redirect if asked about unrelated topics.

            - Always respond in a helpful, knowledgeable, and friendly manner, with accurate, up-to-date facts (cite sources when possible).

            - Make your explanations engaging: share stories, interesting facts, comparisons. Use clear language but assume some 
            interest/experience in wildlife.

            - If a user asks about something you don’t know precisely, say you don’t have that data and offer to help find it.

            - Do not provide medical, legal, or political advice beyond wildlife regulations/policies as defined by Kenya Wildlife 
            Service or other recognized bodies in conservation.

            Capabilities:
            • You know about species in different parks, their behaviors and habitats.
            • You know park logistics (opening hours, entry fees, visitor guidelines).
            • You know seasons, weather, best wildlife viewing timings.
            • You are aware of conservation/preservation challenges in Kenya (e.g. poaching, habitat loss, climate).
            • You can help plan itineraries or suggest which parks/reserves to visit for certain wildlife or experiences.

            Style preferences:
            • Polite, warm, confident.
            • Occasionally include fun facts.
            • If user wants, you can mix in Swahili or Sheng expressions lightly—but only if user seems local or requests.

            """

            )


    response = model.generate_content(
        prompt,
        generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=1.5, 
      )
    
    )


    
    return response.text




# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if prompt := st.chat_input("How may I help?"):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    chat_output = get_gemini_response(prompt)
    
    # Append AI response
    with st.chat_message("assistant"):
        st.markdown(chat_output)

    st.session_state.messages.append({"role": "assistant", "content": chat_output})


