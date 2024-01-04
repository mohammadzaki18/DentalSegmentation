import streamlit as st
from st_pages import Page, show_pages, add_page_title
from PIL import Image

st.title('MRI Segmentation')
st.header('Apa itu Segmentation?')
st.write("""
 Segmentation sendiri merupakan proses dimana bertujuan untuk memisahkan struktur anatomi yang berbeda dalam gambar MRI, 
dalam penelitian ini kami memisahkan struktur tersebut yang dinamakan "Condyle" yang terdapat pada rahang manusia. 

Berikut adalah contoh segmentasi yang kami dapatkan:
""")

col1, col2 = st.columns(2)

with col1:
    st.image('img_sources\Condyle.png', caption="Sebelum Disegmentasi", use_column_width=True)

with col2:
    st.image('img_sources\Condyle Area.png', caption="Setelah Disegmentasikan", use_column_width=True)


st.header('Methodology')

st.write("""
 Segmentation sendiri merupakan proses dimana bertujuan untuk memisahkan struktur anatomi yang berbeda dalam gambar MRI, 
dalam penelitian ini kami memisahkan struktur tersebut yang dinamakan "Condyle" yang terdapat pada rahang manusia. 
Segmentasi Condyle sendiri sangat membantu para ahli medis untuk mengidentifikasi dan menganalisis struktur anatomi 
yang berkaitan dengan penyakit atau kondisi pasien. Hal ini membantu para ahli medis dalam mengidentifikasi masalah kesehatan, merumuskan pengobatan, 
         dan memantau pengembangan penyakit pasien.

Berikut adalah contoh segmentasi yang kami dapatkan:
""")
