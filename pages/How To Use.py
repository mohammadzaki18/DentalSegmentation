import streamlit as st

st.title('How To Use')
st.write("""
- Prepare the raw MRI images
- Upload the image (must not exceed 200MB)
- Click on the Segmentation Button
- MRI segmentation results will appear
""")

st.divider()
st.header ("""Here is the tutorial for using the Application""")
st.video('img_sources\How To Use.mp4')