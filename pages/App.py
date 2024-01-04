import streamlit as st
import torch
import numpy as np
from PIL import Image
from torchvision.transforms import functional as F
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.modeling import build_model
from detectron2.checkpoint import DetectionCheckpointer
from detectron2.model_zoo import model_zoo
import cv2

# Initialize the model and predictor
torch_device = torch.device("cpu")
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_101_C4_3x.yaml"))
cfg.DATALOADER.NUM_WORKERS = 4
cfg.MODEL.WEIGHTS = "model_final.pth" 
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1
cfg.MODEL.DEVICE = torch_device.type

model = build_model(cfg)
model.to(torch_device)
DetectionCheckpointer(model).load(cfg.MODEL.WEIGHTS)
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.9
predictor = DefaultPredictor(cfg)

st.title("Instance Segmentation with Mask R-CNN")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:

    image_pil = Image.open(uploaded_file)
    image_np = np.array(image_pil)

    st.image(image_pil, caption="Original Image", use_column_width=True)

    if st.button("Segmentasi"):
        try:
            with st.spinner("Currently doing segmentation..."):
                outputs = predictor(image_np)
                instances = outputs["instances"].to("cpu")
                segmentation_mask = np.zeros_like(image_np)
                for i in range(len(instances.pred_masks)):
                    mask = instances.pred_masks[i].numpy()
                    color = (0, 255, 0)  # Green color
                    segmentation_mask[mask] = color

                result_image = cv2.addWeighted(image_np, 0.7, segmentation_mask, 0.5, 0)

                # Display the result
                st.image(result_image, caption="Segmentation Result", use_column_width=True)
        except Exception as e:
            st.exception(e)
