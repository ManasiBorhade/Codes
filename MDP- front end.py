# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:59:57 2022

@author: Manasi
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np


diabetes_model = pickle.load(open('C:/Users/Manasi/Desktop/AIT/Placements/diabetes.sav', 'rb'))

heart_model = pickle.load(open('C:/Users/Manasi/Desktop/AIT/Placements/heart.sav','rb'))  

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
# Diabetes Prediction P
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info('Enter the number of pregnancies')
        Pregnancies = st.number_input('Number of Pregnancies')
        
        
    with col2:
        st.info('Enter the plasma glucose concentration')
        Glucose = st.number_input('Glucose Level')
        
    with col3:
        st.info('Enter diastolic blood pressure in mm/Hg')
        BloodPressure = st.number_input('Blood Pressure value')
    
    with col1:
        st.info('Enter Skin Thickness value')
        SkinThickness = st.number_input('Skin Thickness value')
    
    with col2:
        st.info('Enter Insulin Level in U/mL')
        Insulin = st.number_input('Insulin Level')
    
    with col3:
        st.info('Enter BMI value')
        BMI = st.number_input('BMI value')
        
    
    with col1:
        st.info('Please enter Diabetes Pedigree Function value ')
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
    
    with col2:
        st.info('Please enter persons age')
        Age = st.number_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    if st.button('What is Glucose level?'):
     st.write('Glucose level means the level of glucose (sugar) in a person’s blood.Normal blood sugar levels are Between 4.0 to 5.4 mmol/L (72 to 99 mg/dL) when fasting Up to 7.8 mmol/L (140 mg/dL) 2 hours after eating')
    if st.button('What is Blood pressure value?'):
     st.write('Blood pressure is a measure of the force that your heart uses to pump blood around your body.Ideal blood pressure is ranges between 90/60mmHg and 120/80mmHg.High blood pressure ranges from 140/90mmHg or higher.Low blood pressure ranges from 90/60mmHg or lower ')
    if st.button('What is Skin thickness value?'):
     st.write('Skin thickness is primarily determined by collagen content and is increased in insulin-dependent diabetes mellitus (IDDM) ')
    if st.button('What is Insulin level?'):
     st.write('Insulin is a hormone made in the pancreas, which is an organ in your body that helps with digestion. It helps your body use glucose (sugar) for energy. ')
    if st.button('What is BMI?'):
     st.write('The body mass index (BMI) is a measure that uses your height and weight to work out if your weight is healthy. below 18.5 – underweight range. between 18.5 and 24.9  healthy weight range. between 25 and 29.9  overweight range. between 30 and 39.9  obese range.')
    if st.button('What is Diabetes pedigree function?'):
     st.write('Diabetes pedigree function which scores likelihood of diabetes based on family history ') 
      
    
        
    
    
# Heart Disease Prediction
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info('The person age in years')
        age= st.number_input('Age')
    with col2:
        st.info('Enter 1= Male 0= Female')
        sex = st.number_input('sex')
    with col3:
        st.info('Enter chest pain type')
        #cp = st.text_input('Chest Pain types')
        cp=st.number_input('Chest Pain types')
    with col1:
        st.info('Enter Blood Pressure ')
        #trestbps = st.text_input('Resting Blood Pressure')
        trestbps = st.number_input('Blood Pressure')
        
    with col2:
        st.info('Enter Cholestoral')
        #chol = st.text_input('Serum Cholestoral in mg/dl')
        chol = st.number_input('Cholestoral in mg/dl')        
        
    with col3:
        st.info('Enter Blood sugar level')
        #fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        fbs = st.number_input('Blood Sugar')
        
    with col1:
        st.info('Enter Electrocardiographic (ECG) result')
        #restecg = st.text_input('Resting Electrocardiographic results')
        restecg = st.number_input('Resting Electrocardiographic results')
    with col2:
        st.info('Enter Maximum Heart Rate achieved')
        #thalach = st.text_input('Maximum Heart Rate achieved')
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        st.info('Enter Exercise Induced Angina 1 = yes,0 = no')
        #exang = st.text_input('Exercise Induced Angina')
        exang = st.number_input('Exercise Induced Angina')
    with col1:
        st.info('Enter ST depression induced by exercise')
        #oldpeak = st.text_input('ST depression induced by exercise')
        oldpeak = st.number_input('ST depression induced by exercise')
        
        
    with col2:
        st.info('Enter Slope of the peak exercise ST segment')
        #slope = st.text_input('Slope of the peak exercise ST segment')\
        slope = st.number_input('Slope of the peak exercise ST segment')
        
        
    with col3:
        st.info('Enter Major vessels')
        #ca = st.text_input('Major vessels colored by flourosopy')
        ca = st.number_input('Major vessels ')
        
        
    with col1:
        st.info('Enter Thalassemia result')
        #thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        thal = st.number_input('thal:')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    if st.button('What is Chest Pain Type?'):
     st.write('Angina, which is chest pain caused by blockages in the blood vessels leading to your heart.Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic')
    if st.button('What is Blood Pressure?'):
     st.write('Blood pressure is a measure of the force that your heart uses to pump blood around your body.Ideal blood pressure is ranges between 90/60mmHg and 120/80mmHg.High blood pressure ranges from 140/90mmHg or higher.Low blood pressure ranges from 90/60mmHg or lower ')
    if st.button('What is Cholestrol?'):
     st.write('Cholesterol is a waxy, fat-like substance, and there are two types: low-density lipoprotein (LDL) and high-density lipoprotein (HDL).LDL cholesterol levels should be low. But having more HDL, or “good,” cholesterol in the blood may reduce the risk of a heart attack or stroke. ')
    if st.button('What is Blood Sugar?'):
     st.write('Normal blood sugar levels are Between 4.0 to 5.4 mmol/L (72 to 99 mg/dL) when fasting Up to 7.8 mmol/L (140 mg/dL) 2 hours after eating ')
    if st.button('What is Resting Electrocardiographic result?'):
     st.write('No movement is allowed during the test, as electrical impulses generated by other muscles may interfere with those generated by your heart. This type of ECG usually takes 5 to 10 minutes. The normal range of the ECG differed between men and women: heart rate 49 to 100 bpm vs. 55 to 108 bpm, P wave duration 81 to 130 ms vs. 84 to 130 ms, PR interval 119 to 210 ms vs. ')
    if st.button('What are the Heart Rates?'):
     st.write('A normal resting heart rate for adults(18+) ranges from 60 to 100 beats per minute. Birth to 4 weeks: 100 - 205 beats bpm*. (4 weeks to 1 year): 100 – 180 bpm*. (1 to 3 years): 98 - 140 bpm*.(3 to 5 years): 80 - 120 bpm.(5 to 12 years): 75 - 118 bpm.(13 to 18 years): 60 - 100 bpm.')
    if st.button('What is Excercise Induced Agina?'):
     st.write('It usually happens during activity (exertion) and goes away with rest or angina medication. For example, pain that comes on when you are walking uphill or in the cold weather may be angina ')
    if st.button('What is ST depression induces?'):
     st.write('ST depression induced by exercise relative to rest.The exercise-induced ST segment depression was defined as a horizontal or downsloping at least 1.0 mm ST depression at 80 ms after J point or any ST depression of >1.0 mm at 80 ms after J point in ECG. ')
    if st.button('What is Slope of the peak exercise ST segment?'):
     st.write('The ST segment shift relative to exercise-induced increments in heart rate, the ST/heart rate slope (ST/HR slope), has been proposed as a more accurate ECG. Value 1: upsloping, Value 2: flat, Value 3: downsloping ')
    if st.button('What is Major vessels ?'):
     st.write('Number of major vessels colored by fluoroscopy	0–3 value ')
    if st.button('What is thal?'):
     st.write('Thalassemia is an inherited blood disorder that causes your body to have less hemoglobin than normal. Hemoglobin enables red blood cells to carry oxygen. 0 = normal; 1 = fixed defect; 2 = reversable defect')