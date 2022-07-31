import streamlit as st 
from PIL import Image
import numpy as np
import easyocr as ocr # optical character recognition

# https://www.jaided.ai/easyocr/

loaded_image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])

if loaded_image is not None:

    # Getting the model
    def ocr_model():
        model = ocr.Reader(['en'],model_storage_directory='.', detector = True, recognizer = True)
        return model

    # Preparing imgae to model's format
    def prepared_image(image = loaded_image):
        img = Image.open(image)
        #st.image(img)
        img_arr = np.array(img)
        return img_arr

    # applying model onto prepared image, returns appended lines of text
    def apply_model(model = ocr_model(), prepared_image = prepared_image()):
        text_output = []
        model_output = model.readtext(prepared_image)
        for text in model_output:
            st.write(text)
            text_output.append(text[1]) # 1 = predictions https://www.jaided.ai/easyocr/
        return text_output

    #input_image = Image.open(image)
    st.image(loaded_image)
    with st.spinner("computing"):
        st.write(apply_model())

# TO DO LIST:
# 1. Play with availible parameters
# 2. Export text button
# 3. Pack it up into class?\
# 4. Example to play with
# 5. Parametrization (adding languages, img url source)
# 6. Variation of export (txt, html, pdf)