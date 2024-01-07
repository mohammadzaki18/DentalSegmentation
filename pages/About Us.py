import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
import io

st.title('About Us✨')
st.write(""" Hello! We are the Uhuyy team from Yarsi University..""")

st.write (""" As fifth-semester students majoring in Computer Science, we are currently focusing on the trending field of Artificial Intelligence (AI). Our decision to delve into AI is driven by the belief that this technology will bring significant changes, and we are strongly committed to contributing to it's advancements.
""")

st.write("""
Within our team, we have members who enjoy coding, are adept at managing models, and, of course, can make AI look cool. If asked, "Can anyone code while sipping coffee?" the answer is undoubtedly, "Absolutely!" even though it sometimes comes with its challenges, hehe.
""")

st.write("""
Thank you for being part of our journey, and stay tuned for the continuation of our story in upcoming projects! 🌟🤖
""")


def enhance_image(image_data):
    image = Image.open(io.BytesIO(image_data))

    enhanced_image = image.filter(ImageFilter.SHARPEN)

    border_size = 2
    border_color = "black"
    img_with_border = Image.new(
        "RGB",
        (enhanced_image.width + border_size * 2, enhanced_image.height + border_size * 2),
        border_color,
    )
    img_with_border.paste(enhanced_image, (border_size, border_size))

    with io.BytesIO() as output:
        img_with_border.save(output, format="JPEG")
        return output.getvalue()


col1, col2, col3 = st.columns(3)

with col1:
    st.image(enhance_image(open("img_sources/3.png", "rb").read()), caption="Kafah Al Farizi", width=200)

with col2:
    st.image(enhance_image(open("img_sources/2.png", "rb").read()), caption="Mohammad Zaki", width=200)

with col3:
    st.image(enhance_image(open("img_sources/1.png", "rb").read()), caption="Enggar Galih W", width=200)

st.divider() 

st.header("""References""")
st.write("""
- https://github.com/mfcsds/ic-corn
- https://github.com/facebookresearch/detectron2
- https://pubmed.ncbi.nlm.nih.gov/36368120/
- https://ieeexplore.ieee.org/document/10113315
- https://pubmed.ncbi.nlm.nih.gov/34347537/
""")

st.divider()
st.write("""
Copyright © 2023 - Uhuyy, All Rights Reserved.
""")
