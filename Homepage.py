import streamlit as st
from st_pages import Page, show_pages, add_page_title
from PIL import Image

st.divider()   
st.image('img_sources\Thumbnail Web.gif')

st.divider()

st.title('MRI Segmentation Modelling')

st.write("""
    Welcome to our website!, this website displays the modeling results of MRI Segmentation. This website used 
Machine Learning technology to identify the Condyle obtained from MRI segmentation, Harnessing the power of state-of-the-art Machine Learning technology, 
we meticulously unveil the identification of the Condyle derived from MRI segmentation. 
Join us on a captivating journey through the convergence of cutting-edge technology and medical insights. 
Explore the depths of our findings and witness the synergy between innovation and healthcare.
""")

st.header('What is Segmentation?')
st.write("""
 Segmentation is a process that aims to separate different anatomical structures in MRI images, 
in this study we separate the structure called "Condyle" which is found in the human jaw. 

Here is an example of the segmentation that we got:

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
          Page("pages\How To Use.py", "📃How To Use?"),
           Page("pages\About Us.py", "👉About Us"),
            Page("pages\App.py", "📲Application"),
    ]
)