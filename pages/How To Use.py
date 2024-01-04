import streamlit as st
from st_pages import Page, show_pages, add_page_title
from PIL import Image

st.title('Cara Penggunaan')
st.write("""
- Siapkan gambar raw MRI
- Upload Gambar tersebut (tidak boleh melebihi 200 mb)
- Klik pada tombol segmentasi
- Hasil segmentasi MRI akan muncul
""")