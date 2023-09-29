# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 10:04:44 2023

@author: grover.laporte
"""
import pandas as pd
#import numpy as np
#import plotly.express as px
import streamlit as st
import subprocess


st.write(""" # GGIR Interface for Researchers
         #### The steps to using this interface are:
             1. Import your initial ggir inputs (.csv file)
             2. Find the location of your data file.
             3. Find the location of your output file.
             4. Explore and change any of the ggir inputs using the interface.
             5. Click "Go" and wait. 
         """)

ggir_inputs = st.file_uploader("Choose the ggir input file.")
if ggir_inputs is not None:
    df = pd.read_csv(ggir_inputs)

    df

process1 = subprocess.Popen(["Rscript", #"--vanilla",
                             'helloworld.R'],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             text=True)
result1 = process1.communicate()
st.write(result1[1])
