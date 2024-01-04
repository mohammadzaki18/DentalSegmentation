import streamlit as st
from st_pages import Page, show_pages, add_page_title
from PIL import Image

st.divider()   

# Displaying a thumbnail at the top
st.image('img_sources\Thumbnail Web.gif')

# Judul aplikasi
st.title('MRI Segmentation Modelling')

# Penjelasan aplikasi
st.write("""
    Selamat datang di website kami, website ini menampilkan hasil Modelling dari MRI Segmentation. Website ini menggunakan teknologi 
Machine Learning untuk mengidentifikasi Condyle yang didapatkan dari segmentation MRI. 
Dengan menggunakan algoritma klasifikasi canggih, website ini dapat membantu bagi para pembaca, 
peneliti, dan sekaligus dokter dalam melihat hasil segmentasi Condyle yang sudah kami dapatkan.
""")

show_pages(
    [
        Page("Homepage.py", "🖥️Homepage"),
         Page("pages\Segmentation Def.py", "📖Segmentation Def"),
          Page("pages\How To Use.py", "📃How To Use"),
           Page("pages\About Us.py", "👉About Us"),
            Page("pages\App.py", "📲Application"),
    ]
)