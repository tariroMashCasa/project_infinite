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
level_0_dropdown = st.selectbox("What would you like to see", ["","World","Character","Scene","Influence"])

if level_0_dropdown == "World":
    level_1_dropdown = st.selectbox("What would you like to see", ["","Initial","Latest","Full"])
    if level_1_dropdown == "Initial":
        payload = {"text": "initial"}
        r = requests.post(st.secrets["general"]["API_URL"], json=payload, timeout=120)
        if r.ok:
            world_state_text = r.json().get("world_state")  
            st.markdown(world_state_text)        # transcript
        else:
            st.error(f"{r.status_code} {r.text}")  # show server’s complaint
            st.stop()

    elif level_1_dropdown == "Latest":
        payload = {"text": "latest"}
        r = requests.post(st.secrets["general"]["API_URL"], json=payload, timeout=120)
        if r.ok:
            world_state_text = r.json().get("world_state")  
            st.markdown(world_state_text)        # transcript
        else:
            st.error(f"{r.status_code} {r.text}")  # show server’s complaint
            st.stop()
    elif level_1_dropdown == "Full":
        payload = {"text": "full"}
        r = requests.post(st.secrets["general"]["API_URL"], json=payload, timeout=120)
        if r.ok:
            world_state_text = r.json().get("world_state")  
            st.markdown(world_state_text)        # transcript
        else:
            st.error(f"{r.status_code} {r.text}")  # show server’s complaint
            st.stop()

if level_0_dropdown == "Character":
    level_1_dropdown = st.selectbox("What would you like to see", ["","Character Brief","Memories","Motivations"])
    if level_1_dropdown == "Character Brief":
        
        # get the list of characters by calling the get_all_characters_names endpoin

        # get the list of characters by calling the get_all_characters_in_reverse_order endpoint
        payload = {"text": "all"}
        r = requests.post(st.secrets["general"]["get_all_characters_endpoint"], json=payload, timeout=120)
        if r.ok:
            characters_list = r.json().get("character_names").split("|")   
        else:
            st.error(f"{r.status_code} {r.text}")  # show server’s complaint
            st.stop()

        level_2_dropdown = st.selectbox("Select Character", [""] + characters_list)
        if level_2_dropdown != "":
            payload = {"text": level_2_dropdown}
            r = requests.post(st.secrets["general"]["character_brief_endpoint"], json=payload, timeout=120)
            if r.ok:
                character_brief_text = r.json().get("character_brief")   
                st.markdown(character_brief_text)           
            else:
                st.error(f"{r.status_code} {r.text}")  # show server’s complaint
                st.stop()
    if level_1_dropdown == "Memories":
        # get the list of characters by calling the get_all_characters_names endpoin

        # get the list of characters by calling the get_all_characters_in_reverse_order endpoint
        payload = {"text": "all"}
        r = requests.post(st.secrets["general"]["get_all_characters_endpoint"], json=payload, timeout=120)
        if r.ok:
            characters_list = r.json().get("character_names").split("|")   
        else:
            st.error(f"{r.status_code} {r.text}")  # show server’s complaint
            st.stop()

        level_2_dropdown = st.selectbox("Select Character", [""] + characters_list)
        if level_2_dropdown != "":

            payload = {"text": level_2_dropdown}  
            r = requests.post(st.secrets["general"]["character_memories_endpoint"], json=payload, timeout=120)
            if r.ok:
                memories_text = r.json().get("character_memories").split("|")    
                for i in  memories_text:
                    # st.markdown(i)  
                    # alternative
                    st.markdown(
                       f"""
                        <div style="background-color:#f0f8ff; padding:10px; border-radius:6px">
                            <em>{i}</em>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.error(f"{r.status_code} {r.text}")  # show server’s complaint
                st.stop()

    if level_1_dropdown == "Motivations":
        # get the list of characters by calling the get_all_characters_names endpoin

        # get the list of characters by calling the get_all_characters_in_reverse_order endpoint
        payload = {"text": "all"}
        r = requests.post(st.secrets["general"]["get_all_characters_endpoint"], json=payload, timeout=120)
        if r.ok:
            characters_list = r.json().get("character_names").split("|")   
        else:
            st.error(f"{r.status_code} {r.text}")  # show server’s complaint
            st.stop()

        level_2_dropdown = st.selectbox("Select Character", [""] + characters_list)
        if level_2_dropdown != "":
        

            payload = {"text": level_2_dropdown}
            r = requests.post(st.secrets["general"]["character_motivations_endpoint"], json=payload, timeout=120)
            if r.ok:
                motivations_text = r.json().get("character_motivations").split("|") 
                for i in  motivations_text:
                    # st.markdown(i)        # transcript
                    # alternative
                    st.markdown(
                       f"""
                        <div style="background-color:#f0f8ff; padding:10px; border-radius:6px">
                            <em>{i}</em>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.error(f"{r.status_code} {r.text}")  # show server’s complaint
                st.stop()

if level_0_dropdown == "Scene":
    # get the list of scenes by calling the get_all_scenes_in_reverse_order endpoint
    payload = {"text": "all"}
    r = requests.post(st.secrets["general"]["get_all_scenes_in_reverse_order_endpoint"], json=payload, timeout=120)
    if r.ok:
        scenes_list = r.json().get("scene_names").split("|")    
    else:
        st.error(f"{r.status_code} {r.text}")  # show server’s complaint
        st.stop()

    level_1_dropdown = st.selectbox("What would you like to see",[""] + scenes_list)
    if level_1_dropdown != "":
        payload = {"text": level_1_dropdown}

        # get the scene summary first
        r = requests.post(st.secrets["general"]["get_scene_summary_endpoint"], json=payload, timeout=120)
        if r.ok:
            st.header("Scene Summary")
            scene_summary_text = r.json().get("scene_summary")  
            # st.markdown(f"**{scene_summary_text}**")        
            # alternative
            st.markdown(
                       f"""
                        <div style="background-color:#f0f8ff; padding:10px; border-radius:6px">
                            <em>{scene_summary_text}</em>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        else:
            st.error(f"{r.status_code} {r.text}")  # show server’s complaint
            st.stop()
        # insrt a seperator
        st.markdown("---")

        # get the scene narrative
        st.header("Scene Narrative")
        r = requests.post(st.secrets["general"]["get_raw_narrative_from_scene_endpoint"], json=payload, timeout=120)
        if r.ok:
            scene_narrative_text = r.json().get("scene_narrative")  
            st.markdown(scene_narrative_text)        # transcript
        else:
            st.error(f"{r.status_code} {r.text}")  # show server’s complaint
            st.stop()



if level_0_dropdown == "Influence":
    # get the list of characters by calling the get_all_characters_names endpoin

    # get the list of characters by calling the get_all_characters_in_reverse_order endpoint
    payload = {"text": "all"}
    r = requests.post(st.secrets["general"]["get_world_influence_of_all_characters_endpoint"], json=payload, timeout=120)
    if r.ok:
        characters_list = r.json().get("character_influence_summary")
        influence_df = pd.read_json(characters_list)
        st.dataframe(influence_df)  
        # st.markdown(characters_list)   
    else:
        st.error(f"{r.status_code} {r.text}")  # show server’s complaint
        st.stop()




