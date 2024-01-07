import streamlit as st
from st_pages import Page, show_pages, add_page_title
from PIL import Image

st.title('Dental Segmentation')

st.header("Methodology")

st.write("""
 We use a private dataset from IIUM Malaysia as many as 360 MRI scans and have been annotated condyle areas by experts
    using coco.json and vgg.json label formats, from 360 MRIs only 359 can be trained into the model. 
         This dataset only has 1 class which is condyle area.

We used the R-CNN mask with ResNet-101 C4 backbone as the proposed model. 
         Previously, we equalized all "categories" in coco.json labels to "Condyle" 
         because after we explored the data there was inconsistence in the naming of classes/categories, 
         after that we checked whether all images were segmented correctly using coco.json, 
         then we divided the dataset using random state into 271 train data, 68 validation data, and 10 test data. 
         After that we set hyperparameters such as, NUM_WORKERS, BASE_LR, MAX_ITER, etc. After we have set the hyperparameters, 
         we train using our proposed model.

Here for our design experiment: 
""")

st.image('img_sources\Flowchart.jpeg')

st.header("Evaluation")

st.write("""
 After training we evaluate the model. For model evaluation we use the following Average Precision (AP) and use data test for evaluation. 
         Evaluation metrics for the results of several models we have trained and comparison of our proposed model with other backbones

Here for the result: 
""")

st.image('img_sources\Result.jpg')