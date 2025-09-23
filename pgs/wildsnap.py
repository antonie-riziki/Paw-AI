import streamlit as st 
import sys


from PIL import Image

sys.path.insert(1, './modules')


from func import get_wildlife_metadata  


uploaded_file = st.file_uploader("Upload Wildlife Photo/Video", type=["jpg", "jpeg", "png", "mp4", "mov"])  



if uploaded_file is not None:
    wildlife_image = Image.open(uploaded_file)  
    
    col1, col2 = st.columns(2)  

    with col1:
        st.image(uploaded_file, caption='Uploaded Media', use_container_width=True)
    
    with col2:
        wildlife_metadata = get_wildlife_metadata(wildlife_image)

        st.markdown("""
                <style>
                .scroll-box {
                    max-height: 450px;
                    overflow-y: scroll;
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    
                }
                </style>
            """, unsafe_allow_html=True)
        
        st.markdown(f'<div class="scroll-box">{wildlife_metadata}</div>', unsafe_allow_html=True)
    
