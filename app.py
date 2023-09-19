# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 00:12:27 2023

@author: Gabriel Yashim
"""

import numpy as np 
import pickle
import streamlit as st


model = pickle.load(open('RandomForest.pkl', 'rb'))


st.title('Student Depression Prediction System')
html_temp = """
    <h3 style="color:white;text-align:center;">By Gabriel Yashim</h3>
    <div style="background-color:tomato;padding:10px;margin-bottom:3rem">
        <p style="text-align:justify;">
            While mental health issue in the school may always be present to some extent, it is preventable in most cases from
            occurring at all or the least reduced in their impact through Promotion, Prevention, and Early Intervention (PPEI).
            This system was developed to alleviate the challenge student experienced around mental health and how to check-in and
            support each other during times of strain. <br>
            The dataset used to build the model was locally curated using questionniers and survey with the students of the Federal University Lokoja as participants. <br>
            To interact with the pretrained model, all you need to do is fill the form below:
        </p>  
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

# create columns for our UI
col1, col2, col3 = st.columns(3)


# Dictionary to mappings for column1 starts here
# Dictionary to map age ranges to integer values
age_range_mapping = {
    "16-20": 0,
    "21-25": 1,
    "26-30": 2,
    "31-35": 3,
    "35-40": 4
}

# Dictionary to map level to integer values
level_mapping = {
    "100 level":100,
    "200 level":200,
    "300 level":300,
    "400 level":400
}

# Dictionary to map self assessment tool to integer values
self_ass_mapping = {
    "No": 1,
    "Yes": 2,
    "Maybe": 0
}

# Dictionary to map interests to integer values
interest_mapping = {
    "Not at all":0,
    "Several days":1,
    "More than half the days":2,
    "Nearly everyday":3
}

# Dictionary to map sleeping to integer values
sleep_mapping = {
    "Not at all":0,
    "Several days":1,
    "More than half the days":2,
    "Nearly everyday":3
}

# Dictionary to mappings for column1 stops here

with col1:
# Dropdown select box for column1
    selected_age_range = st.selectbox("Select Your Age Range:", list(age_range_mapping.keys()))
    selected_level = st.selectbox("Select Your Level:", list(level_mapping.keys()))
    selected_self_ass = st.selectbox("Have you ever used a self asessment tool on depression in the past?", list(self_ass_mapping.keys()))
    selected_interest = st.selectbox("Do you have little interest or pleasure in doing things?", list(interest_mapping.keys()))
    selected_sleep = st.selectbox("Do you have Trouble falling asleep, staying asleep, or sleeping too much?", list(sleep_mapping.keys()))
    
# storing the selected values in different variables    
age_value = age_range_mapping[selected_age_range]
level_value = level_mapping[selected_level]
self_ass_value = self_ass_mapping[selected_self_ass]
interest_value = interest_mapping[selected_interest]
sleep_value = sleep_mapping[selected_sleep]



# Dictionary to mappings for column2 starts here

# Dictionary to map tiredness to integer values
tiredness_mapping = {
    "Not at all":0,
    "Several days":1,
    "More than half the days":2,
    "Nearly everyday":3
}

# Dictionary to map sleeping to integer values
appetite_mapping = {
    "Not at all":0,
    "Several days":1,
    "More than half the days":2,
    "Nearly everyday":3
}

# Dictionary to map feeling to integer values
feeling_mapping = {
    "Not at all":0,
    "Several days":1,
    "More than half the days":2,
    "Nearly everyday":3
}

# Dictionary to map concentrating to integer values
concentrating_mapping = {
    "Not at all":0,
    "Several days":1,
    "More than half the days":2,
    "Nearly everyday":3
}


# Dictionary to mappings for column2 stops here

with col2:
# Dropdown select box for age range
    selected_tiredness = st.selectbox("Do you Feel Tired or Feel like you have little energy?", list(tiredness_mapping.keys()))
    selected_appetite = st.selectbox("Do you have Poor appetite or over eating?", list(appetite_mapping.keys()))
    selected_feeling = st.selectbox("Are you Feeling bad about yourself?", list(feeling_mapping.keys()))
    selected_concentrating = st.selectbox("Do you have Trouble concentrating on things such as reading the your books or paying attention in class?", list(concentrating_mapping.keys()))
    
    
# storing the selected values in different variables    
tiredness_value = tiredness_mapping[selected_tiredness]
appetite_value = appetite_mapping[selected_appetite]
feeling_value = feeling_mapping[selected_feeling]
concentrating_value = concentrating_mapping[selected_concentrating]




# Dictionary to mappings for column3 starts here

# Dictionary to map restless to integer values
restless_mapping = {
    "Not at all":0,
    "Several days":1,
    "More than half the days":2,
    "Nearly everyday":3
}

# Dictionary to map thoughts to integer values
thoughts_mapping = {
    "Not at all":0,
    "Several days":1,
    "More than half the days":2,
    "Nearly everyday":3
}

# Dictionary to map anxiety to integer values
anxiety_mapping = {
    "No": 1,
    "Yes": 2,
    "Maybe": 0
}

# Dictionary to map diagnosed to integer values
diagnosed_mapping = {
    "No": 1,
    "Yes": 2,
    "Maybe": 0
}

# Dictionary to mappings for column3 stops here

with col3:
# Dropdown select box for age range
    selected_restless = st.selectbox("Do you act fidgety or restless?", list(restless_mapping.keys()))
    selected_thoughts = st.selectbox("Do you have thoughts that you would be better off dead or of hurting yourself in some way?", list(thoughts_mapping.keys()))
    selected_anxiety = st.selectbox("Have you ever had an anxiety attack?", list(anxiety_mapping.keys()))
    selected_diagnosed = st.selectbox("Have you been diagnosed with any form of depression in the past?", list(diagnosed_mapping.keys()))
    

# storing the selected values in different variables 
restless_value = restless_mapping[selected_restless]   
thoughts_value = thoughts_mapping[selected_thoughts]
anxiety_value = anxiety_mapping[selected_anxiety]
diagnosed_value = diagnosed_mapping[selected_diagnosed]

score = interest_value + sleep_value + tiredness_value + appetite_value + feeling_value + concentrating_value + restless_value + thoughts_value


depression_pred = ''

html_temp2 = """
        <h3 style="margin-top:3rem;">Score Metric</h3>
            <ul>
                <li>0 - 4 = Normal</li>
                <li>5 - 9 = Mild</li>
                <li>10 - 14 = Moderate</li>
                <li>15 - 19 = Moderately Severe</li>
                <li>20 - 27 = Severe</li>
            </ul>
            """
st.markdown(html_temp2,unsafe_allow_html=True)


if st.button('Submit'):
    st.write(f"Your score is: {score}")
    depression_pred = model.predict([[age_value, level_value, self_ass_value, interest_value, sleep_value, tiredness_value, appetite_value, feeling_value, concentrating_value, restless_value, thoughts_value, anxiety_value, diagnosed_value, score]])
    
    st.write(f"Your depression level is: {depression_pred[0]}")
    




