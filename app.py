import streamlit as st
from PIL import Image
import numpy as np
from effects.color_pattern import create_colorful_big_one
from effects.simple_grid import create_simple_grid
from effects.complex_pattern import create_complex_pattern
from utils.image_processing import preprocess_image

st.title("Image Effects App")

uploaded_file = st.file_uploader(
    "Drag and drop an image here",
    type=["png", "jpg", "jpeg", "gif"],
    key="image_uploader",
)

if uploaded_file:
    # Load and preprocess image
    pil_image = Image.open(uploaded_file)
    pil_image = preprocess_image(pil_image)

    # Convert to numpy array once
    image_array = np.array(pil_image.convert("RGB"))

    st.image(image_array, caption="Original Image", use_column_width=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Color Pattern"):
            result = create_colorful_big_one(image_array)
            st.image(result, caption="Color Pattern Effect", use_column_width=True)

    with col2:
        if st.button("Simple Grid"):
            result = create_simple_grid(image_array)
            st.image(result, caption="Simple Grid Effect", use_column_width=True)

    with col3:
        if st.button("Complex Pattern"):
            result = create_complex_pattern(image_array)
            st.image(result, caption="Complex Pattern Effect", use_column_width=True)
