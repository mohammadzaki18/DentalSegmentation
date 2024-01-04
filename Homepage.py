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
    Welcome to our website, this website displays the modeling results of MRI Segmentation. This website uses 
Machine Learning technology to identify the Condyle obtained from MRI segmentation. 
""")

st.header('What is Segmentation?')
st.write("""
 Segmentation is a process that aims to separate different anatomical structures in MRI images, 
in this study we separate the structure called "Condyle" which is found in the human jaw. 

Here is an example of the segmentation we got:

""")

col1, col2 = st.columns(2)

with col1:
    st.image('img_sources\Condyle.png', caption="Before Segmentation", use_column_width=True)

with col2:
    st.image('img_sources\Condyle Area.png', caption="After Segmentation", use_column_width=True)



show_pages(
    [
        Page("Homepage.py", "🖥️Homepage"),
         Page("pages\Segmentation Def.py", "📖Design Experiment"),
          Page("pages\How To Use.py", "📃How To Use"),
           Page("pages\About Us.py", "👉About Us"),
            Page("pages\App.py", "📲Application"),
    ]
)