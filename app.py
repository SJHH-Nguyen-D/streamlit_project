from sklearn.datasets import load_boston
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pprint
import numpy as np
np.random.seed(32)

boston = load_boston()
df = pd.DataFrame(data=boston.data, columns=boston.feature_names)
df['target'] = boston.target


st.title('Streamlit Exploration')
x = st.slider('x')
st.write(x, 'squared is', x * x)

f"""{boston.DESCR}"""

st.write("Here's our first attempt at using data to create a table:")
st.write(df.head(20))

feature_label = st.selectbox('Filter to:', df.columns)
st.write(f"Distribution of {feature_label} in Boston")
st.bar_chart(data=df[feature_label], width=0, height=0, use_container_width=True)

st.subheader('Udacity Self-Driving Car Project!')
"""
The Udacity Self-Driving car project is one of the projects that the team of Streamlit often used as a case-in-point for the importance of being able to quickly spin up a powerful front-end data visualization app without the need to delve into the complex tech stack of creating front-end responsive JavaScript applications. 
"""
# Reuse this data across runs!
read_and_cache_csv = st.cache(pd.read_csv)
BUCKET = "https://streamlit-self-driving.s3-us-west-2.amazonaws.com/"
data = read_and_cache_csv(BUCKET + "labels.csv.gz", nrows=1000)
desired_label = st.selectbox('Filter to:', ['car', 'truck'])
st.write(data[data.label == desired_label])

st.subheader('Chart Playground')

if st.checkbox('Show Area Chart'):
    st.write('Area Chart')
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.area_chart(chart_data)


if st.checkbox('Show San Franciso Map'):
    st.write('San Francisco Map')
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    st.map(map_data)

if st.checkbox('Show DataFrame and Line Chart'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)