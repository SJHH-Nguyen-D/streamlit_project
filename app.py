from sklearn.datasets import load_boston
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

boston = load_boston()
df = pd.DataFrame(data=boston.data, columns=boston.feature_names)
df['target'] = boston.target




st.write('Boston Housing Dataset!')
x = st.slider('x')
st.write(x, 'squared is', x * x)
st.write(df.head(20))
st.write(sns.heatmap(df.corr(), annot=True))

st.write('Udacity Self-Driving Car Project!')
# Reuse this data across runs!
read_and_cache_csv = st.cache(pd.read_csv)
BUCKET = "https://streamlit-self-driving.s3-us-west-2.amazonaws.com/"
data = read_and_cache_csv(BUCKET + "labels.csv.gz", nrows=1000)
desired_label = st.selectbox('Filter to:', ['car', 'truck'])
st.write(data[data.label == desired_label])