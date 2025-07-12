import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile
import io
import pandas as pd
import time
import os
import json
import requests
from datetime import datetime
from io import StringIO
from PIL import Image

current_date = datetime.now()
formatted_date = current_date.strftime("%d_%m_%Y_%H_%M_%S")



im = Image.open('slug_logo.png')
st.set_page_config(
    page_title="PSIL",
    page_icon=im,
    initial_sidebar_state="collapsed",
    layout="wide"

    ) 

st.title("Project Infinite")

# this is going to be the first dropoown to select what information you want to get from the world
level_0_dropdown = st.selectbox("What would you like to see", ["","World","Character","Scene"])

if level_0_dropdown == "World":
    level_1_dropdown = st.selectbox("What would you like to see", ["","Initial","Latest","Full"])
    if level_1_dropdown == "Initial":
        payload = {"text": "initial"}
        r = requests.post(st.secrets["general"]["API_URL"], json=payload, timeout=120)
        if r.ok:
            world_state_text = r.json().get("text")  
            st.markdown(world_state_text)        # transcript
        else:
            st.error(f"{r.status_code} {r.text}")  # show server’s complaint
            st.stop()

    elif level_1_dropdown == "Latest":
        payload = {"text": "latest"}
        r = requests.post(st.secrets["general"]["API_URL"], json=payload, timeout=120)
        if r.ok:
            world_state_text = r.json().get("text")  
            st.markdown(world_state_text)        # transcript
        else:
            st.error(f"{r.status_code} {r.text}")  # show server’s complaint
            st.stop()
    elif level_1_dropdown == "Full":
        payload = {"text": "full"}
        r = requests.post(st.secrets["general"]["API_URL"], json=payload, timeout=120)
        if r.ok:
            world_state_text = r.json().get("text")  
            st.markdown(world_state_text)        # transcript
        else:
            st.error(f"{r.status_code} {r.text}")  # show server’s complaint
            st.stop()


 








